# Automating ACAT Transfers: From 40% to 90%+ STP

## Diagnosis

A 60% manual intervention rate on incoming ACATs, with staff copying data between three systems and manually matching transfer items, points to two root causes that account for the vast majority of your STP breaks:

1. **Data quality and identifier mismatches.** When transfer items arrive via ACATS, the security identifiers, account numbers, or asset descriptions from the delivering firm do not automatically reconcile against your internal records. This forces manual lookup and matching.
2. **Lack of system integration.** Copying data between three systems means there is no automated data flow connecting them. Each manual handoff is a point where errors are introduced and processing stalls.

Before building anything, you need to know exactly where the breaks occur. The Pareto principle applies here: 20% of root causes typically account for 80% of exceptions.

## Recommended Approach

### Phase 1 -- Baseline and Root Cause Analysis (Weeks 1-4)

Define precisely what "STP" means for your ACAT process: an incoming transfer is received, items are matched against your records, positions are accepted or rejected, and the transfer completes with zero human intervention.

Instrument your current process to categorize every manual touch. For four weeks, have your ops team log the reason they intervene on each transfer. You will likely find categories such as:

- **Identifier mismatches** -- the delivering firm uses a different security identifier (CUSIP vs. ISIN vs. ticker) than your system of record
- **Missing or stale reference data** -- a security in the transfer does not exist in your security master, or the record is outdated
- **Data format inconsistencies** -- fields from the ACATS feed do not match the expected format in your destination systems
- **Account mapping failures** -- the receiving account cannot be automatically identified from the transfer data
- **Asset type exceptions** -- certain asset types (alternative investments, annuities, physical certificates) require manual handling by nature
- **System re-keying** -- data must be manually entered because there is no integration between the three systems

Rank these categories by volume multiplied by average resolution time. This is your prioritized remediation list.

### Phase 2 -- Data Quality Remediation (Months 1-3)

Attack the highest-volume exception categories first. Based on typical ACAT exception profiles:

**Security identifier cross-referencing.** Build or procure a cross-reference service that maps between CUSIP, ISIN, SEDOL, and ticker symbols. When an incoming ACAT item uses an identifier your system does not recognize, the cross-reference service translates it automatically. This single step often eliminates the largest category of matching failures.

**Reference data enrichment.** Audit your security master against the universe of securities that actually appear in incoming transfers. Identify securities that are missing or have stale data. Establish an automated feed (from your market data provider or custodian) that keeps the security master current. Transfers that break because "we don't have that CUSIP in the system" should drop to near zero.

**Standardize data formats.** Map the field formats from the ACATS feed to the expected formats in each of your three systems. Build a translation layer that normalizes dates, quantities, currency codes, account identifiers, and other fields automatically. This eliminates the "formatting error" exception category entirely.

**Expected improvement:** STP rate from 40% to approximately 60-65%.

### Phase 3 -- System Integration (Months 3-6)

The manual copying between three systems is where you are burning the most labor hours. Replace it with automated data flow.

**Evaluate integration options for each system pair.** For each of your three systems, determine the best integration pattern:

- If the system offers an API (REST, SOAP, FIX), use API-based integration. This is the gold standard -- structured, versioned, testable, and real-time.
- If the system only supports file-based exchange, implement automated file generation, transfer, and ingestion with monitoring for failures.
- If the system is a legacy application with no API and no file interface, use RPA as a temporary bridge, but plan to replace it with a proper integration. RPA is brittle and should not be treated as a permanent solution.

**Build a workflow orchestration layer.** Instead of humans routing work between systems, implement a workflow engine that:

1. Receives the incoming ACAT notification
2. Runs automated matching of each transfer item against your security master (using the cross-reference service from Phase 2)
3. Validates completeness and consistency of all data fields
4. For items that pass all validation, automatically updates all three systems and marks the transfer item as accepted
5. For items that fail validation, routes to an exception queue with the specific failure reason pre-identified

**Implement standing instruction databases.** If your ACAT matching requires looking up account-level or counterparty-level instructions, centralize these in a single reference database that all three systems consume.

**Expected improvement:** STP rate from 60-65% to approximately 80-85%.

### Phase 4 -- Exception Management and Auto-Resolution (Months 6-9)

With the major data quality and integration issues resolved, the remaining 15-20% of exceptions are lower-volume, more varied cases. Implement structured exception handling:

**Exception categorization and queuing.** Route every exception to a typed queue (data quality, document, matching, system error, asset type). The ops analyst sees exactly what failed and why, rather than having to investigate from scratch.

**Auto-resolution rules for well-understood exceptions.** Examples relevant to ACATs:

- If a position quantity differs by a small fractional amount (e.g., fractional share rounding differences under 0.01 shares), auto-match within the tolerance
- If a security identifier is missing but the security description plus CUSIP partial match uniquely identifies the asset, auto-populate and re-process
- If a cost basis discrepancy falls below a de minimis threshold, accept the delivering firm's basis and flag for later review

Each auto-resolution rule must be documented with its rationale, risk assessment, and approval. Overly aggressive auto-resolution introduces silent errors.

**Prioritize exception queues.** Transfers with approaching deadlines, high dollar values, or repeat exceptions from the same source should surface first. Implement aging-based escalation so nothing sits unresolved.

**Expected improvement:** STP rate from 80-85% to approximately 90-92%.

### Phase 5 -- Monitoring and Continuous Improvement (Ongoing)

**STP rate dashboard.** Build a real-time or daily view showing:
- Overall ACAT STP rate and trend over time
- Exception volume breakdown by category
- Top exception generators (delivering firms, asset types, account types)
- Aging distribution of open exceptions
- Auto-resolution rate (what percentage of exceptions are resolved without human intervention)

**Continuous improvement cycle.** Each month, review the top 3-5 exception categories by volume, investigate root causes, and implement fixes. A reasonable improvement cadence is 3-5 percentage points per quarter when below 80%, and 1-2 points per quarter above 80% as marginal gains become harder.

**Change management for automation rules.** Any rule change must be tested against historical transfer data to confirm it fixes the targeted exception without breaking STP for previously automated items. Regression testing is essential.

## Implementation Priorities

If you need to sequence this work against a limited budget, the order of impact is:

1. **Baseline measurement** -- you cannot improve what you have not measured; instrument the process first
2. **Security identifier cross-referencing** -- likely your single highest-volume exception category
3. **System-to-system integration** -- eliminates the manual re-keying entirely
4. **Pre-transfer validation rules** -- catches problems before they enter the exception queue
5. **Auto-resolution rules** -- handles the long tail of minor discrepancies
6. **Dashboard and monitoring** -- sustains the improvement over time

## Key Pitfalls to Avoid

- **Do not automate the current manual process as-is.** First ask whether each step is necessary. Automating an unnecessary review step just makes it a faster unnecessary step.
- **Do not skip the baseline.** Without knowing your current exception breakdown, you will invest in the wrong areas.
- **Do not treat RPA as the answer.** If you use bots to copy data between your three systems, you have automated the symptom (manual copying) without fixing the cause (no system integration). The bots will break every time a UI changes.
- **Do not set loose matching tolerances to inflate your STP rate.** Aggressive auto-matching creates silent errors that surface later as reconciliation breaks or client complaints.
- **Do not neglect your ops team.** Reposition staff from manual processing to exception analysis, process improvement, and client service. The goal is not headcount reduction -- it is redeploying skilled people to higher-value work.

## Realistic Timeline and Targets

| Milestone | Timeline | Expected STP Rate |
|-----------|----------|-------------------|
| Baseline measurement complete | Week 4 | 40% (current) |
| Data quality remediation | Month 3 | 60-65% |
| System integration live | Month 6 | 80-85% |
| Auto-resolution and exception management | Month 9 | 90-92% |
| Continuous improvement steady state | Month 12+ | 92-95% |

Getting from 40% to 90% is achievable within 9 months if you prioritize data quality first, integration second, and auto-resolution third. The jump from 90% to 95%+ requires progressively more investment for each marginal point of improvement, so evaluate whether the remaining manual exceptions justify the cost of further automation or are better handled by a smaller, specialized exceptions team.
