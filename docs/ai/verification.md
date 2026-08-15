# MITF Dev Space `.github` — Cloud Agent Verification

Audit date: 2026-08-15  
Repository: `mitf-dev-space/.github` (public org governance)

## Purpose

Organization profile, governance docs, issue templates, and reusable GitHub Actions workflow templates. **No application source code.**

## Branches

| Branch | Role |
|--------|------|
| `main` | Default; org profile README at `profile/README.md` |

No `develop` or release branch.

## Runtimes

None. Markdown and YAML only.

## Manifest inventory

| Artifact | Path |
|----------|------|
| Org profile README | `profile/README.md` |
| Logo assets | `profile/logo.svg`, `profile/logo-512.png` |
| Governance docs | `docs/`, `CONTRIBUTING.md`, `SECURITY.md` |
| Workflow templates | `.github/workflows/` (`dependency-review.yml`, `oidc-aws-deploy.yml`, `platform-health-auto-add.yml`) |

No `*.sln`, `package.json`, `pyproject.toml`, `requirements.txt`, `Dockerfile`, or `docker-compose*`.

## Docker / Compose

None.

## Verified safe commands (2026-08-15)

| Command | Result |
|---------|--------|
| `git status` | **PASS** — clean working tree expected |
| Review Markdown/YAML locally | **PASS** — no compile step |

There is **no build, test, or lint** step for this repository.

## Restore / build / test / lint / run locally

| Task | Command | Verified |
|------|---------|----------|
| Restore deps | N/A | — |
| Build | N/A | — |
| Unit tests | N/A | — |
| Integration tests | N/A | — |
| Frontend tests | N/A | — |
| Lint / typecheck | N/A | — |
| Start application | N/A | — |

## Required services / databases / mocks

None.

## Safe commands (disposable dev environment)

- Read and edit Markdown/YAML
- `git status`, `git diff`
- Open PRs (triggers `dependency-review` on PRs only)

## Unsafe / external commands

| Command | Risk |
|---------|------|
| `oidc-aws-deploy.yml` (manual dispatch) | Deploys to AWS when configured with real OIDC role |
| `platform-health-auto-add.yml` | Writes to GitHub Project #2 (org project) |

## CI reference

| Workflow | Trigger | Notes |
|----------|---------|-------|
| `dependency-review.yml` | PR | Dependency review only |
| `platform-health-auto-add.yml` | Issues/PRs | Adds items to Platform Health project |
| `oidc-aws-deploy.yml` | `workflow_dispatch` | Template only |

## Notes for Cloud Agents

- Do **not** add application code here; keep governance and org profile only.
- Org profile README requires this repo to stay **public**.
- Internal migration runbooks in `docs/` may reference private infrastructure; do not copy secrets into public issues.
