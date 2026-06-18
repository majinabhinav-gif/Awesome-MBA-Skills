# Approval Workflow Design for Account Maintenance Requests

## Overview

This design uses a tiered approval model where each request type maps to a workflow tier with escalating approval depth, SLA targets, and escalation rules.

## Request Type Classification

| Request Type | Tier | Approvals Required | Special Requirements |
|---|---|---|---|
| Address Change | Tier 1 | 1 (operations) | None |
| Beneficiary Change | Tier 2 | 2 (operations + compliance) | Compliance review |
| Re-registration | Tier 3 | 3 (operations + compliance + supervisor) | Supervisor sign-off |

## Data Model

### Core Entities

**MaintenanceRequest**
- `request_id` (unique identifier)
- `request_type` (ADDRESS_CHANGE | BENEFICIARY_CHANGE | RE_REGISTRATION)
- `account_id`
- `submitted_by`
- `submitted_at`
- `status` (PENDING_APPROVAL | APPROVED | REJECTED | ESCALATED | EXPIRED)
- `current_approval_level` (1, 2, or 3)
- `required_approval_levels` (derived from request type)
- `payload` (the actual change details)

**ApprovalStep**
- `step_id`
- `request_id` (foreign key)
- `level` (1, 2, or 3)
- `approver_role` (OPERATIONS | COMPLIANCE | SUPERVISOR)
- `approver_id`
- `decision` (PENDING | APPROVED | REJECTED | ESCALATED)
- `decision_at`
- `comments`
- `sla_deadline`

**EscalationRecord**
- `escalation_id`
- `request_id`
- `from_level`
- `escalated_to`
- `reason`
- `escalated_at`

## Workflow Engine Design

### State Machine

Each request follows a linear approval chain. The state machine for a Tier N request:

```
SUBMITTED
  -> PENDING_LEVEL_1
    -> APPROVED_LEVEL_1 (if N > 1, goto PENDING_LEVEL_2; else COMPLETED)
    -> REJECTED (terminal)
    -> ESCALATED_LEVEL_1
  -> PENDING_LEVEL_2
    -> APPROVED_LEVEL_2 (if N > 2, goto PENDING_LEVEL_3; else COMPLETED)
    -> REJECTED (terminal)
    -> ESCALATED_LEVEL_2
  -> PENDING_LEVEL_3
    -> APPROVED_LEVEL_3 -> COMPLETED
    -> REJECTED (terminal)
    -> ESCALATED_LEVEL_3
```

### Approval Level Definitions

**Level 1 -- Operations Review**
- Approver pool: Operations team members
- Validates: data completeness, supporting documentation, account standing
- Applies to: all request types

**Level 2 -- Compliance Review**
- Approver pool: Compliance officers
- Validates: regulatory requirements (AML/KYC for beneficiary changes, tax implications, ERISA considerations if applicable)
- Applies to: Beneficiary Changes, Re-registrations

**Level 3 -- Supervisor Sign-off**
- Approver pool: Department supervisors / senior management
- Validates: overall risk assessment, high-value or unusual patterns, final authorization
- Applies to: Re-registrations only

## SLA Targets and Escalation Rules

### SLA by Tier and Level

| Tier | Level | SLA Target | Escalation Trigger |
|---|---|---|---|
| Tier 1 | Level 1 (Ops) | 4 business hours | Auto-escalate at 4h |
| Tier 2 | Level 1 (Ops) | 4 business hours | Auto-escalate at 4h |
| Tier 2 | Level 2 (Compliance) | 8 business hours | Auto-escalate at 8h |
| Tier 3 | Level 1 (Ops) | 4 business hours | Auto-escalate at 4h |
| Tier 3 | Level 2 (Compliance) | 8 business hours | Auto-escalate at 8h |
| Tier 3 | Level 3 (Supervisor) | 24 business hours | Auto-escalate at 24h |

### Escalation Chain

Each level has a two-stage escalation:

1. **Warning** at 75% of SLA: Notify the assigned approver and their backup via email/notification.
2. **Auto-escalate** at 100% of SLA: Reassign to the next person in the escalation chain.

Escalation chains by level:

- **Level 1 (Ops):** Assigned analyst -> Senior analyst -> Operations manager
- **Level 2 (Compliance):** Assigned compliance officer -> Senior compliance officer -> Chief compliance officer
- **Level 3 (Supervisor):** Assigned supervisor -> Department head -> Division executive

### Business Hours Calculation

SLAs are measured in business hours (e.g., 9:00-17:00 local time, excluding weekends and firm holidays). The SLA clock pauses outside business hours and resumes the next business day.

## Implementation Architecture

### Recommended Approach: Event-Driven with a Workflow Queue

```
[Client/UI] -> [API Gateway] -> [Request Service]
                                      |
                                      v
                               [Workflow Engine]
                                 |          |
                          [Approval Queue]  [SLA Timer Service]
                                 |                |
                          [Notification Service]  [Escalation Service]
                                 |
                          [Audit Log]
```

**Request Service** -- Accepts new maintenance requests, validates input, determines the tier, and creates the initial approval chain.

**Workflow Engine** -- Manages state transitions. When an approval is recorded, it checks whether the next level is needed or the request is complete.

**SLA Timer Service** -- Runs on a schedule (e.g., every 15 minutes). Checks all PENDING approval steps against their SLA deadlines. Fires warning or escalation events as needed.

**Escalation Service** -- Handles reassignment logic. Picks the next approver in the escalation chain and updates the approval step.

**Notification Service** -- Sends alerts for new approvals needed, SLA warnings, escalations, and final decisions.

**Audit Log** -- Immutable record of every state change, approval, rejection, escalation, and notification. Critical for regulatory compliance.

### Key Design Decisions

**1. Sequential, not parallel approvals.** Each level must complete before the next begins. This ensures lower levels filter out obvious issues before consuming senior reviewers' time.

**2. Any rejection is terminal.** A rejection at any level stops the workflow. The submitter must create a new request with corrections. This keeps the audit trail clean.

**3. Approvers cannot approve their own requests.** Enforce separation of duties -- the submitter is excluded from the approver pool at all levels.

**4. Delegation support.** Allow approvers to delegate to a named substitute (e.g., during PTO). Delegations are logged and time-bound.

**5. Idempotent state transitions.** The workflow engine should handle duplicate approval events gracefully (e.g., approver clicks "Approve" twice).

## API Design

### Submit a Request
```
POST /api/v1/maintenance-requests
Body: { account_id, request_type, payload, supporting_documents[] }
Response: { request_id, status, approval_chain[] }
```

### Record an Approval Decision
```
POST /api/v1/maintenance-requests/{request_id}/approvals/{level}
Body: { decision: "APPROVED" | "REJECTED", comments }
Response: { request_id, status, next_pending_level }
```

### Query Request Status
```
GET /api/v1/maintenance-requests/{request_id}
Response: { request_id, status, approval_chain[], escalation_history[] }
```

### List Pending Approvals (for an approver's queue)
```
GET /api/v1/approvals/pending?approver_id={id}&role={role}
Response: { items[]: { request_id, request_type, level, sla_deadline, submitted_at } }
```

## Compliance and Audit Considerations

- **Immutable audit trail.** Every action (submission, approval, rejection, escalation, notification) is logged with timestamp, actor, and before/after state.
- **Retention.** Maintain approval records for the firm's regulatory retention period (typically 6-7 years under SEC Rule 17a-4).
- **Access controls.** Role-based access ensures only authorized personnel can approve at each level. Compliance officers cannot be bypassed for Tier 2/3 requests.
- **Reporting.** Build dashboards for SLA compliance rates, average approval times by tier, escalation frequency, and rejection rates. These metrics help identify bottlenecks and staffing needs.

## Example Walkthrough: Beneficiary Change (Tier 2)

1. Client submits beneficiary change request via portal.
2. System creates request with `required_approval_levels = 2`.
3. **Level 1 (Operations):** Request appears in ops queue. SLA clock starts (4 business hours). Analyst verifies documentation (new beneficiary form, ID verification). Analyst approves.
4. **Level 2 (Compliance):** Request moves to compliance queue. SLA clock starts (8 business hours). Compliance officer reviews for AML red flags, confirms the beneficiary relationship is documented, checks for OFAC screening. Compliance approves.
5. Request status moves to COMPLETED. Downstream systems process the beneficiary update. Client receives confirmation.

If the compliance officer does not act within 6 hours (75% of 8h SLA), a warning notification fires. At 8 hours, the request auto-escalates to the senior compliance officer.
