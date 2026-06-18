# Compliance Requirements for Opening a Family Trust Account with Mixed US/UK Trustees and a Corporate Trustee

This is a complex account opening scenario that triggers multiple enhanced compliance requirements. The trust involves three individual trustees (two US persons, one UK resident), a corporate trustee, and cross-border tax obligations. Here is a structured walkthrough of every compliance gate.

---

## 1. Account Classification and Risk Tier Assignment

This account will not qualify for auto-approval. Based on risk-based review tier frameworks, this trust triggers **Tier 3 (Compliance Review)** at minimum due to:

- **Complex entity structure** -- a trust with multiple trustees including a corporate trustee
- **Cross-border element** -- a UK-resident trustee introduces foreign jurisdiction considerations
- **Multi-party account** -- four associated parties (three individuals plus one corporate trustee) all requiring screening

The first step is to classify the trust: **revocable or irrevocable**. This distinction drives the beneficial ownership analysis:

- **Revocable (living) trust** where the grantor retains control: generally treated as an individual account for CDD purposes, with the grantor as the beneficial owner.
- **Irrevocable trust**: a legal entity subject to full beneficial ownership requirements under the FinCEN CDD Rule, requiring identification of all 25%+ beneficial owners and at least one control person.

Obtain the trust document or a trust certification to make this determination before proceeding.

---

## 2. CIP Verification for All Individual Trustees

Under USA PATRIOT Act Section 326, every individual associated with the account must be verified before the account becomes active. For this trust, that means CIP verification on all three individual trustees.

### Two US-Person Trustees

Standard database verification via an identity verification vendor (e.g., LexisNexis, Alloy, Equifax). Submit name, date of birth, address, and SSN/TIN. Expect real-time pass/fail/inconclusive results. These should be straightforward assuming clean credit files.

### UK-Resident Trustee

CIP verification for a non-US person presents additional complexity:

- **Database verification coverage is weaker** for non-US persons. Documentary verification (passport upload with liveness check) will likely be the primary method.
- **Acceptable identification**: passport number and country of issuance, alien identification card number, or another unexpired government-issued document evidencing nationality or residence bearing a photograph.
- Route this trustee to the documentary verification path directly rather than attempting database verification first and waiting for it to fail.
- Collect a passport copy, verify via OCR and liveness detection, and retain the verification record.

**Recordkeeping**: For all three trustees, retain identifying information, a description of the verification method used, the vendor response, timestamp, outcome, and resolution of any discrepancies. These records must be retained for 5 years after the account is closed.

---

## 3. CIP and Beneficial Ownership for the Corporate Trustee

The corporate trustee is a legal entity associated with the trust account. This triggers its own layer of compliance:

- **Entity classification**: Determine whether the corporate trustee qualifies for any CDD Rule exemption (publicly traded company, SEC-registered entity, bank, broker-dealer, government entity, etc.). If exempt, document the exemption and bypass beneficial ownership collection for the corporate trustee itself.
- **If not exempt**: Collect a FinCEN beneficial ownership certification for the corporate trustee, identifying:
  - Every individual owning 25% or more of the corporate trustee's equity (ownership prong)
  - At least one individual with significant managerial responsibility -- CEO, CFO, managing member, etc. (control prong)
- **Trace indirect ownership**: If any 25%+ owner of the corporate trustee is itself an entity, trace through intermediate entities until you reach natural persons.
- **Verify and screen each identified beneficial owner** of the corporate trustee using the same CIP procedures and OFAC screening applied to individual account holders.
- **Collect formation documents** and a corporate resolution or operating agreement authorizing the corporate trustee to act in the trust capacity.

---

## 4. Beneficial Ownership Determination for the Trust Itself

Under the FinCEN CDD Rule (31 CFR 1010.230), if this is an irrevocable trust:

- **Ownership prong**: Identify any beneficiary with a 25% or greater ascertainable interest in the trust. If the trust document grants the trustee broad discretion over distributions (discretionary trust), beneficial interests may not be fixed, making this determination challenging. Document your methodology and rationale.
- **Control prong**: Identify at least one individual with significant responsibility for controlling, managing, or directing the trust. Typically this is the trustee with primary decision-making authority. If the corporate trustee serves as the primary decision-maker, identify the individual at the corporate trustee who exercises that control.
- All identified beneficial owners must be verified (CIP) and screened (OFAC).
- The certification form must be signed by an individual authorized to act on behalf of the trust.

---

## 5. OFAC and Sanctions Screening

OFAC screening is mandatory for **every individual and entity associated with this account** before activation. The scope for this trust includes:

- All three individual trustees
- The corporate trustee (as an entity)
- Beneficial owners of the corporate trustee (if not exempt)
- Any beneficiaries identified under the CDD ownership prong
- Any individuals with power of attorney or trading authority over the account

Screen against the full suite of lists: SDN list, Sectoral Sanctions Identifications (SSI), Non-SDN Menu-Based Sanctions, Foreign Sanctions Evaders (FSE), FinCEN 314(a), and any firm-specific restricted lists.

**The UK-resident trustee** warrants particular attention: confirm there are no connections to sanctioned jurisdictions beyond the UK itself (which is not a sanctioned jurisdiction, but the individual's nationality, dual citizenship, or business connections may introduce additional screening considerations).

**Potential match handling**: Any alert halts the account opening process. A compliance analyst must review, comparing all available identifying data, and document the disposition (true positive or false positive with rationale). No account activation until all alerts are resolved.

---

## 6. PEP and Negative Media Screening

Run PEP (Politically Exposed Person) screening on all three individual trustees and the control person of the corporate trustee. The UK-resident trustee triggers foreign PEP screening -- foreign senior political figures, their family members, and close associates are flagged for enhanced review.

Run adverse media screening on all associated individuals. Any hits above the firm's severity threshold escalate the application to compliance review.

---

## 7. Tax Compliance: FATCA and CRS

This is where the cross-border element creates significant complexity.

### FATCA

- **Two US-person trustees**: Collect a **W-9** from each.
- **UK-resident trustee**: Collect a **W-8BEN** (or W-8BEN-E if acting in a fiduciary capacity for an entity). Determine the trustee's FATCA classification.
- **Trust entity classification**: Classify the trust under FATCA. Is it an Active NFFE, Passive NFFE, or a Financial Institution? For a Passive NFFE, identify any controlling persons who are US persons (the two US-person trustees likely qualify, triggering FATCA reporting).
- **Corporate trustee**: Collect a W-8BEN-E with the corporate trustee's FATCA classification.

Failure to collect valid W-8/W-9 forms triggers **backup withholding at 24%** on reportable payments.

### CRS (Common Reporting Standard)

- The **UK-resident trustee** triggers CRS obligations. If the trustee is tax-resident in the UK (a CRS-participating jurisdiction), the firm must:
  - Collect a **CRS self-certification of tax residency**, including the foreign taxpayer identification number (UK National Insurance number, format: 2 letters + 6 digits + 1 letter).
  - Report the account to HMRC via the firm's CRS reporting channel.
- Determine whether the trust itself has reporting obligations in the UK based on the UK trustee's role and the trust's activities.

### Multi-Jurisdictional Reporting

Because the trust has both US persons and a UK tax resident associated with it, the firm may need to report under **both FATCA and CRS**. The account opening system should identify these multi-jurisdictional obligations and route the account for compliance review of its reporting requirements.

Set **W-8 renewal triggers** -- W-8 forms expire every 3 years unless a change of circumstances occurs.

---

## 8. Suitability Assessment

Collect the full investment profile for the trust account as required by FINRA Rule 2111 and Regulation Best Interest:

- Investment objectives, risk tolerance, time horizon, liquidity needs
- Financial situation of the trust (assets, income, distributions)
- Investment experience of the trustees (collectively and individually)
- Tax status of the trust
- Any restrictions in the trust document on permitted investments

For a discretionary advisory account, establish an **Investment Policy Statement (IPS)** at account opening.

If any trustees are age 65 or older, this triggers senior investor protections (trusted contact designation, enhanced suitability review).

Under **Reg BI**, document the rationale for the recommended account type (brokerage vs. advisory, fee structure) and deliver Form CRS before or at the time of the first recommendation.

---

## 9. Trust-Specific Documentation

Collect and review:

- **Trust agreement or trust certification** -- confirms the trust's existence, names the trustees, defines their powers, identifies beneficiaries, and specifies any investment restrictions
- **Evidence of each trustee's authority** -- the trust document should authorize each named trustee to act on behalf of the trust; determine whether all trustees must act jointly or any can act independently
- **Corporate trustee authorization** -- a board resolution or equivalent document authorizing the corporate trustee to act in its capacity and designating the individual(s) authorized to execute transactions
- **EIN verification** -- confirm the trust's Employer Identification Number

---

## 10. Compliance Checklist Summary

Before this account can be activated, the following must be complete and documented:

| Requirement | Scope |
|---|---|
| Trust classification (revocable/irrevocable) | Trust document reviewed and classification documented |
| CIP verification -- US trustees | Database verification pass for both |
| CIP verification -- UK trustee | Documentary verification (passport + liveness) |
| Corporate trustee entity classification | Exempt or non-exempt determination documented |
| Beneficial ownership certification (trust) | Ownership and control prongs identified and documented |
| Beneficial ownership certification (corporate trustee) | If not exempt: 25%+ owners and control person identified |
| CIP verification -- all beneficial owners | Verified per firm CIP procedures |
| OFAC screening -- all associated persons and entities | Clear or false-positive disposition documented |
| PEP screening -- all individuals | Clear or escalated for enhanced review |
| Negative media screening | Clear or escalated if above threshold |
| W-9 collection -- US persons | Both US trustees |
| W-8BEN collection -- UK trustee | Collected with FATCA classification |
| CRS self-certification -- UK trustee | Collected with UK TIN |
| Trust FATCA classification | Active/Passive NFFE or Financial Institution |
| Suitability questionnaire | Complete for the trust account |
| Trust agreement or certification | Collected and reviewed |
| Corporate trustee resolution | Collected |
| Trusted contact designation | Collected (mandatory effort for all; critical if any trustee is 65+) |
| CDD risk rating assignment | Assigned based on risk factors |
| Ongoing monitoring triggers established | Periodic review date, event-driven triggers, OFAC rescreening |
| Compliance review and approval | Tier 3 reviewer sign-off with documented rationale |

---

## 11. Ongoing Monitoring Triggers Set at Opening

Given the complexity of this account, assign an **elevated CDD risk rating** (medium-high or high). This drives:

- **Annual periodic review** of beneficial ownership, trustee status, and trust terms
- **Event-driven review triggers**: change in trustees, change in beneficiaries, corporate trustee merger or restructuring, death of a trustee, UK trustee's change of tax residency
- **OFAC rescreening** on every list update for all associated persons
- **Transaction monitoring baselines** established from the trust's stated purpose and expected activity patterns
- **W-8 renewal tracking** for the UK trustee (3-year expiration)
- **CRS reporting obligations** tracked and executed annually

Document the handoff from account opening compliance to ongoing monitoring explicitly, including all conditions of approval, the risk rating, and the next scheduled review date.

---

## Key Risks Specific to This Scenario

1. **Screening all parties**: The most common pitfall is screening only the primary trustee and missing joint trustees, the corporate trustee, and beneficial owners. Every associated person and entity must be screened.
2. **Indirect ownership through the corporate trustee**: If the corporate trustee holds a beneficial interest in the trust (not just a fiduciary role), trace its ownership to natural persons.
3. **Cross-border tax compliance**: The combination of US persons and a UK tax resident creates dual FATCA/CRS reporting obligations that must be identified and tracked from day one.
4. **Trust classification error**: Misclassifying a revocable trust as irrevocable (or vice versa) changes the entire beneficial ownership analysis. Get this right from the trust document before proceeding.
5. **Corporate trustee authority**: Ensure the individual signing on behalf of the corporate trustee is actually authorized to do so per the corporate resolution. An unauthorized signer invalidates the beneficial ownership certification.
