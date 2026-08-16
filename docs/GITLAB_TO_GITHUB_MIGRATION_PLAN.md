# GitLab → GitHub migration plan

**Status:** Planned — execution starts Sunday (company network)  
**Source:** [Repo It DEP 01 sheet](https://docs.google.com/spreadsheets/d/125Hl9a5Rp1VjkzXGDisWniaW02ID2Jo4jpS_GjZrU8Y/edit)  
**Target:** [mitf-dev-space](https://github.com/mitf-dev-space) (GitHub Free)  
**Inventory:** [GITLAB_REPO_INVENTORY.md](./GITLAB_REPO_INVENTORY.md) (67 repos)

---

## Goals

1. Leave unreliable GitLab (`10.10.20.51`) for company-owned GitHub
2. Migrate **one repo at a time** with clean history, branches, and CI
3. One **naming**, **branch**, and **policy** standard across all repos
4. Convert GitLab CI → GitHub Actions (minimal, maintainable workflows)
5. Map GitLab groups to MITF **platform** groupings where it reduces sprawl

**Out of scope for this plan:** `MW-Development-Team` org, personal repos (`tw-os`, `masarat-portfolio`), `wallet-services` until team confirms.

---

## Two migration tracks

| Track | Source | Count | Sunday priority |
|-------|--------|-------|-----------------|
| **A** | `anstwechy/*` GitHub transfers | 6 compose + wallet (later) | After GitLab pilot |
| **B** | GitLab `10.10.20.51` | 67 repos | **Primary** |

This document covers **Track B**. Track A: [SUNDAY_MIGRATION_RUNBOOK.md](./SUNDAY_MIGRATION_RUNBOOK.md).

---

## Strategy: mirror first, consolidate later

GitLab today has **many small service repos**. GitHub org already has **platform monoliths**. Do not big-bang merge on day one.

| Mode | When | Result |
|------|------|--------|
| **Mirror** | Default for Sunday | 1 GitLab repo → 1 new `mitf-dev-space/<name>` repo |
| **Platform link** | Repo already exists in org | Import into existing platform repo as subdirectory in a follow-up PR |
| **Archive GitLab** | After smoke test on GitHub | Mark GitLab read-only; document redirect in README |

Consolidation (e.g. 4 voucher backends → `voucher-provider-workspace`) is **Phase 2** after mirrors are stable.

---

## Domain grouping (migration waves)

Migrate in waves — smallest, best-documented repos first.

| Wave | Domain | Repos | Rationale |
|------|--------|-------|-----------|
| **0 — Pilot** | `web` | 4 | Sheet shows pipelines + tests on `webpages-v2` |
| **1** | `core-services`, `reporting`, `providers` | 4 | Small, shared infrastructure |
| **2** | `office`, `voucher` | 6 | Aligns with existing org platforms |
| **3** | `gateways` | 8 | Payment/notification entry points |
| **4** | `transactions` | 8 | High coupling — migrate as a batch week |
| **5** | `backend-other` | 17 | Miscellaneous — review each for platform mapping |
| **M1–M4** | **mobile** (package-first) | **24** | **Priority track** — [MOBILE_MIGRATION_PLAN.md](./MOBILE_MIGRATION_PLAN.md) |

**Sunday target:** Complete **M1** foundation packages + validate `flutter pub get` from GitHub git URLs. Parallel: Wave 0 web pilot.

## Platform mapping (GitLab → existing GitHub)

Use when deciding mirror name vs future merge target.

| GitHub platform (exists) | GitLab repos to associate |
|--------------------------|---------------------------|
| `voucher-provider-workspace` | `voucher.external`, `voucher.internal`, `voucher.management`, `Voucher.PurchaseOrchestrator` |
| `mitf-online-payment` | `Mitf.OnlinePayment`, payment mobile cores |
| `dev-office-assistance` | `Mitf.Office.*`, office web (coordinate with `mitf-office`) |
| `mitf_notification_system` | `SMSChannel`, `Mitf.Whatsapp.Gateway`, `SIBSmsGateway`, `MobileChannel` |
| `mitf-payment-ecosystem` | `Mitf.*Adapter`, `Mitf.OnePay*`, transaction hubs |
| `mitf-aml-system` | (none in sheet — already in org) |
| `insurance-provider-hub` | Review `backend-other` during wave 5 |
| **New mirror** | Anything without a clear platform home |

---

## CI/CD migration approach

GitLab sheet: almost all repos **no pipeline** / **no unit tests**. Treat CI as **greenfield** using org templates, not literal `.gitlab-ci.yml` translation.

### Recommended path

1. **Audit** (optional): `gh actions-importer audit --source gitlab` with GitLab token ([GitHub docs](https://docs.github.com/en/actions/tutorials/migrate-to-github-actions/automated-migrations/gitlab-migration))
2. **Dry-run** per repo if `.gitlab-ci.yml` exists
3. **Default workflow** for repos with no CI:
   - Copy from `mitf-platform-template` or `.github` org workflows
   - Minimum: `ci.yml` (build + test), `codeql.yml`, `dependency-review.yml`
4. **Secrets:** GitLab CI variables → GitHub Actions secrets ([ACTIONS_SECRETS_RUNBOOK.md](./ACTIONS_SECRETS_RUNBOOK.md))
5. **Runners:** GitLab tags → `runs-on: ubuntu-latest` (or self-hosted `runs-on: [self-hosted, linux]` when on company network)

### Workflow standards

- Explicit `permissions:` on every workflow (org default token is read-only)
- No long-lived credentials in YAML — use secrets or OIDC ([OIDC_AND_SUPPLY_CHAIN.md](./OIDC_AND_SUPPLY_CHAIN.md))
- Publish images to `ghcr.io/mitf-dev-space/<repo>` by default
- Docker Hub only when `DOCKERHUB_TOKEN` is set at org level

---

## Policies (apply to every migrated repo)

From [NAMING_AND_BRANCH_STANDARDS.md](./NAMING_AND_BRANCH_STANDARDS.md):

- [ ] Default branch `main`
- [ ] Integration branch `develop` (create if missing)
- [ ] Squash merge + delete branch on merge
- [ ] Topics + description
- [ ] Team access: `engineering-leads`, `backend`/`web`/`mobile`, `platform`
- [ ] `SECURITY.md`, `CODEOWNERS`, PR template
- [ ] Standard labels
- [ ] Dependabot + CodeQL + dependency-review enabled
- [ ] Org ruleset: require PR to `main` (and `develop` when CI exists)

---

## Prerequisites (before Sunday)

| Item | Owner | Notes |
|------|-------|-------|
| Company VPN / domain access to `10.10.20.51` | You | Required for `git clone` |
| GitLab read token or SSH key | DevOps | `read_repository` scope |
| GitHub org Owner | You / Jihad | Create repos, set teams |
| Sheet kept updated | Team lead | [Inventory](./GITLAB_REPO_INVENTORY.md) regenerated after changes |
| Pilot repo chosen | Recommend `webpages-v2` | Has pipeline in sheet |

---

## Success criteria (per repo)

- [ ] All branches pushed; `main` is default
- [ ] Legacy branch names documented in README if renamed
- [ ] At least one green Actions run on `main`
- [ ] Team permissions applied
- [ ] Row updated on Platform Health project
- [ ] GitLab repo marked archived / README points to GitHub

---

## Timeline (suggested)

| Week | Focus |
|------|-------|
| **Sun week 1** | Pilot Wave 0 (web), tooling, naming validation |
| **Week 2** | Waves 1–2 (core, office, voucher) |
| **Week 3** | Waves 3–4 (gateways, transactions) |
| **Week 4+** | Waves 5–7 (backend-other, mobile) + platform consolidation |

Adjust pace to team capacity — **quality over speed**.

---

## Related docs

- [GITLAB_MIGRATION_RUNBOOK.md](./GITLAB_MIGRATION_RUNBOOK.md) — step-by-step per repo
- [GITLAB_REPO_INVENTORY.md](./GITLAB_REPO_INVENTORY.md) — full 67-repo list
- [NAMING_AND_BRANCH_STANDARDS.md](./NAMING_AND_BRANCH_STANDARDS.md)
- [NEW_PLATFORM_CHECKLIST.md](./NEW_PLATFORM_CHECKLIST.md)
- [SUNDAY_MIGRATION_RUNBOOK.md](./SUNDAY_MIGRATION_RUNBOOK.md) — Track A (personal GitHub)
