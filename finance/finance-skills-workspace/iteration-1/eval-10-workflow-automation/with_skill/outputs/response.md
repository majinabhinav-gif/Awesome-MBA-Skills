# Approval Workflow Design for Account Maintenance Requests

## Approval Matrix

Define a delegation of authority matrix that maps each maintenance type to the required approval levels, SLA targets, and escalation rules:

| Maintenance Type | Approval Levels | Approvers | SLA Target | Escalation Trigger |
|---|---|---|---|---|
| Address change | 1 | Operations analyst + team lead review | 1 business day | Yellow at 4 hours, Red at 6 hours |
| Beneficiary change | 2 | Operations analyst + team lead + compliance review | 2 business days | Yellow at 1 day, Red at 1.5 days |
| Re-registration | 3 | Operations analyst + team lead + compliance review + supervisor sign-off | 5 business days | Yellow at 2.5 days, Red at 4 days |

## State Machine Design

Model each request as a state machine with the following states. The number of approval tiers traversed depends on the request type, controlled by guard conditions on the transitions.

**States:** Received --> Validated --> Pending Approval (Tier 1) --> Pending Approval (Tier 2) --> Pending Approval (Tier 3) --> Approved --> Submitted to Custodian --> Completed | Rejected

- **Address changes** skip Tier 2 and Tier 3 -- after Tier 1 (team lead) approval, they transition directly to Approved.
- **Beneficiary changes** require Tier 1 (team lead) and Tier 2 (compliance review), then transition to Approved.
- **Re-registrations** require all three tiers: Tier 1 (team lead), Tier 2 (compliance review), and Tier 3 (supervisor sign-off).

Guard conditions on each transition enforce this logic by evaluating the request type at the gateway after Tier 1 and Tier 2 to determine whether the next tier is required or whether the request proceeds directly to Approved.

## Approval Tier Details

### Tier 1 -- Team Lead Review (All Request Types)

The team lead reviews the request for completeness and accuracy. For address changes, this is the only approval needed -- the team lead confirms the change is supported by client authorization (signed form, authenticated request, or verbal confirmation with callback verification).

- **SLA for approval action:** 4 hours from assignment
- **Timeout escalation:** If unactioned after 4 hours, send reminder to team lead. If unactioned after 6 hours, escalate to operations manager for direct approval or reassignment.
- **Delegation:** Each team lead must have a configured delegate who inherits approval authority during absences. Delegation is time-limited and logged.

### Tier 2 -- Compliance Review (Beneficiary Changes and Re-registrations)

The compliance reviewer receives a structured review package containing: the client's identity verification, the nature of the change, supporting documentation, and any risk flags (e.g., elderly client, recent advisor change, third-party beneficiary). The compliance review determines whether the change raises concerns under FINRA Rule 3110 supervisory obligations or firm-specific policies around beneficiary exploitation, estate planning changes, or unauthorized account modifications.

- **SLA for approval action:** 1 business day from assignment
- **Timeout escalation:** If unactioned after 4 business hours, send reminder to compliance reviewer. If unactioned after 6 business hours, escalate to Chief Compliance Officer.
- **Review output:** Approve, reject, or request additional information. If additional information is requested, the SLA clock pauses while the request is in "Pending Documentation" status (a sub-state that loops back to the compliance review once documentation is provided).

### Tier 3 -- Supervisor Sign-off (Re-registrations Only)

Re-registrations involve changing the legal ownership of the account (e.g., individual to trust, individual to joint, estate settlement). These changes affect cost basis continuity, tax reporting, and beneficial ownership -- all areas with regulatory implications. The supervisor (operations manager or designated senior officer) reviews the complete package including all prior approvals.

- **SLA for approval action:** 1 business day from assignment
- **Timeout escalation:** If unactioned after 4 business hours, send reminder to supervisor. If unactioned after 1 business day, escalate to the head of operations.
- **Four-eyes-plus enforcement:** The system must enforce that the supervisor is a different individual from both the initiating analyst and the Tier 1 team lead. No single person may serve as both maker and checker at any level.

## Escalation Rules

Implement aging thresholds relative to the overall SLA for each request type, following a Green/Yellow/Red/Breached model:

| Status | Threshold | Action |
|---|---|---|
| Green | Less than 50% of SLA elapsed | Normal processing. No alerts. |
| Yellow | 50% to 80% of SLA elapsed | Assigned analyst and current approver see a yellow indicator on their dashboard. Item appears on the priority list. |
| Red | 80% to 100% of SLA elapsed | Team lead and operations manager receive automated notification. If the item is waiting for an approval, the approver receives an urgent reminder. |
| Breached | SLA exceeded | Operations manager receives a breach notification. The item is flagged for mandatory root cause documentation. Included in the SLA breach report. |

### Escalation Tiers Within Each Approval Step

Each approval step has its own timeout escalation independent of the overall SLA:

- **Tier 1 escalation chain:** Reminder to team lead (2 hours) --> notification to operations manager (4 hours) --> auto-reassignment to alternate team lead (6 hours).
- **Tier 2 escalation chain:** Reminder to compliance reviewer (4 hours) --> notification to CCO (6 hours) --> CCO assumes review (1 business day).
- **Tier 3 escalation chain:** Reminder to supervisor (4 hours) --> notification to head of operations (1 business day) --> head of operations assumes sign-off (1.5 business days).

## Routing Logic

Use role-based routing with workload-based assignment within each role:

- **Address changes** route to any available operations analyst (workload-balanced), then to the assigned team lead for Tier 1 approval.
- **Beneficiary changes** route to an operations analyst, then team lead (Tier 1), then the compliance reviewer on rotation (Tier 2).
- **Re-registrations** route to a senior operations analyst (skill-based routing -- must have entity account processing certification), then team lead (Tier 1), then compliance (Tier 2), then supervisor (Tier 3).

## Audit Trail Requirements

Every action in the workflow must be logged with: who performed it (user identity, not role), what was done (state transition, approval, rejection, reassignment, escalation), when it occurred (timestamp with timezone), why (approval justification, rejection reason, escalation trigger), and the data state before and after the action. This satisfies SEC Rule 17a-3/17a-4 recordkeeping requirements and provides examination-ready documentation for FINRA Rule 3110 supervisory review.

The audit trail must be immutable -- entries cannot be modified or deleted by any user including administrators. If the workflow configuration itself changes (e.g., adding a new approval tier, changing an SLA threshold), that change must also be documented with effective date, business justification, and approver.

## Implementation Recommendations

1. **Model the delegation of authority matrix as configuration, not code.** Store the mapping of request type to required approval levels, SLA targets, and escalation thresholds in a configuration table. When the firm's risk assessment changes, the matrix can be updated without a code deployment, subject to change management controls.

2. **Handle the "Pending Documentation" sub-state.** Both beneficiary changes and re-registrations frequently stall waiting for client documents (signed beneficiary designation forms, trust agreements, court orders). When a request enters Pending Documentation, pause the SLA clock but start a separate documentation follow-up timer that sends reminders to the advisor at defined intervals (e.g., day 3, day 7, day 14) and auto-closes the request after 30 calendar days of no response.

3. **Enforce the four-eyes principle at every tier.** The system must prevent the same individual from acting as both the initiating analyst and any approver, and from serving as the approver at more than one tier for the same request. This is a non-negotiable control for FINRA supervisory compliance.

4. **Build delegation before go-live.** Every approver role must have a configured delegate before the workflow goes into production. Without delegation, a single absent team lead or compliance reviewer creates a bottleneck that breaches SLAs for the entire queue.

5. **Start with baseline measurement.** Before setting SLA targets, measure the current average cycle time for each request type. If address changes currently take 2 days on average, a 1-business-day SLA is achievable only with process improvements (such as eliminating the shared email inbox and moving to structured workflow routing). Set initial SLAs at achievable levels, then tighten them as the workflow matures.

6. **Management reporting.** Build a weekly dashboard showing: requests received and completed by type, SLA compliance rate by type, average cycle time by type, breach count and root causes, approval turnaround time by tier, and queue depth trends. Review weekly to identify bottlenecks and calibrate escalation thresholds.
