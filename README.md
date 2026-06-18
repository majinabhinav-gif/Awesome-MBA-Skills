# MBA Skills

A consolidated collection of **93 Claude Skills** spanning the core disciplines of an MBA curriculum — Finance, Strategy & Consulting, Marketing, and Product Management. Each skill is a self-contained `SKILL.md` (plus any supporting references, templates, examples, and scripts) that Claude can load on demand.

This repository merges four formerly separate skill packs into one organized library. Per-pack `README` and `LICENSE` files have been removed; see [LICENSE](LICENSE) for consolidated licensing and attribution.

## Repository layout

```
MBA-Skills/
├── finance/              84 skills — markets, wealth, compliance, operations
├── strategy-consulting/   1 skill  — MBB-level management consultant (+113 reference modules)
├── marketing/             1 skill  — marketing research & positioning
└── product-management/    7 skills — discovery → roadmap → user stories (+ master orchestrator)
```

To use a skill with Claude Code, point it at the relevant `SKILL.md`, or install a domain folder into your `~/.claude/skills` directory.

---

## 💰 Finance — `finance/`

84 skills organized into seven plugin groups (see `finance/plugins/`). Also retains the original `CLAUDE.md`, `evals/`, and `finance-skills-workspace/` (benchmark/test infrastructure).

| Group | Count | Skills |
|-------|-------|--------|
| **core** | 3 | return-calculations · statistics-fundamentals · time-value-of-money |
| **wealth-management** | 32 | asset-allocation · diversification · rebalancing · tax-efficiency · tax-loss-harvesting · equities · fixed-income (corporate/municipal/sovereign/structured) · alternatives · commodities · real-assets · digital-assets · currencies-and-fx · valuation (qualitative/quantitative) · performance (metrics/attribution/reporting) · risk (historical/forward) · volatility-modeling · investment-policy · liquidity-management · debt-management · lending · savings-goals · emergency-fund · bet-sizing · fund-vehicles · finance-psychology |
| **compliance** | 16 | reg-bi · fiduciary-standards · advice-standards · investment-suitability · know-your-customer · anti-money-laundering · conflicts-of-interest · fee-disclosure · client-disclosures · advertising-compliance · sales-practices · books-and-records · regulatory-reporting · examination-readiness · gips-compliance · privacy-data-security |
| **advisory-practice** | 12 | client-onboarding · client-review-prep · client-reporting-delivery · crm-client-lifecycle · financial-planning-workflow · financial-planning-integration · proposal-generation · next-best-action · advisor-dashboards · order-management-advisor · portfolio-management-systems · fee-billing |
| **trading-operations** | 9 | order-lifecycle · trade-execution · pre-trade-compliance · post-trade-compliance · settlement-clearing · exchange-connectivity · margin-operations · counterparty-risk · operational-risk |
| **client-operations** | 8 | account-opening-workflow · account-opening-compliance · account-maintenance · account-transfers · corporate-actions · reconciliation · stp-automation · workflow-automation |
| **data-integration** | 4 | market-data · reference-data · data-quality · integration-patterns |

## 📊 Strategy & Consulting — `strategy-consulting/`

- **management-consultant** — MBB-level (McKinsey/Bain/BCG) structured problem solver: issue trees, MECE, hypothesis-driven analysis, market sizing, profitability, market entry, M&A, pricing, ops, org design, and executive-grade deliverables. Backed by **113 reference modules** in `management-consultant/references/`.
- Supporting material retained: `FRAMEWORKS.md`, `CASE-STUDIES.md`, `case-studies/` (Apollo Hospitals FY27 sample engagement), `assets/`, `INSTALL.md`, `GITHUB-SETUP-GUIDE.md`, `NOTICE`.

## 📣 Marketing — `marketing/`

- **marketing-research** — practitioner-grade research system for products, avatars, markets, competitors, and positioning: value propositions, ICP/avatar profiling, unique mechanisms, market awareness/sophistication, and copywriting research for landing pages, ads, and email. Includes `examples/` and an install `scripts/`.

## 🚀 Product Management — `product-management/`

| Skill | Purpose |
|-------|---------|
| **pm-master** | Master orchestrator — routes and sequences the six skills below and turns outputs into decks/spreadsheets |
| **jobs-to-be-done** | Uncover customer jobs, pains, and gains in structured JTBD format |
| **discovery-process** | Full discovery cycle: framing → interviews → synthesis → experiments |
| **prioritization-advisor** | Choose a prioritization framework (RICE, ICE, value/effort, …) |
| **product-strategy-session** | End-to-end strategy across positioning, discovery, and roadmap |
| **roadmap-planning** | Turn strategy into a sequenced, stakeholder-aligned release plan |
| **user-story** | Mike Cohn–format stories with Gherkin acceptance criteria |

---

## Sources & licensing

This library aggregates four upstream projects. Original `README`/`LICENSE` files were removed during consolidation; license terms and attribution are preserved in [LICENSE](LICENSE):

| Domain | Upstream pack | License |
|--------|---------------|---------|
| finance | `finance_skills` (© 2026 Joel Lewis) | MIT |
| strategy-consulting | `claude-skill-management-consultant-B1` | Apache-2.0 |
| marketing | `claude-marketing-research-skill` | Apache-2.0 |
| product-management | `pm-skills-starter-pack` | (unspecified upstream) |
