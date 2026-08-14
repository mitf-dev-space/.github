# Quarterly Access Review — MITF Dev Space

Run this checklist every quarter (or after major onboarding/offboarding). GitHub Free does not provide automated access reviews; this manual process closes that gap.

## 1. Organization owners

- [ ] Confirm only required people are **Owners** (currently: `anstwechy`, `JihadEjdaydhom`, `rashadshayoup` when joined)
- [ ] Remove owner role from anyone who no longer needs org-wide admin access
- [ ] Settings: https://github.com/orgs/mitf-dev-space/people

## 2. Team membership

| Team | Purpose | Review |
|------|---------|--------|
| `engineering-leads` | Cross-platform write + CODEOWNERS | Leads only |
| `backend` | API / services | Active backend engineers |
| `web` | Front-end / admin portals | Active web engineers |
| `mobile` | Flutter / mobile | Active mobile engineers |
| `devops` | Compose, infra, deploy paths | Active DevOps |
| `platform` | Full-stack platform repos | Platform squad |

- [ ] Remove departed members from all teams
- [ ] Settings: https://github.com/orgs/mitf-dev-space/teams

## 3. Outside collaborators

After migration, some users may still be **outside collaborators** on individual repos instead of org members.

- [ ] List collaborators per repo: **Repository → Settings → Collaborators**
- [ ] Prefer org membership + team access over per-repo collaborators
- [ ] Remove access for anyone who left the company

## 4. Deploy keys and webhooks

- [ ] Audit deploy keys: **Repository → Settings → Deploy keys**
- [ ] Audit webhooks: **Repository → Settings → Webhooks**
- [ ] Remove unused or unknown integrations

## 5. Actions secrets and variables

- [ ] Rotate `DOCKERHUB_TOKEN` if exposed or staff changed
- [ ] Confirm org-level vs repo-level secret policy (see [ACTIONS_SECRETS_RUNBOOK.md](./ACTIONS_SECRETS_RUNBOOK.md))
- [ ] Remove secrets for decommissioned environments

## 6. Public repository exposure

Public repos (`dev-office-assistance`, `compose-omnitest-studio`, `mitf_*_public_docs`):

- [ ] Secret scanning + push protection enabled
- [ ] Dependabot security updates enabled
- [ ] No internal hostnames, API keys, or private registry URLs in README or workflows

## 7. Pending items (when ready)

- [ ] Enable **Require 2FA** for all org members (after everyone enrolls)
- [ ] Manual UI: block members deleting repos / changing visibility
- [ ] Migrate `wallet-services` when team is ready
- [ ] Resolve stuck compose repo transfers

## Sign-off

| Quarter | Reviewer | Date | Notes |
|---------|----------|------|-------|
| Q3 2026 | | | Initial org setup |
