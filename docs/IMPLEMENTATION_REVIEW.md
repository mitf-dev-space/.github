# MITF Dev Space — implementation review (2026-08-14)

This document summarizes the health check performed on org setup, profile README, workflows, and migration artifacts.

## Org profile README (fixed)

**Root cause:** GitHub only renders `profile/README.md` from `org/.github` when that repository is **public**. The repo was private, so the org home showed the default placeholder: *"You can create a README file or pin repository visible to anyone."*

**Fix applied:**
- Made `mitf-dev-space/.github` **public**
- Pinned six repositories on the org profile (`.github`, public docs, `dev-office-assistance`, `mitf-platform-template`)
- Removed workflows inappropriate for a docs-only repo (`codeql.yml`, `ghcr-publish.yml`)

**Verify:** https://github.com/mitf-dev-space — custom README and logo should appear for anonymous visitors.

## Workflows on `.github`

| Workflow | Status | Notes |
|----------|--------|-------|
| `platform-health-auto-add.yml` | Active | Adds issues/PRs with `platform-health` label to Project #2. Requires **Settings → Actions → General → Workflow permissions → Access to organization projects** on this repo. |
| `dependency-review.yml` | Active | Runs on PRs only; appropriate for docs repo. |
| ~~`codeql.yml`~~ | Removed | No application source; caused failing matrix builds. |
| ~~`ghcr-publish.yml`~~ | Removed | No Dockerfile; spurious failure on push. |

## Platform repos (spot check)

CodeQL and dependency-review remain on application repositories transferred to the org. Run `gh run list -R mitf-dev-space/<repo> --limit 3` per repo if you need a full matrix.

## Security notes (manual follow-up)

| Item | Status |
|------|--------|
| Org default permission = None | Done |
| Block members from deleting repos | Done |
| Block members from changing repo visibility | **UI:** Org Settings → Member privileges |
| 2FA required for org | **Pending** |
| Org secret `DOCKERHUB_TOKEN` | Not set (GHCR workflows use `GITHUB_TOKEN` where configured) |
| `.github` public | **Done** — contains governance docs only; no secrets. Internal GitLab hostnames appear in migration docs (same as shared sheet). |

## Migration & project tracking

- Master tracker: [issue #17](https://github.com/mitf-dev-space/.github/issues/17)
- Platform Health project: https://github.com/orgs/mitf-dev-space/projects/2
- Sunday pilot: `webpages-v2` per `docs/SUNDAY_MIGRATION_RUNBOOK.md`

## Deferred (do not change without explicit request)

- `wallet-services` migration
- `mitf-support` CI fixes
- Personal `compose-*` transfers (Track A in Sunday runbook)
- `MW-Development-Team` org
