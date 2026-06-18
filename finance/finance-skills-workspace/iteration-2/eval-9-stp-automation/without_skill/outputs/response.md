# Automating ACATS Transfers: Raising STP Rate from ~40% to 90%+

## Understanding the Problem

A 60% manual intervention rate on incoming ACATS (Automated Customer Account Transfer Service) transfers is high but not uncommon at firms that grew their operations organically. The typical pain points are:

- **Data format mismatches** between the ACATS/NSCC feed and your internal systems
- **Manual re-keying** across multiple systems (often a transfer management system, a book-of-record, and a CRM or client portal)
- **Position matching failures** where incoming transfer items do not cleanly reconcile against your holdings master or security reference data
- **Missing or incomplete customer data** that requires outreach before the transfer can settle

Getting to 90%+ STP (straight-through processing) is achievable, but it requires addressing each failure category systematically rather than trying to build one monolithic automation.

## Recommended Approach

### Phase 1: Instrument and Categorize (Weeks 1-3)

Before automating anything, you need data on *why* transfers require manual intervention. Tag every manual touch with a reason code:

| Category | Typical Causes |
|---|---|
| **Security matching** | CUSIP/SEDOL not in your reference data, or mapped differently |
| **Account matching** | Incoming account number does not map to an existing client record |
| **Position reconciliation** | Quantity or lot-level detail mismatches |
| **Data enrichment** | Missing SSN, tax ID, registration details, or beneficiary info |
| **Asset type unsupported** | Alternative investments, limited partnerships, physical certificates |
| **Regulatory holds** | Cost basis gaps, restricted securities, control/affiliate shares |

This categorization will show you where the 60% breaks down. In most firms, 2-3 categories account for 80% of the failures.

### Phase 2: Build the Matching and Enrichment Layer (Weeks 4-8)

This is where you get the biggest STP gains. Build (or configure) an integration layer between the NSCC/ACATS feed and your internal systems:

1. **Security reference data mapping.** Create a robust CUSIP-to-internal-ID mapping table. Subscribe to a reference data feed (e.g., from your clearing firm, or a vendor like Refinitiv or Bloomberg) to auto-resolve new or unfamiliar securities. Fuzzy matching on security description can catch many edge cases.

2. **Account matching rules engine.** Build deterministic matching first (exact account number, exact SSN+name), then probabilistic matching (name similarity, address overlap) for cases where the contra firm uses different identifiers. Flag low-confidence matches for human review rather than rejecting them outright.

3. **Position reconciliation automation.** For equity and fixed-income positions, automate quantity matching with tolerance thresholds (e.g., fractional share rounding differences). For mutual funds, handle share-class conversions automatically where your firm offers the equivalent class.

4. **Data enrichment via API.** Where your systems need fields the ACATS feed does not carry (e.g., full beneficiary details, cost basis at the lot level), build API integrations to pull from the delivering firm's systems or from DTCC's Cost Basis Reporting Service (CBRS).

### Phase 3: Workflow Orchestration (Weeks 6-10, overlapping with Phase 2)

Replace the manual copy-paste across three systems with an orchestration layer:

- **Event-driven processing.** When an ACATS transfer instruction arrives from NSCC, it should trigger an automated pipeline: validate, match, enrich, book, and confirm. Each step either succeeds (moves to next) or routes to exception queue with context.
- **Exception management UI.** For the remaining manual cases, build a single screen that shows the ops team everything they need: the incoming transfer data, the matching candidates in your systems, and the specific reason it could not auto-process. Pre-populate as much as possible so the human intervention is a review-and-confirm rather than re-keying.
- **Status tracking.** Give the ops team (and ideally the advisor/client) real-time visibility into where each transfer stands in the pipeline.

### Phase 4: Continuous Improvement (Ongoing)

- **Monitor STP rates daily** by category. When a new failure pattern emerges, add a rule or mapping to handle it.
- **Cost basis automation.** Cost basis is one of the last things to go fully STP because of ACATS limitations. Consider CBRS integration and automated lot-matching logic.
- **Partial transfers.** These are harder to automate because they require asset-level selection logic. Start by automating full transfers and handle partials as a later optimization.
- **ACAT reject handling.** Build automated retry logic for common reject codes (e.g., timing issues, temporary holds) rather than having ops manually resubmit.

## Technical Architecture Considerations

- **Do not replace your three systems.** Instead, build an integration/orchestration layer on top of them. Ripping out book-of-record or transfer management systems is a multi-year project that will delay your STP improvements.
- **Use idempotent operations.** Transfers can be amended, rejected, and resubmitted. Your automation must handle re-processing without creating duplicates.
- **Audit trail.** Every automated decision (match, enrichment, booking) must be logged with the data that drove it. Regulators and your compliance team will require this.
- **Reconciliation checkpoints.** Even with automation, run end-of-day reconciliation between NSCC records, your transfer system, and your book-of-record. Automation that silently misbooks is worse than manual processing.

## Realistic STP Targets

| Milestone | Expected STP Rate | Timeline |
|---|---|---|
| After Phase 1 (instrumented, no automation) | 40% (baseline) | Week 3 |
| After Phase 2 (matching + enrichment) | 70-75% | Week 8 |
| After Phase 3 (orchestration + exception mgmt) | 85-90% | Week 12 |
| After 6 months of tuning | 90-95% | Month 6 |

Getting above 95% is possible but requires handling long-tail edge cases (alternative assets, physical certificates, accounts with legal restrictions) that may not justify the automation investment.

## Key Risks

- **Data quality in your own systems.** If your security master or account records are incomplete, the matching layer will have a low ceiling. Clean your own data first.
- **Clearing firm dependencies.** If you clear through a third party, your automation options may be constrained by their APIs and data formats. Engage them early.
- **Change management.** Your ops team currently has tribal knowledge about handling edge cases. Capture this knowledge before automating, or you will lose it.
- **Regulatory timing requirements.** ACATS has specific timeframes (3 business days for validation, 6 for settlement). Your automation must respect these deadlines and escalate before they are missed, not after.

## Summary

The path from 40% to 90%+ STP is: instrument first, then automate matching and enrichment (biggest ROI), then orchestrate the end-to-end workflow, then continuously tune. Resist the urge to build a single large system -- an integration layer on top of your existing three systems will deliver results faster and with less risk.
