# Tiered Approval Workflow for Account Maintenance Requests

## Overview

Design a workflow engine with three distinct tiers, each mapped to a request type with escalating approval depth, SLA targets, and escalation rules. The core abstraction is a **request pipeline** where each request type declares its required approval chain, and the engine enforces ordering, timeouts, and escalation.

## Request Type Tiers

### Tier 1: Address Changes (Single Approval)

- **Approvers:** One operations representative
- **SLA Target:** 4 business hours from submission to completion
- **Escalation Rule:** If not approved within 4 hours, auto-escalate to the operations team lead
- **Validation:** Verify new address against USPS/postal database; flag PO boxes or international addresses for manual review
- **Auto-approval candidate:** Consider auto-approving if the address change matches a known pattern (e.g., USPS NCOA match) and the account has no recent suspicious activity

### Tier 2: Beneficiary Changes (Two Approvals + Compliance Review)

- **Approvers:**
  1. First approval: Operations representative (same as Tier 1)
  2. Second approval: Compliance officer
- **SLA Targets:**
  - First approval: 4 business hours
  - Compliance review: 1 business day from first approval
  - Total end-to-end: 2 business days
- **Escalation Rules:**
  - If first approval stalls past 4 hours, escalate to ops team lead
  - If compliance review stalls past 1 business day, escalate to compliance manager
  - If total SLA breaches 2 business days, notify the branch manager
- **Additional Controls:**
  - Require identity re-verification of the account holder before initiating the request
  - If the new beneficiary is a non-family member or an entity, flag for enhanced due diligence
  - Maintain an audit trail capturing who the previous beneficiary was, the reason for change, and supporting documentation

### Tier 3: Re-registrations (Three Approvals + Supervisor Sign-off)

- **Approvers:**
  1. First approval: Operations representative
  2. Second approval: Compliance officer
  3. Third approval: Supervisor or branch manager (the "supervisor sign-off")
- **SLA Targets:**
  - First approval: 4 business hours
  - Compliance review: 1 business day
  - Supervisor sign-off: 1 business day after compliance clears
  - Total end-to-end: 3 business days
- **Escalation Rules:**
  - Each stage follows the same escalation as its Tier 2 equivalent
  - If supervisor sign-off stalls past 1 business day, escalate to regional manager
  - If total SLA breaches 3 business days, generate an exception report for the COO

## Data Model

```
RequestType: ADDRESS_CHANGE | BENEFICIARY_CHANGE | RE_REGISTRATION

Request:
  id: UUID
  type: RequestType
  account_id: string
  submitted_by: string
  submitted_at: timestamp
  status: PENDING | IN_REVIEW | APPROVED | REJECTED | ESCALATED | CANCELLED
  current_step: int  (which approval step we are on, 0-indexed)
  payload: JSON      (type-specific data: new address, new beneficiary, new registration details)
  supporting_docs: list[DocumentRef]

ApprovalStep:
  id: UUID
  request_id: FK -> Request
  step_order: int
  role_required: OPS_REP | COMPLIANCE_OFFICER | SUPERVISOR
  assigned_to: string (nullable, for explicit assignment)
  status: PENDING | APPROVED | REJECTED | ESCALATED
  sla_deadline: timestamp
  decided_at: timestamp (nullable)
  decided_by: string (nullable)
  comments: text

EscalationEvent:
  id: UUID
  step_id: FK -> ApprovalStep
  escalated_to: string
  escalated_at: timestamp
  reason: SLA_BREACH | MANUAL
```

## Workflow Engine Design

### 1. Request Submission

When a request is submitted:

- Validate the payload (address format, beneficiary details, re-registration documents)
- Look up the request type to determine the approval chain template
- Create the `Request` record and generate all `ApprovalStep` records with calculated SLA deadlines
- Activate only the first step (set its status to PENDING and notify the assignee or role queue)

### 2. Approval Processing

When an approver acts on a step:

- If **approved**: mark the step as APPROVED, advance `current_step`, activate the next step (if any), notify the next approver
- If **rejected**: mark the step as REJECTED, set the overall request status to REJECTED, notify the submitter with the reason
- If it is the **final step** and approved: mark the request as APPROVED, trigger downstream processing (actually execute the change in the book of record)

### 3. SLA Monitoring and Escalation

Run a scheduled job (every 15-30 minutes) that:

- Queries all active `ApprovalStep` records where `status = PENDING` and `sla_deadline < now()`
- For each breached step:
  - Create an `EscalationEvent`
  - Re-assign or notify the escalation target based on the step's role and tier
  - Update step status to ESCALATED
  - Send notifications (email, dashboard alert, Slack/Teams message)

### 4. Escalation Chain

Define escalation targets per role:

| Original Role | Escalation Target | Second Escalation |
|---|---|---|
| OPS_REP | Ops Team Lead | Branch Manager |
| COMPLIANCE_OFFICER | Compliance Manager | Chief Compliance Officer |
| SUPERVISOR | Regional Manager | COO |

If the first escalation does not resolve within another SLA window (e.g., 50% of the original SLA), trigger the second escalation.

## Implementation Recommendations

### State Machine

Model each request as a finite state machine. States are derived from the combination of `Request.status` and `Request.current_step`. Transitions are triggered by approver actions or SLA breaches. This makes the workflow auditable and easy to extend with new tiers.

```
SUBMITTED -> STEP_0_PENDING -> STEP_0_APPROVED -> STEP_1_PENDING -> ...
                            -> STEP_0_REJECTED -> REJECTED
                            -> STEP_0_ESCALATED -> (re-enters STEP_0_PENDING with new assignee)
```

### Separation of Concerns

- **Workflow definition layer:** Declarative configuration of which request types need which approval chains. Store this as configuration, not code, so adding a new request type does not require a deployment.
- **Execution engine:** Generic engine that reads the workflow definition and processes steps. Handles assignment, notification, SLA tracking, and escalation.
- **Integration layer:** Connects to the book-of-record system to execute the actual change once fully approved. Also connects to notification systems (email, messaging).

### Audit and Compliance

- Every state transition must be logged immutably with timestamp, actor, and action
- Support "four-eyes" principle: no single person can both submit and approve a request
- For Tier 2 and Tier 3, enforce that the compliance reviewer is a different person from the operations approver
- Retain all records for the regulatory retention period (typically 6-7 years for FINRA-regulated firms)

### Configuration-Driven Design

Define approval chains in a configuration file or database table rather than hardcoding:

```yaml
approval_chains:
  ADDRESS_CHANGE:
    steps:
      - role: OPS_REP
        sla_hours: 4
        escalation_target: OPS_TEAM_LEAD
  BENEFICIARY_CHANGE:
    steps:
      - role: OPS_REP
        sla_hours: 4
        escalation_target: OPS_TEAM_LEAD
      - role: COMPLIANCE_OFFICER
        sla_hours: 8
        escalation_target: COMPLIANCE_MANAGER
  RE_REGISTRATION:
    steps:
      - role: OPS_REP
        sla_hours: 4
        escalation_target: OPS_TEAM_LEAD
      - role: COMPLIANCE_OFFICER
        sla_hours: 8
        escalation_target: COMPLIANCE_MANAGER
      - role: SUPERVISOR
        sla_hours: 8
        escalation_target: REGIONAL_MANAGER
```

This approach allows you to add new request types (e.g., account closure, power-of-attorney changes) without modifying the engine code.

### Notifications

Each step transition should trigger a notification to the relevant party:

- **Step activated:** Notify the approver (or the role queue) that action is required
- **SLA warning:** Send a reminder at 75% of the SLA window
- **SLA breach:** Notify the escalation target
- **Request completed:** Notify the original submitter and the account holder
- **Request rejected:** Notify the submitter with the rejection reason and instructions for resubmission

### Dashboard and Reporting

Build a dashboard that shows:

- Open requests by type and current step
- SLA compliance rates (percentage completed within SLA by tier)
- Average processing time per tier and per step
- Escalation frequency and resolution time
- Aging report for requests approaching or past SLA

This data supports operational management and regulatory examination readiness.
