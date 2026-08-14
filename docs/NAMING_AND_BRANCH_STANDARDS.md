# MITF naming and branch standards

Single standard for all repositories in `mitf-dev-space`, including repos migrated from GitLab (`10.10.20.51`).

---

## Repository naming

### Rules

| Rule | Example |
|------|---------|
| Lowercase only | `mitf-online-payment` not `Mitf.OnlinePayment` |
| Kebab-case (`-`) | `mitf-bank-adapter` not `mitf_bank_adapter` |
| Prefix `mitf-` for company services | `mitf-system-core` |
| Exception: existing product names already in org | `mitf_notification_system`, `voucher-provider-workspace` — keep until rename window |
| Max length 100 characters | GitHub limit |
| No `.git` suffix in repo name | — |
| Private by default | Public only for approved docs |

### GitLab → GitHub name mapping

| GitLab pattern | GitHub target |
|----------------|---------------|
| `Mitf.OnlinePayment` | `mitf-online-payment` |
| `Core Mobile Banking` | `core-mobile-banking` |
| `Mitt.SystemCore` | `mitt-systemcore` or merge into platform repo |
| White-label bank app `Siraj Mobile` | `siraj-mobile` (group under `banking-mobile` topic) |

Full mapping: [GITLAB_REPO_INVENTORY.md](./GITLAB_REPO_INVENTORY.md)

### Topics (required on every repo)

```
mitf, platform|<layer>, <stack>
```

Examples: `mitf`, `backend`, `csharp` or `mitf`, `mobile`, `flutter`, `banking`

---

## Branch naming

### Long-lived branches (every repo)

| Branch | Purpose | Replaces (GitLab legacy) |
|--------|---------|--------------------------|
| `main` | Production-ready, protected | `master`, `Main`, `main` |
| `develop` | Integration / next release | `development`, `develop`, `develop ` (trim spaces) |

**Migration rule:** On import, rename default branch to `main`. Create or rename integration branch to `develop`. Delete stale `master`/`development` after team confirms.

### Short-lived branches (features)

```
<type>/<ticket>-<short-description>
```

| Type | Use |
|------|-----|
| `feature/` | New capability |
| `fix/` | Bug fix |
| `hotfix/` | Production urgent fix |
| `chore/` | Tooling, deps, CI only |
| `release/` | Release prep (`release/1.4.0`) |

Examples:

- `feature/MITF-142-add-sms-retry`
- `fix/MITF-89-login-timeout`
- `hotfix/MITF-201-payment-gateway`

Rules:

- Lowercase, hyphens only (no spaces, underscores, Arabic in branch names)
- Optional ticket ID from GitHub Issues (`MITF-###`) or internal tracker
- Max ~60 characters

### What we do **not** use

- Per-bank long-lived branches on shared repos (sheet notes “each bank has dev branch” for `Mitf.BankBackOffice.API`) — use **feature flags**, config, or separate deploy targets instead
- Unprefixed branches like `jihad-fix` (use `fix/` prefix)

---

## Commit messages

[Conventional Commits](https://www.conventionalcommits.org/) — already org policy:

```
feat: add OTP retry for SMS gateway
fix: correct settlement date in OnePay adapter
chore: migrate GitLab CI to GitHub Actions
docs: update deployment runbook
```

Reference GitHub issues: `fix: handoff timeout (#42)`

---

## Tags and releases

- Annotated tags: `v1.2.3` (semver)
- GitHub Releases for production deploys
- Pre-release: `v1.2.3-rc.1`

---

## Directory layout (platform repos)

Prefer **one platform repo** (backend + web + mobile + infra) over many micro-repos. When migrating GitLab services that belong to an existing platform, plan merge into:

| Existing GitHub platform | Absorb GitLab groups |
|--------------------------|----------------------|
| `voucher-provider-workspace` | `voucher.*` backends |
| `mitf-online-payment` | payment gateways + payment mobile cores |
| `dev-office-assistance` / `mitf-office` (web) | office backends + `mitf-office` web |
| `mitf_notification_system` | SMS/WhatsApp gateways |
| `mitf-payment-ecosystem` | transactions/* adapters |

See [GITLAB_TO_GITHUB_MIGRATION_PLAN.md](./GITLAB_TO_GITHUB_MIGRATION_PLAN.md) for merge vs mirror decisions.

---

## Enforcement

| Control | GitHub Free |
|---------|-------------|
| Default branch `main` | Repo setting |
| Delete branch on merge | Repo setting |
| Squash merge preferred | Repo setting |
| Branch protection (require PR) | **Rulesets** — org ruleset on `main` + `develop` |
| CODEOWNERS | File in repo (review routing; no block on private Free) |
| Required status checks | Ruleset when CI exists |

Apply via [GITLAB_MIGRATION_RUNBOOK.md](./GITLAB_MIGRATION_RUNBOOK.md) step 8 on every migrated repo.
