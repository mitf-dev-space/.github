# Mobile migration runbook (per repository)

Use with [MOBILE_MIGRATION_PLAN.md](./MOBILE_MIGRATION_PLAN.md). Generic steps: [GITLAB_MIGRATION_RUNBOOK.md](./GITLAB_MIGRATION_RUNBOOK.md).

---

## Variables (fill per repo)

```text
GITLAB_URL=http://10.10.20.51/front-end/payment/payment-core.git
GITHUB_NAME=mitf-payment-core
MIGRATION_WAVE=M1
LAYER=mobile-package          # mobile-package | mobile
DOMAIN=payment-mobile         # payment-mobile | banking-mobile
```

---

## Phase 0 — Pre-flight (10 min)

- [ ] Row exists in [mobile-repos-corrected.csv](./data/sheet-import/mobile-repos-corrected.csv)
- [ ] **M1 packages migrated** before migrating apps that depend on them
- [ ] Export GitLab CI/CD variables → `secrets/gitlab-<repo>-variables.txt` (secure storage; **do not commit**)
- [ ] Inventory Android keystore + iOS signing files used by this app
- [ ] Create GitHub issue: `[Mobile migration] <name> → <GITHUB_NAME>`
- [ ] Add to [Platform Health project](https://github.com/orgs/mitf-dev-space/projects/2)

---

## Phase 1 — Mirror git history

From company network (VPN if required):

```powershell
$GITLAB_URL = "http://10.10.20.51/front-end/payment/payment-core.git"
$GITHUB_NAME = "mitf-payment-core"
$ORG = "mitf-dev-space"

pwsh ./scripts/mobile/Mirror-GitLabRepo.ps1 `
  -GitLabUrl $GITLAB_URL `
  -GitHubName $GITHUB_NAME `
  -Organization $ORG
```

- [ ] All branches and tags visible on GitHub
- [ ] Run `gitleaks detect` or spot-check for tokens in history
- [ ] If PAT found in history → rotate + BFG scrub before team clone

---

## Phase 2 — Normalize branches

```powershell
$ORG = "mitf-dev-space"
$REPO = "mitf-payment-core"
cd $REPO

# Identify current production branch from inventory main_branch_gitlab
# Map: master|main|Main → main ; development|develop → develop

$prod = "master"   # from inventory
if ($prod -ne "main") {
  git fetch origin
  git checkout $prod
  git branch -m main
  git push -u origin main
  gh api "repos/$ORG/$REPO" -X PATCH -f default_branch=main
}

# Integration branch
foreach ($legacy in @("development", "develop", "Development")) {
  if (git ls-remote --heads origin $legacy) {
    git fetch origin $legacy
    git checkout -B develop origin/$legacy
    git push -u origin develop
    break
  }
}
```

- [ ] Default branch = `main`
- [ ] `develop` exists
- [ ] Document legacy names in `README.md` → Migration section

---

## Phase 3 — Rewrite pubspec dependencies (apps only)

Skip for **mobile-package** repos.

```powershell
pwsh ./scripts/mobile/Rewrite-PubspecDeps.ps1 -RepoPath . -Ref develop
flutter pub get
flutter analyze
flutter test
```

- [ ] No `path: ../` dependencies remain
- [ ] Internal `10.10.20.51` git URLs replaced with `github.com/mitf-dev-space`

---

## Phase 4 — Migrate secrets & signing keys

Follow [MOBILE_SECRETS_AND_KEYS_RUNBOOK.md](./MOBILE_SECRETS_AND_KEYS_RUNBOOK.md).

```powershell
# Example: Android keystore
gh secret set ANDROID_KEYSTORE_BASE64 --repo $ORG/$REPO < keystore.b64
gh secret set ANDROID_KEYSTORE_PASSWORD --repo $ORG/$REPO --body "***"
gh secret set ANDROID_KEY_ALIAS --repo $ORG/$REPO --body "***"
gh secret set ANDROID_KEY_PASSWORD --repo $ORG/$REPO --body "***"
```

- [ ] All GitLab CI variables accounted for in GitHub
- [ ] Signing works in Actions test build (development flavor)
- [ ] **Do not disable GitLab CI until GitHub build is green**

---

## Phase 5 — GitHub Actions CI

```powershell
mkdir -p .github/workflows
cp ../docs/templates/flutter-ci.yml .github/workflows/flutter-ci.yml
# Edit flutter version if .fvmrc exists
git add .github/workflows/flutter-ci.yml
git commit -m "ci: add Flutter CI workflow for GitHub Actions"
git push
```

- [ ] `flutter-ci.yml` green on `main`
- [ ] CodeQL + dependency-review from org template (optional second PR)

---

## Phase 6 — Org standards

```powershell
$ORG = "mitf-dev-space"
$REPO = "mitf-payment-core"

gh api "orgs/$ORG/teams/mobile/repos/$ORG/$REPO" -X PUT -f permission=push
gh api "orgs/$ORG/teams/engineering-leads/repos/$ORG/$REPO" -X PUT -f permission=admin
gh api "orgs/$ORG/teams/platform/repos/$ORG/$REPO" -X PUT -f permission=push

gh repo edit "$ORG/$REPO" `
  --add-topic mitf --add-topic mobile --add-topic flutter `
  --add-topic $DOMAIN

gh api "repos/$ORG/$REPO" -X PATCH `
  -f allow_squash_merge=true `
  -f allow_merge_commit=false `
  -f delete_branch_on_merge=true
```

Add: `SECURITY.md`, `.github/CODEOWNERS`, `docs/ai/verification.md` (after first green CI).

---

## Phase 7 — Cutover (no disruption)

1. Announce canonical URL in team channel
2. Verify developers can `flutter pub get` from GitHub-only layout
3. Run parallel CI on GitLab + GitHub for **one release cycle** (packages) or **one hotfix** (apps)
4. Archive GitLab project; README → GitHub URL
5. Update sheet column `migration_status` → `done`
6. Close migration issue

---

## Troubleshooting

| Problem | Fix |
|---------|-----|
| `flutter pub get` fails on GitHub URL | Package repo not migrated or wrong `ref` |
| Keystore build fails | Re-import base64 secret; check line endings |
| iOS build fails on Linux runner | Use `macos-latest` job or self-hosted Mac |
| OnePub publish fails | Set org `ONEPUB_TOKEN`; only for `mitf-core-mobile-banking` |
| FVM version mismatch | Read `.fvmrc`; pin in workflow `flutter-version` |
