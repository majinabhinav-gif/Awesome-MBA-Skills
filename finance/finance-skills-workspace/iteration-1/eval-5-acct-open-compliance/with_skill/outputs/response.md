# Compliance Requirements for Opening a Family Trust Account with Mixed US/UK Trustees and a Corporate Trustee

This is a complex account opening that triggers multiple enhanced compliance requirements. The combination of a trust structure, a non-US person (UK resident trustee), and a corporate trustee places this account squarely in Tier 3 (Compliance Review) -- it will require full manual compliance review before activation. Here is a step-by-step walkthrough of what is required.

---

## 1. Trust Classification and Documentation

First, determine the trust type -- revocable or irrevocable -- because this drives the entire beneficial ownership analysis.

- **Revocable (living) trust where the grantor retains control:** For CDD purposes, the grantor is treated as the beneficial owner. The trust is essentially treated like an individual account.
- **Irrevocable trust:** This is a legal entity subject to full beneficial ownership requirements under the FinCEN CDD Rule (31 CFR 1010.230). You must identify all beneficial owners under both the ownership prong (25%+ equity interest) and the control prong.

**Action items:**
- Obtain and review the trust document (trust agreement or trust certification).
- Classify the trust as revocable or irrevocable and document the classification.
- Identify all trustees, beneficiaries, grantors, and any persons with authority over the trust.
- If irrevocable, proceed with full beneficial ownership determination (see Section 3 below).

---

## 2. CIP Verification for All Three Individual Trustees

Under USA PATRIOT Act Section 326, you must verify the identity of each person associated with the account. For a trust, this means all trustees. No account activation until CIP clears for every trustee.

### Two US Person Trustees
- Run database verification (name, date of birth, address, SSN) through your identity verification vendor API.
- Expect standard pass/fail/inconclusive results. Pass results advance automatically.

### UK Resident Trustee
- This is a non-US person, which introduces additional complexity. Database verification coverage is weaker for non-US persons.
- **Route this trustee directly to the documentary verification path** -- do not require a failed database check first. Collect a passport upload with liveness detection.
- Acceptable identification: passport number and country of issuance, or another unexpired government-issued document evidencing nationality or residence that bears a photograph.
- Collect the trustee's foreign address and passport number (no SSN available; use passport number as the identification number).
- **Recordkeeping:** Retain the identification method, verification results, and any discrepancy resolution for 5 years after account closure.

**If any CIP result is inconclusive:** Route to an exception queue with a defined resolution window (typically 3-5 business days). Request additional documentation. Do not open the account until all three trustees clear CIP.

---

## 3. Beneficial Ownership Certification (FinCEN CDD Rule)

If this is an irrevocable trust (or any trust where the grantor does not retain control), the trust is a legal entity customer subject to full beneficial ownership requirements.

### Ownership Prong (25%+ Equity Interest)
- Determine which beneficiaries hold ascertainable interests of 25% or more in the trust.
- For trusts with discretionary distribution provisions (where the trustee has sole discretion), identifying 25% owners is challenging because beneficial interests are not fixed. Document your methodology for this determination.
- If no beneficiary has a clearly ascertainable 25%+ interest, document that finding and the rationale.

### Control Prong
- Identify at least one individual with significant responsibility for controlling, managing, or directing the trust.
- Typically the trustee is identified as the control person. With three individual trustees and a corporate trustee, you need to determine which individual(s) exercise primary control.
- **Corporate trustee complication:** You cannot name a corporate entity as the control person -- the CDD Rule requires a natural person. Identify the individual at the corporate trustee entity who has day-to-day responsibility for managing the trust relationship (e.g., trust officer, managing director). That individual must be identified and verified as the control person.

### Certification Form
- Collect a FinCEN beneficial ownership certification form (or your firm's equivalent).
- The form must be signed by an individual authorized to act on behalf of the trust.
- Verify the identity (CIP) and run OFAC screening on every identified beneficial owner and control person -- including the individual identified through the corporate trustee.

---

## 4. OFAC and Sanctions Screening

OFAC screening must cover **all individuals associated with the account**, not just the primary contact. For this trust, that means screening:

- All three individual trustees (both US persons and the UK resident)
- The corporate trustee entity itself
- The individual(s) at the corporate trustee identified as control persons
- All identified beneficial owners/beneficiaries with 25%+ interests
- Any authorized signers or persons with trading authority
- The grantor(s) of the trust

**Screen against:** OFAC SDN list, Sectoral Sanctions Identifications (SSI) list, Non-SDN Menu-Based Sanctions list, Foreign Sanctions Evaders (FSE) list, FinCEN 314(a) list, and any firm-specific restricted lists.

**UK resident trustee:** The presence of a UK person does not in itself create a sanctions issue (the UK is not a high-risk jurisdiction), but you must still screen this individual against all lists. Verify there are no connections to sanctioned jurisdictions through dual nationality, business interests, or other ties.

**Potential match handling:** If any screening produces a potential match, halt the account opening entirely. Route the alert to a compliance analyst. The analyst compares all identifying data points (name, date of birth, nationality, address, passport number) and makes a true positive/false positive determination. Document the analysis thoroughly. For a true positive: block the application and file a blocked property report with OFAC within 10 business days.

---

## 5. PEP Screening and Adverse Media

- Screen all trustees, beneficial owners, and the corporate trustee's control person against PEP databases.
- The UK resident trustee warrants particular attention -- screen for foreign PEP status (senior political figures, family members, close associates).
- Run adverse media screening on all associated individuals and the corporate trustee entity.
- PEP matches or significant adverse media hits trigger enhanced due diligence, including source-of-wealth analysis.

---

## 6. Enhanced Due Diligence -- Risk Factors Specific to This Account

This account has multiple enhanced review triggers that collectively warrant Tier 3 (Compliance Review) or potentially Tier 4 (Senior Compliance/CCO Review):

| Risk Factor | Trigger |
|---|---|
| Complex ownership structure | Trust with multiple trustees including a corporate trustee |
| Multiple authorized parties | Three individual trustees plus a corporate trustee entity |
| Non-US person | UK resident trustee -- weaker CIP verification, cross-border considerations |
| Entity involvement | Corporate trustee requires identification of underlying control persons |

**Additional documentation to collect:**
- Source of funds/source of wealth statement for the trust
- Purpose of the account
- Expected account activity (investment strategy, anticipated deposits/withdrawals)
- Corporate trustee's formation documents, evidence of regulatory status (if applicable), and identification of the individual officer responsible for the trust
- Any relevant tax documentation (W-9 for US persons, W-8BEN for the UK resident trustee)

---

## 7. Suitability Assessment

- Collect the full investment profile: objectives, risk tolerance, time horizon, liquidity needs, financial situation, investment experience, and tax status.
- Determine who has investment authority -- do all three individual trustees act jointly, or does the corporate trustee have sole discretion?
- If the account will be managed on a discretionary basis, establish an Investment Policy Statement (IPS) at opening.
- Document the account type recommendation rationale under Reg BI (if broker-dealer) or fiduciary duty of care analysis (if RIA).
- Deliver Form CRS (broker-dealer) or Form ADV Part 2A/2B (RIA) and collect acknowledgment.

---

## 8. Senior Investor Protections

- Determine the ages of all three individual trustees. If any trustee is 65 or older, trigger senior investor protections.
- Collect trusted contact person information under FINRA Rule 4512 (for all customers, but especially if any trustee is a senior investor).
- Flag the account for age-based monitoring if applicable.

---

## 9. Risk Rating and Ongoing Monitoring Setup

At the conclusion of the opening process, assign a CDD risk rating. Given the complexity of this account, expect a **medium-high or high** risk rating based on:
- Trust structure with multiple trustees
- Corporate trustee involvement
- Non-US person (UK resident) associated with the account
- Multi-party authorization structure

**Set the following ongoing monitoring triggers:**
- Annual periodic review (high-risk entity schedule)
- Event-driven review triggers: changes to trustees, changes to beneficiaries, changes in corporate trustee personnel, significant changes in account activity
- OFAC rescreening on all associated persons whenever OFAC lists are updated
- Monitor for UK regulatory or tax changes that could affect the trust structure

---

## 10. Compliance Checklist Summary

Before this account can be activated, confirm completion of every item:

- [ ] Trust document obtained and reviewed
- [ ] Trust classified as revocable or irrevocable (documented)
- [ ] CIP verification passed for US Trustee 1
- [ ] CIP verification passed for US Trustee 2
- [ ] CIP verification passed for UK Resident Trustee (documentary verification)
- [ ] Corporate trustee formation documents collected
- [ ] Corporate trustee control person identified and CIP verified
- [ ] Beneficial ownership certification form completed and signed by authorized individual
- [ ] Beneficial owner identities verified (CIP) for all identified beneficial owners
- [ ] OFAC screening clear for all associated individuals and the corporate trustee entity
- [ ] PEP screening completed for all associated individuals
- [ ] Adverse media screening completed
- [ ] Suitability questionnaire completed
- [ ] Investment authority documented (joint vs. sole, discretionary vs. non-discretionary)
- [ ] Account type recommendation rationale documented (Reg BI / fiduciary)
- [ ] Form CRS or Form ADV delivered and acknowledged
- [ ] Source of funds/wealth documented
- [ ] Trusted contact person collected (or refusal documented)
- [ ] Senior investor protections applied (if any trustee is 65+)
- [ ] CDD risk rating assigned
- [ ] Ongoing monitoring triggers configured
- [ ] Periodic review date scheduled
- [ ] Compliance analyst review completed and documented (Tier 3 sign-off)
- [ ] W-9 collected for US person trustees; W-8BEN collected for UK resident trustee

---

## Key Risk to Watch

The most common failure point with trust accounts like this one is **incomplete beneficial ownership determination**. Specifically:

1. Failing to look through the corporate trustee to identify the natural person with control -- you cannot stop at the entity level.
2. Not tracing indirect ownership through the trust structure to identify beneficiaries with 25%+ interests.
3. Accepting a certification signed by someone not authorized to act on behalf of the trust.
4. Screening only the "primary" trustee against OFAC rather than all trustees, beneficial owners, and the corporate trustee's control person.

Document every step of your analysis and every compliance decision. Examiners reviewing trust account files will focus on whether the firm's beneficial ownership methodology was consistently applied and whether all associated persons were properly identified, verified, and screened.
