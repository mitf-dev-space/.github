# Actions Secrets & Variables Runbook

Secrets must be re-created after repository transfer from a personal account to the organization. GitHub does **not** copy secrets across owners.

## Organization policy

- `GITHUB_TOKEN` default: **read-only** at org level (workflows must request elevated permissions explicitly)
- Actions allowed: **GitHub-owned + verified** actions only (reduces supply-chain risk)

## Per-repository requirements

### mitf-support

| Name | Type | Required by | Notes |
|------|------|-------------|-------|
| `DOCKERHUB_TOKEN` | Secret | Docker Hub workflow | Docker Hub access token |
| `DOCKERHUB_USERNAME` | Variable | Docker Hub workflow | Defaults to personal Docker Hub user if unset |
| `SUPPORT_AI_EVAL_BASE_URL` | Variable | AI Eval (scheduled) | Deployed eval API base URL — **missing causes AI Eval failures** |

### dev-office-assistance (public)

| Name | Type | Required by | Notes |
|------|------|-------------|-------|
| `DOCKERHUB_TOKEN` | Secret | Docker Hub workflow | Required for image push |
| `DOCKERHUB_USERNAME` | Variable | Docker Hub workflow | Optional fallback username |

## How to add secrets (owners)

```bash
# Repository secret
gh secret set DOCKERHUB_TOKEN --repo mitf-dev-space/mitf-support --body "YOUR_TOKEN"

# Repository variable
gh variable set SUPPORT_AI_EVAL_BASE_URL --repo mitf-dev-space/mitf-support --body "https://your-eval-api.example.com"
```

Or: **Repository → Settings → Secrets and variables → Actions**

## Org-level secrets (optional, recommended)

For shared Docker Hub credentials across platforms, create **organization secrets** with repository access policies:

**Organization → Settings → Secrets and variables → Actions → New organization secret**

This avoids duplicating `DOCKERHUB_TOKEN` in every platform repo.

## Verification

```bash
gh secret list --repo mitf-dev-space/mitf-support
gh variable list --repo mitf-dev-space/mitf-support
gh run list --repo mitf-dev-space/mitf-support --limit 5
```
