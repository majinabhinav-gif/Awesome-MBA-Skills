# Automating ACATs to Achieve 90%+ STP

## Current State Assessment

A 60% manual intervention rate on incoming ACATs means roughly 6 out of every 10 transfers require your ops team to touch them -- copying data between systems, manually matching transfer items, and resolving discrepancies by hand. Before building anything, you need to understand exactly why those 60% are failing to process automatically. The approach below is structured in phases that address root causes in priority order.

## Phase 1: Baseline Measurement and Root Cause Analysis (Weeks 1-4)

First, define precisely what "STP completion" means for your ACAT process: an incoming transfer is received, validated, matched against your records, accepted or rejected, and assets are re-registered -- all without any human touching it. Any manual intervention at any step means that transfer is not STP.

Instrument your current process to categorize every manual touch. Have ops staff track the reason each time they intervene. You will likely find something like:

- **Data mismatches between systems** (the transfer agent sends identifiers or account data in a format that does not match your records) -- often the largest category
- **Security matching failures** (CUSIP/identifier mismatches, fractional shares, DTC-ineligible securities, or securities not in your master)
- **Account data discrepancies** (name, SSN/TIN, or registration mismatches between the incoming ACAT and your records)
- **Missing or stale reference data** (your system lacks standing instructions or counterparty data for the delivering firm)
- **Manual re-keying between systems** (data exists in one system but must be hand-entered into another because the systems are not integrated)

The Pareto principle almost certainly applies: 20% of root causes are driving 80% of your exceptions. Identify the top 3-5 categories by volume before writing any code.

## Phase 2: Data Quality Remediation (Months 1-3)

Data quality issues are the single largest source of STP breaks, and fixing them delivers the highest return for the lowest effort. Target the top exception categories from your baseline:

**Security identifier cross-referencing.** If incoming ACATs use a different identifier than your internal records (e.g., they send CUSIP and you store by ISIN, or vice versa), build or procure a cross-reference service that maps between identifier types automatically. When an incoming transfer item references a security by one identifier, the system should resolve it to your internal identifier without human lookup.

**Account data normalization.** Standardize name formats, address formats, and registration descriptions across your three systems. Incoming ACAT data often has slight variations (abbreviated names, different address line structures, different trust registration phrasing) that cause matching failures. Implement fuzzy matching with a confidence threshold: matches above 95% confidence auto-resolve, matches below that route to manual review.

**Reference data completeness.** Audit your counterparty and delivering-firm data against the NSCC participant list. Ensure you have standing data for every firm you regularly receive transfers from. Missing counterparty data forces manual lookup on every transfer from that firm.

Expected improvement: STP rate from 40% to 60-65%.

## Phase 3: System Integration (Months 3-6)

Your ops team copying data between three systems is a pure integration problem, not a process problem. This is where the largest efficiency gains come from after data quality is addressed.

**Eliminate re-keying with API-based integration.** Identify which of your three systems can communicate programmatically (APIs, file exports/imports, database connections). The goal is that when an incoming ACAT notification arrives, the data flows automatically to all systems that need it:

- If your systems support APIs, build real-time integrations so that an incoming transfer notification in System A automatically creates the corresponding records in Systems B and C.
- If APIs are not available, implement message-queue-based integration (e.g., a message broker that receives the ACAT notification and distributes it to each system's import mechanism).
- If one or more systems are legacy with no API or import facility, use RPA as a temporary bridge -- but plan to replace it. RPA is brittle (UI changes break the bot) and should be treated as a tactical stopgap, not a permanent architecture.

**Automated matching engine.** Build rule-based matching logic for incoming transfer items against your records:

1. **Exact match pass.** Match on security identifier + quantity. If both match exactly, auto-accept the item.
2. **Tolerance match pass.** If quantities differ by a small amount (e.g., fractional shares below a threshold), auto-match with a notation.
3. **Cross-reference match pass.** If the security identifier does not match directly but resolves via cross-reference to a known holding, auto-match.
4. **Exception routing.** Items that fail all three passes route to an exception queue with the specific failure reason pre-categorized, so the ops analyst sees exactly what is wrong rather than having to investigate from scratch.

Expected improvement: STP rate from 60-65% to 80-85%.

## Phase 4: Exception-Based Processing and Auto-Resolution (Months 6-9)

With data quality fixed and systems integrated, the remaining exceptions are lower-volume and more varied. Shift from a review-all model to a review-exceptions model:

**Tiered processing.** Not all ACATs need the same treatment:

- **Tier 1 (full STP):** Simple transfers of listed equities and standard mutual funds between known counterparties with clean data. These process end-to-end with zero human review. Target: 70-75% of volume.
- **Tier 2 (light-touch review):** Transfers involving less common security types, minor data discrepancies that auto-resolution could not handle, or counterparties with a history of data issues. An analyst reviews only the flagged items, not the entire transfer. Target: 15-20% of volume.
- **Tier 3 (full review):** Transfers with DTC-ineligible securities, partial transfers with complex lot selection, or account registration mismatches requiring legal review. Target: 5-10% of volume.

**Auto-resolution rules.** For well-understood, low-risk exception categories, implement automated fixes:

- If a security identifier is missing but can be derived from other fields (ticker + exchange), auto-populate and re-process.
- If a quantity mismatch is due to a known corporate action (stock split, dividend reinvestment) that occurred between the transfer initiation and receipt, auto-adjust.
- If an account name mismatch is within fuzzy-match tolerance and all other fields (SSN, account number) match exactly, auto-accept with an audit log entry.

Each auto-resolution rule needs documented rationale, risk assessment, approval from operations management and compliance, and periodic review. Over-aggressive auto-resolution introduces silent errors.

Expected improvement: STP rate from 80-85% to 90-93%.

## Phase 5: Monitoring, Controls, and Continuous Improvement (Ongoing)

**STP rate dashboard.** Build a real-time view showing:

- Current STP rate for ACATs (daily, weekly, monthly trend)
- Exception volume breakdown by category
- Top exception generators (delivering firms, security types, account types)
- Aging distribution of open exceptions
- Auto-resolution rate (what percentage of exceptions are resolved without human touch)

**Operational controls.** Automation does not eliminate controls -- it changes them:

- Every automated action must have an audit trail (input data, rule applied, decision made, action taken, timestamp).
- Separation of duties: the person configuring auto-resolution rules is not the same person approving them for production.
- Rule changes go through a development-testing-approval-deployment cycle with regression testing against historical data.
- Automated reconciliation serves as the primary detective control -- if the automation is producing errors, reconciliation surfaces them.

**Continuous improvement cycle.** STP improvement is iterative:

1. Measure current STP rates and exception profiles.
2. Identify the top 3-5 exception categories by volume.
3. Rank by impact (volume multiplied by cost-per-exception) and feasibility.
4. Implement the fix (data quality improvement, rule adjustment, new auto-resolution, system enhancement).
5. Verify the exception volume decreases as expected.
6. Repeat with the next set of exception categories.

A reasonable improvement cadence is 3-5 percentage points per quarter for processes below 80% STP, and 1-2 percentage points per quarter above 80%.

## Realistic Timeline and Targets

| Phase | Timeframe | Expected STP Rate | Key Actions |
|-------|-----------|-------------------|-------------|
| Baseline | Weeks 1-4 | 40% (current) | Measure, categorize every manual touch |
| Data quality | Months 1-3 | 60-65% | Identifier cross-referencing, name normalization, reference data cleanup |
| Integration | Months 3-6 | 80-85% | API-based system integration, automated matching engine |
| Auto-resolution | Months 6-9 | 90-93% | Tiered processing, auto-resolution rules, exception queuing |
| Optimization | Ongoing | 93-95% | Dashboard monitoring, continuous improvement cycles |

## Key Risks to Watch

- **Do not automate a bad process.** Before automating any step, ask whether the step is necessary at all. Redesign first, then automate.
- **Do not neglect data quality.** Investing in system enhancements without fixing data quality yields disappointing results. Data quality is the foundation.
- **Do not treat RPA as permanent.** If you use RPA to bridge legacy systems, have a plan and timeline to replace bots with API integrations.
- **Do not skip regression testing.** A new auto-resolution rule that fixes one exception category may break STP for another. Test every rule change against the full range of transfer types.
- **Do not set it and forget it.** Automated processes need continuous monitoring and reconciliation. Without alerting, errors compound undetected.

The 90% target is achievable within 9 months if data quality is genuinely addressed first. Trying to build automation on top of inconsistent data is the most common reason these initiatives underdeliver.
