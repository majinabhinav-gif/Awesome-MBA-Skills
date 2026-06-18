# GitHub Setup Guide — Publishing Your Consulting Skill

This guide walks you through creating the GitHub repo and optimizing it for maximum discoverability — search engines, AI systems, GitHub search, and human discovery.

---

## Step 1: Create the GitHub Repository

1. Go to [github.com/new](https://github.com/new)
2. Set the **Repository name** to:
   ```
   mbb-management-consultant-claude-skill
   ```
3. Set the **Description** to (copy exactly — this is indexed by GitHub and Google):
   ```
   Free MBB-level management consultant AI skill for Claude. McKinsey/Bain/BCG frameworks, case interview prep, market sizing, strategy consulting tools for MBA students, consultants & business professionals.
   ```
4. Set to **Public**
5. Check **Add a README file** → No (we have our own)
6. Set **License** → MIT
7. Click **Create repository**

---

## Step 2: Upload Your Files

### Option A: GitHub Web Interface (No Code Required)

1. In your new repo, click **Add file → Upload files**
2. Upload all files from the outputs folder:
   - `README.md`
   - `INSTALL.md`
   - `FRAMEWORKS.md`
   - `CASE-STUDIES.md`
   - `LICENSE`
3. Create a `skill/` folder:
   - Click **Add file → Create new file**
   - Type `skill/SKILL.md` in the filename box (the slash creates the folder)
   - Paste the contents of your SKILL.md
4. Upload all reference files into `skill/references/`:
   - Click **Add file → Upload files**
   - Navigate into `skill/references/` first
   - Upload all 80+ reference markdown files

### Option B: Git Command Line

```bash
# Clone your new empty repo
git clone https://github.com/YOUR_USERNAME/mbb-management-consultant-claude-skill.git
cd mbb-management-consultant-claude-skill

# Copy files into the repo folder
cp /path/to/outputs/README.md .
cp /path/to/outputs/INSTALL.md .
cp /path/to/outputs/FRAMEWORKS.md .
cp /path/to/outputs/CASE-STUDIES.md .
cp /path/to/outputs/LICENSE .

# Copy skill files
mkdir -p skill/references
cp /path/to/skill/SKILL.md skill/
cp /path/to/skill/references/*.md skill/references/

# Commit and push
git add .
git commit -m "Initial release: MBB management consultant skill for Claude"
git push origin main
```

---

## Step 3: Configure GitHub Settings for Maximum Discoverability

### Add Repository Topics (Critical for SEO)

In your repo, click the gear icon next to "About" on the right sidebar. Add these topics:

```
management-consulting
mbb
mckinsey
bain
bcg
consulting-frameworks
case-interview
mba
strategy-consulting
claude-ai
anthropic
ai-skill
business-strategy
structured-thinking
mece
pyramid-principle
market-sizing
profitability-analysis
case-prep
business-frameworks
```

### Set the Website

In the "About" section, add the website URL if you have one (even a LinkedIn URL works). This creates a backlink and shows authority.

### Enable GitHub Pages (Optional but Powerful)

1. Go to **Settings → Pages**
2. Select **Deploy from a branch → main → / (root)**
3. Click **Save**

GitHub will generate a free website at `https://YOUR_USERNAME.github.io/mbb-management-consultant-claude-skill/` — this gets indexed by Google separately from the repo itself, doubling your SEO surface area.

---

## Step 4: Write Your First GitHub Issue (Seed Content)

Create a "pinned" issue as a welcome/discussion thread:

**Title**: `Welcome — How are you using this skill? 👋`

**Body**:
```markdown
Welcome to the MBB Management Consultant Skill for Claude!

Share how you're using it:
- 🎓 Case interview prep
- 💼 Real consulting work
- 📊 Business strategy and analysis
- 🏫 MBA coursework
- 🚀 Startup strategy

Drop your use case below — it helps others discover the skill and helps me prioritize improvements.

**Quick links:**
- [Installation Guide](./INSTALL.md)
- [Frameworks Reference](./FRAMEWORKS.md)
- [Worked Case Studies](./CASE-STUDIES.md)
```

Pin this issue. It becomes a community gathering point and shows GitHub it's an active repo.

---

## Step 5: Add a GitHub Release

1. Go to **Releases → Create a new release**
2. Set the tag to `v1.0.0`
3. Title: `v1.0.0 — Initial Release: Full MBB Consulting Skill`
4. Description:
```
First public release of the MBB Management Consultant Skill for Claude.

**Includes:**
- Full skill definition (SKILL.md) with 80+ reference files
- Complete consulting frameworks reference (FRAMEWORKS.md)
- 3 worked case studies with full solutions (CASE-STUDIES.md)
- Step-by-step installation guide (INSTALL.md)

**Covers:**
- 9 industry verticals (Healthcare, Financial Services, Energy, TMT, Consumer, Industrial, Public Sector, Real Estate, Hospitality)
- 11 specialist methodologies (Due Diligence, PMI, GenAI Strategy, Pricing, Corporate Restructuring, etc.)
- Complete case interview coaching (McKinsey, Bain, BCG formats)
- Full consulting toolkit (frameworks, communication, deliverables, career)

Built to democratize MBB-caliber thinking. Free forever. MIT License.
```

---

## Step 6: Promote for Maximum Discovery

### LinkedIn Post (Copy & Adapt)
```
I just open-sourced a complete MBB management consultant AI skill for Claude — free, MIT licensed.

It turns Claude into a McKinsey/Bain/BCG-level consultant with:
→ 80+ deep-knowledge reference files
→ 9 industry verticals (Healthcare, FinServ, TMT, Consumer, Energy...)
→ Complete case interview coaching (all formats)
→ Every consulting framework you've ever heard of, actually explained well
→ Worked case studies with full solutions

Built for:
🎓 MBA students and case interview candidates
💼 Consultants who want to work 10x faster with AI
📊 Business professionals who want structured thinking
🚀 Anyone Claude has saved from a $500/hour consultant bill

[Link to GitHub repo]

Spread the light. Knowledge should be free.

#management-consulting #MBA #McKinsey #Bain #BCG #AI #Claude #caseinterview
```

### Post in These Communities
- **Reddit**: r/consulting, r/MBA, r/mba, r/caseinterview, r/ChatGPT, r/ClaudeAI
- **LinkedIn**: Tag #consulting #MBA #caseinterview #McKinsey
- **Hacker News**: Submit with title "Show HN: Open-source MBB consulting skill for Claude"
- **Product Hunt**: Launch as "MBB Management Consultant AI Skill"
- **Twitter/X**: Tag @AnthropicAI, use #ClaudeAI, #consulting, #MBA

### For Case Interview Communities
- PrepLounge
- Management Consulted Forum
- Poets & Quants (MBA forums)
- Blind (consulting track)
- Wall Street Oasis

---

## Step 7: SEO Optimization Checklist

✅ Repository name contains keywords (mbb, management-consultant, claude, skill)
✅ Description is keyword-rich (McKinsey, Bain, BCG, MBA, case interview, consulting frameworks)
✅ README uses all target keywords naturally in context
✅ Topics/tags are set (20 relevant tags)
✅ At least one Release created (signals active project)
✅ Issues enabled and first issue pinned
✅ License set (MIT — signals open-source credibility)
✅ GitHub Pages enabled (doubles indexed surface area)

---

## Expected Discovery Timeline

| Timeframe | What Happens |
|-----------|-------------|
| Day 1 | GitHub indexes the repo; shows in GitHub search for key terms |
| Day 3-7 | Google crawls and indexes the repo |
| Week 2-4 | AI search systems (Perplexity, Claude, ChatGPT browsing) discover it |
| Month 1-3 | Organic backlinks from community posts drive ranking |
| Month 3-6 | Appearing in top results for "consulting frameworks Claude", "case interview AI", "McKinsey skill Claude" |

---

*The knowledge exists. Now let it travel.*
