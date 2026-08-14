# GitLab migration runbook (per repository)

Use this checklist for **each** repo migrated from `http://10.10.20.51` to `mitf-dev-space`.

**Plan:** [GITLAB_TO_GITHUB_MIGRATION_PLAN.md](./GITLAB_TO_GITHUB_MIGRATION_PLAN.md)  
**Naming:** [NAMING_AND_BRANCH_STANDARDS.md](./NAMING_AND_BRANCH_STANDARDS.md)  
**Inventory:** [GITLAB_REPO_INVENTORY.md](./GITLAB_REPO_INVENTORY.md)

---

## Variables (fill per repo)

```text
GITLAB_URL=http://10.10.20.51/<group>/<project>
GITHUB_NAME=mitf-example-service
PLATFORM_DOMAIN=gateways          # from inventory
WAVE=3
```

---

## Phase 1 — Prepare (5 min)

- [ ] Confirm repo row in [inventory](./GITLAB_REPO_INVENTORY.md)
- [ ] Confirm proposed `GITHUB_NAME` (kebab-case, `mitf-` prefix)
- [ ] Check if **platform merge** applies later (note in migration log)
- [ ] Create GitHub issue: `[Migration] GITLAB_NAME → GITHUB_NAME`
- [ ] Add issue to [Platform Health project](https://github.com/orgs/mitf-dev-space/projects/2)

---

## Phase 2 — Mirror git history (company network)

```powershell
$GITLAB_URL = "http://10.10.20.51/front-end/web/webpages-v2.git"
$GITHUB_NAME = "webpages-v2"
$ORG = "mitf-dev-space"

# Clone mirror from GitLab (use token or SSH as configured)
git clone --mirror $GITLAB_URL gitlab-mirror.git
cd gitlab-mirror.git

# Create empty GitHub repo
gh repo create "$ORG/$GITHUB_NAME" --private --description "Migrated from GitLab: $GITLAB_URL"

# Push all refs
git push --mirror "https://github.com/$ORG/$GITHUB_NAME.git"
cd ..
```

- [ ] All branches and tags visible on GitHub
- [ ] No secrets in repo history (`git log -p` spot-check; use `gitleaks` if available)

---

## Phase 3 — Normalize branches

```powershell
$ORG = "mitf-dev-space"
$REPO = "webpages-v2"
cd $REPO
git fetch origin

# Rename default branch to main if needed
$default = git remote show origin | Select-String "HEAD branch" | ForEach-Object { ($_ -split ": ")[1].Trim() }
if ($default -ne "main") {
  git branch -m $default main
  git push -u origin main
  gh api repos/$ORG/$REPO -X PATCH -f default_branch=main
}

# Normalize integration branch → develop
foreach ($legacy in @("development", "develop", "Development")) {
  if (git show-ref --verify --quiet "refs/heads/$legacy") {
    git branch -m $legacy develop
    git push origin develop
    git push origin --delete $legacy
    break
  }
}
# If no develop branch, create from main
if (-not (git show-ref --verify --quiet refs/heads/develop)) {
  git checkout -b develop origin/main
  git push -u origin develop
}
```

- [ ] Default branch is `main`
- [ ] `develop` exists for integration
- [ ] Document renames in repo `README.md` Migration section

---

## Phase 4 — CI/CD (GitHub Actions)

### If `.gitlab-ci.yml` exists

```powershell
# Optional: convert with GitHub Actions Importer (needs GitLab + GitHub tokens)
gh actions-importer dry-run gitlab --output-dir ./actions-output `
  --source-url $GITLAB_URL --target-url "https://github.com/$ORG/$GITHUB_NAME"
```

Review output; commit workflows via PR.

### If no CI (most repos in sheet)

Copy standard workflows from org template:

```powershell
gh repo clone mitf-dev-space/mitf-platform-template /tmp/template
cp -r /tmp/template/.github/workflows/* .github/workflows/
# Edit: project paths, dotnet version, docker image name
```

Minimum workflows:

- [ ] `ci.yml` — build + test (stack-appropriate)
- [ ] `codeql.yml` — from org `.github`
- [ ] `dependency-review.yml` — on PRs

- [ ] Secrets documented in [ACTIONS_SECRETS_RUNBOOK.md](./ACTIONS_SECRETS_RUNBOOK.md)
- [ ] First Actions run **green** on `main`

---

## Phase 5 — Org standards

```powershell
$ORG = "mitf-dev-space"
$REPO = "webpages-v2"

# Teams (adjust layer: web → web team, mobile → mobile, else backend)
gh api orgs/$ORG/teams/engineering-leads/repos/$ORG/$REPO -X PUT -f permission=push
gh api orgs/$ORG/teams/backend/repos/$ORG/$REPO -X PUT -f permission=push
gh api orgs/$ORG/teams/platform/repos/$ORG/$REPO -X PUT -f permission=push
# gh api orgs/$ORG/teams/web/repos/$ORG/$REPO -X PUT -f permission=push

# Merge settings
gh api repos/$ORG/$REPO -X PATCH `
  -f allow_squash_merge=true `
  -f allow_merge_commit=false `
  -f allow_rebase_merge=false `
  -f delete_branch_on_merge=true

# Topics
gh repo edit $ORG/$REPO --add-topic mitf --add-topic platform --add-topic web
```

Files to add (copy from `mitf-platform-template` or `mitf-support`):

- [ ] `.github/CODEOWNERS`
- [ ] `.github/pull_request_template.md`
- [ ] `SECURITY.md`
- [ ] Standard labels (script in org tooling or `gh label create`)

- [ ] Row added to [platform catalog](../profile/README.md) if net-new platform

---

## Phase 6 — Cutover

- [ ] Announce in team channel: new canonical URL
- [ ] Archive GitLab project (Maintainer → Archive) or add README redirect
- [ ] Update Google Sheet column: **GitHub URL**
- [ ] Close migration GitHub issue
- [ ] Mark **Done** on Platform Health board

---

## Phase 7 — Post-migration (optional, later)

- [ ] Merge into platform monolith if mapped in migration plan
- [ ] Remove duplicate CI secrets
- [ ] Add to compose / deploy manifests in org

---

## Sunday pilot suggestion

| Order | GitLab repo | GitHub name | Why |
|-------|-------------|-------------|-----|
| 1 | `webpages-v2` | `webpages-v2` | Pipeline + tests in sheet |
| 2 | `mitf-office` | `mitf-office-gitlab` or merge into existing `mitf-office` web | Coordinate with existing org repo |

After pilot, proceed with [wave order](./GITLAB_TO_GITHUB_MIGRATION_PLAN.md#domain-grouping-migration-waves).

---

## Troubleshooting

| Problem | Fix |
|---------|-----|
| Cannot reach `10.10.20.51` | VPN / company network only |
| Push rejected (large file) | Git LFS migrate or BFG before push |
| `master` protected on GitHub | Change default branch in settings first |
| GitLab CI uses internal runners | Rewrite `runs-on`; use self-hosted runner label if needed |
| Duplicate repo name in org | Suffix `-service` or merge into platform |
