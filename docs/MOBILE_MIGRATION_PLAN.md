# Mobile GitLab → GitHub migration plan

**Strategy:** Package-first **multi-repo** (decision locked 2026-08-16)  
**Target org:** [mitf-dev-space](https://github.com/mitf-dev-space)  
**GitLab host:** `http://10.10.20.51`  
**Inventory:** [data/gitlab-inventory.json](./data/gitlab-inventory.json)  
**Sheet import (corrected):** [data/sheet-import/mobile-repos-corrected.csv](./data/sheet-import/mobile-repos-corrected.csv)

---

## Summary

| Category | Count |
|----------|-------|
| Mobile **apps** (sheet) | 20 |
| Mobile **packages** (added to inventory) | 4 |
| **Total mobile track** | **24** repos |

Apps cannot be mirrored in isolation — they use `path: ../sibling` and internal Git URLs in `pubspec.yaml`. Migrate **packages first**, rewrite dependencies to **GitHub git refs**, then migrate apps.

---

## Architecture decision: package-first multi-repo

| Approach | Why we chose it |
|----------|-----------------|
| **Package-first multi-repo** | Matches current GitLab layout; per-bank permissions; Cloud Agents work repo-by-repo; no monorepo permission blast radius |
| ~~Monorepo~~ | Would force one permission model for all banks |
| ~~OnePub-only~~ | Still need source repos on GitHub for agents and audits |

### Dependency rewrite rule

Replace every local `path:` and internal `git:` URL with:

```yaml
package_name:
  git:
    url: https://github.com/mitf-dev-space/<repo>.git
    ref: <branch-after-normalization>  # usually develop until cutover, then main
```

Mapping: [data/sheet-import/pubspec-dependency-map.csv](./data/sheet-import/pubspec-dependency-map.csv)

---

## Migration waves (mobile track)

| Wave | Repos | When |
|------|-------|------|
| **M1 — Foundation packages** | `mitf-payment-core`, `mitf-sharedcomponents`, `mitf-mobile-widgets`, `mitf-ozmobile`, `mitf-mobile-ocr` | **First** |
| **M2 — Payment wallet apps** | 7 payment apps | After M1 + pubspec rewrite |
| **M3 — Core banking** | `mitf-core-mobile-banking` | After M1 banking packages |
| **M4 — White-label banking apps** | 12 bank apps | After M3; batch by bank family |

### M1 — Foundation packages (order matters)

| # | GitHub repo | GitLab path | Blocks |
|---|-------------|-------------|--------|
| 1 | `mitf-payment-core` | `front-end/payment/payment-core` | All payment apps |
| 2 | `mitf-sharedcomponents` | `front-end/payment/sharedcomponents` | All payment apps |
| 3 | `mitf-mobile-widgets` | `front-end/banking/mobile-widgets` | All banking apps |
| 4 | `mitf-ozmobile` | `front-end/banking/packages/ozmobile` | `core-mobile-banking` |
| 5 | `mitf-mobile-ocr` | `front-end/banking/packages/mitf-ocr` | Banking apps using OCR |

### M2 — Payment apps

`mitf-daman-pay`, `mitf-musrfy-pay`, `mitf-sahara-pay`, `mitf-siraj-payment`, `mitf-yussor-pay`, `mitf-waha-pay`

**Pilot:** `mitf-daman-pay` (clear deps, moderate branch count).

### M3 — Core banking

`mitf-core-mobile-banking` — 59 branches, Flutter tests, OnePub publish CI. Normalize `develop` (current HEAD) → org `develop`; production line → `main`.

### M4 — Banking white-label apps

Batch suggestions:

| Batch | Apps |
|-------|------|
| Siraj | `mitf-siraj-mobile`, `mitf-siraj-business` |
| Sahara | `mitf-sahara-mobile`, `mitf-sahara-business` |
| Masrfi | `mitf-masrfi-plus`, `mitf-masrfi-business`, `mitf-mobimal` |
| Remaining | `mitf-dib-bank`, `mitf-ncb-business`, `mitf-wahda-business`, `mitf-waha-mobile`, `mitf-daman-360` |

---

## Sheet corrections applied

| Old sheet value | Corrected value |
|-----------------|-----------------|
| **Finish Date** | **Daman 360** → `mitf-daman-360` |
| Core Mobile Banking default `master` | **`develop`** (live GitLab HEAD) |
| DIB bank pipeline = no | **yes** (`.gitlab-ci.yml` APK/AAB) |
| Wahda / waha_pay branches blank | `develop` / `main` only |
| Missing repos | `mobile-widgets`, `sharedcomponents`, `ozmobile`, `mitf-ocr` (mobile package) |

Import corrected rows: **File → Import** in [repo sheet](https://docs.google.com/spreadsheets/d/125Hl9a5Rp1VjkzXGDisWniaW02ID2Jo4jpS_GjZrU8Y/edit) from `mobile-repos-corrected.csv`.

Developer mapping sheet: [developers sheet](https://docs.google.com/spreadsheets/d/14QkyaksE7fNKcHETQpSauii-ELzxXsimaMXIZGUPHzM/edit) — add columns `GitHub team`, `Mobile migration owner`, `Invite accepted`.

---

## Per-repo procedure

Use [MOBILE_MIGRATION_RUNBOOK.md](./MOBILE_MIGRATION_RUNBOOK.md) for every repo.

High-level:

1. **Mirror** — `scripts/mobile/Mirror-GitLabRepo.ps1`
2. **Normalize branches** — `main` + `develop` per [NAMING_AND_BRANCH_STANDARDS.md](./NAMING_AND_BRANCH_STANDARDS.md)
3. **Rewrite pubspec** (apps only) — `scripts/mobile/Rewrite-PubspecDeps.ps1`
4. **Migrate secrets** — [MOBILE_SECRETS_AND_KEYS_RUNBOOK.md](./MOBILE_SECRETS_AND_KEYS_RUNBOOK.md)
5. **Add CI** — `.github/workflows/flutter-ci.yml` from template
6. **Org standards** — teams, topics, SECURITY.md, CODEOWNERS
7. **Verify** — green Actions run; `flutter pub get` + `flutter test`
8. **Cutover** — archive GitLab; update sheet `migration_status` → `done`

---

## Secrets & keys (zero-disruption)

All GitLab CI/CD variables, Android keystores, iOS signing assets, and tokens must be migrated **before** disabling GitLab pipelines.

| Class | GitLab source | GitHub destination |
|-------|---------------|-------------------|
| Android keystore | CI variables / runner files | Repo or org secrets (base64) |
| iOS certs & profiles | CI variables / Mac runner | Repo secrets (base64) |
| `ONEPUB_TOKEN` | core-mobile-banking CI | Org secret |
| Firebase / Huawei | Committed JSON (audit) | Keep in repo or move to secrets |
| API keys in `envied` | `.env` / CI vars | GitHub Actions secrets + environments |

Full checklist: [MOBILE_SECRETS_AND_KEYS_RUNBOOK.md](./MOBILE_SECRETS_AND_KEYS_RUNBOOK.md)

**Security action:** Rotate exposed GitLab PAT found in `dib-bank` pubspec history (`glpat-…` in comment).

---

## CI/CD standard (Flutter)

| Step | Command |
|------|---------|
| Setup | `subosito/flutter-action` + FVM if `.fvmrc` present |
| Deps | `flutter pub get` |
| Codegen | `dart run build_runner build --delete-conflicting-outputs` (if `build_runner` in pubspec) |
| Analyze | `flutter analyze` |
| Test | `flutter test` |
| Android build (optional) | `./build.sh <flavor>` per app |

Template: [templates/flutter-ci.yml](./templates/flutter-ci.yml)

Banking apps with flavors: mock / development / staging / production (see `dib-bank` GitLab CI).

---

## GitHub org prerequisites

| Item | Owner | Status |
|------|-------|--------|
| `mobile` team populated from [developer sheet](https://docs.google.com/spreadsheets/d/14QkyaksE7fNKcHETQpSauii-ELzxXsimaMXIZGUPHzM/edit) | Engineering lead | Pending invites |
| Org secrets: `ONEPUB_TOKEN`, shared Android keystore policy | DevOps | Documented |
| macOS runner for iOS (self-hosted or GitHub larger runners) | DevOps | Plan required |
| `MobileChannel` backend still on GitLab | Backend wave | Apps need API for E2E |

---

## Success criteria (mobile track complete)

- [ ] All **24** repos mirrored on GitHub with full branch history
- [ ] All `pubspec.yaml` use GitHub git URLs (no `path: ../`)
- [ ] All secrets migrated; GitLab CI disabled only after green GitHub Actions
- [ ] Sheet `migration_status` = `done` for all mobile rows
- [ ] Platform Health project updated
- [ ] GitLab projects archived with README pointing to GitHub

---

## Related docs

- [MOBILE_MIGRATION_RUNBOOK.md](./MOBILE_MIGRATION_RUNBOOK.md) — step-by-step per repo
- [MOBILE_SECRETS_AND_KEYS_RUNBOOK.md](./MOBILE_SECRETS_AND_KEYS_RUNBOOK.md) — keys & CI variables
- [GITLAB_MIGRATION_RUNBOOK.md](./GITLAB_MIGRATION_RUNBOOK.md) — generic mirror steps
- [GITLAB_MIGRATION_WAVES.md](./GITLAB_MIGRATION_WAVES.md) — full org wave index
