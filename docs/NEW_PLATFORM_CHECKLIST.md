# New Platform Repository Checklist

Use this when adding a new MITF full-stack platform to `mitf-dev-space`.

## Before creating the repo

- [ ] Name follows convention: `mitf-<domain>` or existing product name (kebab-case preferred)
- [ ] Repo is **private** unless explicitly approved for public docs
- [ ] Platform listed in [profile/README.md](../profile/README.md) catalog

## Repository setup

- [ ] Create under `mitf-dev-space` (not personal account)
- [ ] Add description (one line: what the platform does)
- [ ] Add topics: `mitf`, `platform`, stack tags (`csharp`, `typescript`, `flutter`, etc.)
- [ ] Enable Dependabot alerts (on by default for new org repos)

## Access (teams)

Apply **Write** to:

- `engineering-leads`
- `backend`
- `platform` (or `web` / `mobile` if domain-specific)

```bash
gh api repos/mitf-dev-space/NEW_REPO/teams/backend -X PUT -f permission=push
gh api repos/mitf-dev-space/NEW_REPO/teams/platform -X PUT -f permission=push
gh api repos/mitf-dev-space/NEW_REPO/teams/engineering-leads -X PUT -f permission=push
```

## Standard files

Copy from an existing platform (e.g. `mitf-support`):

- [ ] `.github/CODEOWNERS` — adjust paths for repo layout
- [ ] `.github/pull_request_template.md` (from org `.github` repo)
- [ ] `SECURITY.md` or link to org policy
- [ ] Standard labels: `platform`, `bug`, `enhancement`, `security`, `devops`, `triage`, `blocked`

## CI/CD

- [ ] Workflows use `permissions:` explicitly (org default `GITHUB_TOKEN` is read-only)
- [ ] Secrets documented in [ACTIONS_SECRETS_RUNBOOK.md](./ACTIONS_SECRETS_RUNBOOK.md)
- [ ] Prefer **OIDC** over long-lived cloud/registry tokens where possible
- [ ] Docker images: org-level `DOCKERHUB_TOKEN` or GHCR under `ghcr.io/mitf-dev-space/`

## Merge settings (recommended)

- [ ] Allow squash merge (default)
- [ ] **Delete branch on merge** enabled
- [ ] Default branch: `main`

## After first deploy

- [ ] Add platform row to org profile catalog
- [ ] Notify `#engineering` (or internal channel) with repo link and team access
