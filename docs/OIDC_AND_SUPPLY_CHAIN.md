# OIDC & Supply Chain Hardening (MITF Dev Space)

Grounded in [GitHub security features](https://docs.github.com/en/code-security/getting-started/github-security-features) and [OIDC for Actions](https://docs.github.com/en/actions/deployment/security-hardening-your-deployments/about-security-hardening-with-openid-connect).

## Already applied

| Control | Status |
|---------|--------|
| Org default repo permission: None | Enabled |
| `GITHUB_TOKEN` default read-only | Enabled |
| Actions: GitHub-owned + verified only | Enabled |
| Dependabot alerts for new repos | Enabled |
| Secret scanning (public repos) | Enabled where applicable |
| CODEOWNERS (documentation) | 15+ platform repos |

## Recommended next steps (no extra GitHub cost)

### 1. Replace long-lived registry secrets with OIDC

Today several workflows use `DOCKERHUB_TOKEN`. Long-term, prefer:

- **GitHub Container Registry (GHCR)** — `ghcr.io/mitf-dev-space/<image>` with `GITHUB_TOKEN` or OIDC
- **AWS ECR / Azure ACR** — OIDC federation from Actions (no static AWS keys in secrets)

Example Actions OIDC pattern (AWS):

```yaml
permissions:
  id-token: write
  contents: read

steps:
  - uses: aws-actions/configure-aws-credentials@v4
    with:
      role-to-assume: arn:aws:iam::ACCOUNT:role/github-mitf-deploy
      aws-region: eu-central-1
```

### 2. Pin third-party Actions to commit SHAs

Verified actions are allowed, but pinning to full SHAs reduces tag-moving supply-chain risk:

```yaml
# Instead of: uses: actions/checkout@v4
uses: actions/checkout@11bd71901bbe5b1630ceea73d27597364b9f6c2b # v4.2.2
```

Prioritize workflows that run on `pull_request` from forks and release pipelines.

### 3. Code scanning on public repos (free)

For `dev-office-assistance` and public doc repos, enable **CodeQL** via default workflow:

**Security → Code scanning → Set up → Default**

Private repos require GitHub Code Security (paid).

### 4. Dependency review on PRs

Add to platform repos with heavy npm/nuget usage:

```yaml
- uses: actions/dependency-review-action@v4
```

Shows vulnerable dependency changes before merge (works on private repos with dependency graph).

### 5. Organization audit log

Free orgs have limited audit log retention. Export periodically:

**Organization → Settings → Audit log → Export**

Store exports for compliance and incident response.

## Paid upgrades (when budget allows)

| Feature | Plan | Benefit |
|---------|------|---------|
| Branch protection enforcement (private) | GitHub Team ($4/user/mo) | Required reviews, status checks |
| CODEOWNERS enforcement | Team + Secret Protection | Block merges without owner approval |
| Secret scanning on private repos | Secret Protection (~$19/active committer/mo) | Catch leaked tokens in private code |
| SAML SSO | Enterprise | Central identity for offboarding |

## 2FA requirement

Before enabling **Require 2FA for all members**:

1. Announce deadline to all members
2. Confirm each member enrolled at https://github.com/settings/security
3. Enable: https://github.com/organizations/mitf-dev-space/settings/security

Members without 2FA are removed from the org when enforcement kicks in.
