# Approval Workflow Design for Account Maintenance Requests

## Overview

This design implements a tiered approval workflow for three account maintenance request types -- address changes, beneficiary changes, and re-registrations -- each with distinct approval depth, SLA targets, and escalation rules. The design follows BPM fundamentals and the delegation of authority matrix pattern, with state machine modeling, timeout escalation, and audit trail requirements built in from the start.

---

## 1. Delegation of Authority Matrix

The approval matrix maps each maintenance type to its required approval chain, SLA target, and rationale:

| Maintenance Type | Approval Levels | Approvers | SLA Target | Rationale |
|---|---|---|---|---|
| Address change | 1 | Operations analyst + team lead review | 1 business day | Low risk, no documentation beyond client confirmation. Single maker-checker approval is sufficient. |
| Beneficiary change | 2 | (1) Operations analyst + team lead review, (2) Compliance review | 2 business days | Beneficiary changes affect asset disposition and are a common vector for elder exploitation or unauthorized changes. Compliance review ensures the change is consistent with client instructions and flags any red flags (e.g., changing beneficiary shortly after advisor change, elderly client with new unrelated beneficiary). |
| Re-registration | 3 | (1) Operations analyst, (2) Senior analyst or team lead, (3) Supervisor sign-off | 5 business days | Re-registrations (e.g., individual to trust, individual to joint, estate transfers) involve legal documentation, custodian re-titling, and cost basis continuity. The complexity and potential for error warrant three levels of review including a supervisory sign-off for FINRA Rule 3110 purposes. |

---

## 2. State Machine Design

Model each request as a state machine with the following states and transitions:

```
States:
  Received --> Validated --> Pending Approval (Tier 1) --> [Pending Approval (Tier 2)]
    --> [Pending Approval (Tier 3)] --> Approved --> Submitted to Custodian
    --> Completed

  At any approval tier:  --> Rejected (terminal)
  At any approval tier:  --> Returned for Information (loops back to Validated)
  After 30 calendar days in Pending Documentation: --> Auto-Cancelled
```

**Guard conditions on transitions:**

- **Received to Validated:** All required fields populated, client identity confirmed, supporting documents attached (for beneficiary changes and re-registrations).
- **Validated to Pending Approval (Tier 1):** Validation checks pass. The system evaluates the request type and automatically determines how many approval tiers are required.
- **Tier 1 to Tier 2:** Only for beneficiary changes and re-registrations. Tier 1 approval is recorded before the item advances.
- **Tier 2 to Tier 3:** Only for re-registrations. Tier 2 approval is recorded before the item advances.
- **Final approval tier to Approved:** All required approvals are recorded. The four-eyes principle is enforced -- the initiating analyst cannot also serve as an approver at any tier.

**Request type determines the approval path automatically:**

- Address change: Tier 1 only (team lead review), then Approved.
- Beneficiary change: Tier 1 (team lead review), then Tier 2 (compliance review), then Approved.
- Re-registration: Tier 1 (operations analyst peer review or senior analyst), then Tier 2 (team lead review), then Tier 3 (supervisor sign-off), then Approved.

---

## 3. SLA Targets and Aging Thresholds

### SLA by Request Type

| Request Type | SLA Target | SLA Clock Starts | SLA Clock Stops |
|---|---|---|---|
| Address change | 1 business day | When request enters Received state | When request reaches Completed state |
| Beneficiary change | 2 business days | When request enters Received state | When request reaches Completed state |
| Re-registration | 5 business days | When request enters Received state | When request reaches Completed state |

Note: SLA clock pauses while in the Returned for Information or Pending Documentation state (waiting on the client or advisor), but only if the request for information was sent within the first 50% of the SLA window. Late requests for information do not pause the clock -- this prevents gaming the SLA by requesting trivial information near the deadline.

### Aging Thresholds (Applied Per Request Type)

| Color | Threshold | Action |
|---|---|---|
| Green | 0-50% of SLA elapsed | Normal processing. No special action. |
| Yellow | 50-80% of SLA elapsed | Item appears on priority list. Assigned analyst receives a dashboard indicator. |
| Red | 80-100% of SLA elapsed | Team lead notified. Item escalated to next tier if not actively being worked. |
| Breached | Over 100% of SLA elapsed | Operations manager notified. Formal breach recorded. Item included in SLA breach report with root cause documentation required. |

**Concrete timing for each type:**

- Address change (1-day SLA): Yellow at 4 hours, Red at 6.4 hours, Breached at 8 hours (assuming 8-hour business day).
- Beneficiary change (2-day SLA): Yellow at 8 hours, Red at 12.8 hours, Breached at 16 hours.
- Re-registration (5-day SLA): Yellow at 2.5 days, Red at 4 days, Breached at 5 days.

---

## 4. Escalation Rules Per Approval Tier

### Tier 1 -- Team Lead / Peer Review (All Request Types)

| Elapsed Time Without Action | Escalation |
|---|---|
| 2 hours | Automated reminder to the assigned Tier 1 approver |
| 4 hours | Notification to the team lead's manager or an alternate team lead. If a delegate is configured, the item is reassigned to the delegate. |
| 6 hours | Item reassigned to the operations manager for direct approval or reassignment |

### Tier 2 -- Compliance Review (Beneficiary Changes) / Team Lead Review (Re-registrations)

| Elapsed Time Without Action | Escalation |
|---|---|
| 4 hours | Automated reminder to the assigned Tier 2 reviewer |
| 8 hours (1 business day) | For compliance review: escalation to the Chief Compliance Officer. For team lead review: escalation to the operations manager. |
| 12 hours | Item reassigned to an alternate reviewer with equivalent authority |

### Tier 3 -- Supervisor Sign-Off (Re-registrations Only)

| Elapsed Time Without Action | Escalation |
|---|---|
| 4 hours | Automated reminder to the assigned supervisor |
| 8 hours | Escalation to the next-level supervisor or operations director |
| 12 hours | Escalation to the head of operations or COO |

### Delegation Rules (All Tiers)

- Each approver must have a configured delegate who inherits approval authority during absence.
- Delegation is time-limited (auto-expires at the end of the configured period).
- The delegate cannot further delegate.
- The audit trail records that the delegate approved on behalf of the primary approver, including the delegation authorization reference.

---

## 5. Compliance Review Package (Tier 2, Beneficiary Changes)

When a beneficiary change reaches Tier 2 compliance review, the workflow assembles a structured review package for the compliance analyst:

- **Client profile:** Name, age, account type, relationship tenure.
- **Current beneficiary designation:** Names, percentages, relationships to client.
- **Proposed beneficiary designation:** Names, percentages, relationships to client.
- **Change context:** Who initiated the request (client directly, advisor on behalf of client), method of instruction (signed form, verbal with written follow-up), and whether the client confirmed the change independently.
- **Risk indicators:** Client age over 65 (senior investor protection), beneficiary changed within 90 days of advisor change, new beneficiary is unrelated to client, beneficiary change removes a spouse or child.
- **Supporting documents:** Signed beneficiary designation form, any correspondence.

The compliance analyst reviews the package and selects one of: Approve, Reject (with documented reason), or Request Additional Information (which returns the item to the operations analyst with specific questions).

---

## 6. Supervisor Sign-Off Package (Tier 3, Re-registrations)

When a re-registration reaches Tier 3 supervisor sign-off, the workflow assembles:

- **Account details:** Current registration, proposed registration, account value, tax lot positions.
- **Legal documentation status:** Trust agreement (reviewed and on file), court order (if applicable), letters testamentary (for estate transfers).
- **Custodian requirements:** Confirmation that the custodian's specific re-registration requirements are met (varies by custodian).
- **Cost basis continuity:** Verification that cost basis will transfer correctly under the new registration.
- **Prior approval trail:** Tier 1 and Tier 2 approval decisions with approver identities, timestamps, and comments.

The supervisor reviews the complete package and provides sign-off, rejection, or requests additional information. This sign-off satisfies FINRA Rule 3110 supervisory review obligations.

---

## 7. Audit Trail Requirements

Every action in the workflow must be logged with:

- **Who:** User identity (not just role) of the person performing the action.
- **What:** The specific action (state change, approval, rejection, reassignment, escalation, data modification).
- **When:** Timestamp with timezone.
- **Why:** Decision rationale -- approval reason, rejection reason, override justification, or escalation trigger.
- **Data state:** Before-and-after values for any data modifications (e.g., old beneficiary vs. new beneficiary).

Audit log entries must be immutable (write-once, append-only) to satisfy SEC Rule 17a-4 preservation requirements. Configuration changes to the workflow itself (e.g., changing an SLA threshold or adding an approval tier) must also be logged with the effective date, business justification, and the identity of the person who authorized the change.

---

## 8. Notification Design

To avoid notification fatigue, follow these principles:

- **Address changes** (high volume, low risk): Escalation reminders only -- no proactive notifications to approvers for each item. Approvers work from a prioritized queue.
- **Beneficiary changes** (moderate volume, moderate risk): Push notification to the compliance reviewer when an item enters their queue. Escalation reminders at the intervals defined above.
- **Re-registrations** (lower volume, higher complexity): Push notification to each tier's approver when the item enters their queue, plus escalation reminders.
- **Batch digest:** Team leads and operations managers receive a once-daily summary of open items by aging band rather than individual item alerts, unless an item is in Red or Breached status (those generate immediate alerts).

---

## 9. Management Reporting

Build a weekly SLA dashboard that shows:

- Total requests received and completed by type.
- SLA compliance rate by maintenance type (target: 90% or above).
- Average cycle time by maintenance type and by approval tier (to identify which tier creates the most latency).
- Breach count with root cause categories (approver delay, missing documentation, custodian delay, system issue).
- Approval turnaround time by tier and by approver (to identify chronic bottlenecks).
- Rework rate (items returned for information as a percentage of total items).

---

## 10. Implementation Recommendations

1. **Model the workflow as roles, not named individuals.** Route to "Team Lead" and "Compliance Reviewer" roles, not to specific people. When staff change, update the role assignment, not the workflow.

2. **Measure the baseline before setting SLAs.** If current address change turnaround averages 2 days, setting a 1-day SLA requires process changes (parallel validation, pre-populated forms, automated custodian submission) before the SLA is achievable.

3. **Enforce the four-eyes principle in code.** The workflow engine must programmatically prevent the request initiator from approving at any tier. This is not a policy control -- it is a system control.

4. **Test escalation paths before go-live.** Simulate approver absence scenarios and verify that delegation, timeout, and reassignment rules work correctly. A single misconfigured escalation can halt the entire queue for a request type.

5. **Integrate with downstream systems.** The workflow should trigger custodian submissions, CRM updates, and confirmation generation automatically upon final approval. A workflow that tracks status but still requires manual entry into the custodian portal adds overhead without reducing effort.

6. **Document the rules in written supervisory procedures.** The approval matrix, escalation thresholds, and delegation rules must exist in the firm's written supervisory procedures, not just in the workflow engine's configuration. This is required for FINRA Rule 3110 compliance and examination defensibility.
