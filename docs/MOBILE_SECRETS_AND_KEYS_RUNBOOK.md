# Mobile secrets, signing keys & CI variables

Migrate **before** disabling GitLab CI. GitHub does not copy secrets from GitLab.

**Parent:** [MOBILE_MIGRATION_PLAN.md](./MOBILE_MIGRATION_PLAN.md)  
**Generic secrets:** [ACTIONS_SECRETS_RUNBOOK.md](./ACTIONS_SECRETS_RUNBOOK.md)

---

## Export from GitLab (per project)

GitLab UI: **Settings → CI/CD → Variables** → export manually or use API:

```bash
# Requires GITLAB_TOKEN with read_api (run on company network)
curl --header "PRIVATE-TOKEN: $GITLAB_TOKEN" \
  "http://10.10.20.51/api/v4/projects/<url-encoded-path>/variables"
```

Store exports in a **password manager** or encrypted vault — never commit to git.

---

## Organization secrets (shared across mobile repos)

| Secret | Used by | Notes |
|--------|---------|-------|
| `ONEPUB_TOKEN` | `mitf-core-mobile-banking` | Private pub publish (`onepub import`) |
| `GITLAB_READ_TOKEN` | Migration scripts only | Temporary; revoke after cutover |

```bash
gh secret set ONEPUB_TOKEN --org mitf-dev-space --visibility private
```

---

## Per-repo secrets — Android signing

Required for apps with `build.sh` / release APK or AAB (e.g. `dib-bank`).

| Secret | Description |
|--------|-------------|
| `ANDROID_KEYSTORE_BASE64` | Base64 of `.jks` / `.keystore` file |
| `ANDROID_KEYSTORE_PASSWORD` | Keystore password |
| `ANDROID_KEY_ALIAS` | Key alias |
| `ANDROID_KEY_PASSWORD` | Key password |

```powershell
# Create base64 (Windows)
[Convert]::ToBase64String([IO.File]::ReadAllBytes("release.keystore")) | Set-Content keystore.b64
gh secret set ANDROID_KEYSTORE_BASE64 --repo mitf-dev-space/mitf-dib-bank < keystore.b64
gh secret set ANDROID_KEYSTORE_PASSWORD --repo mitf-dev-space/mitf-dib-bank --body "YOUR_PASSWORD"
```

**GitLab source:** CI variables often named `KEYSTORE_*`, `ANDROID_*`, or stored on runner filesystem — ask mobile DevOps lead.

---

## Per-repo secrets — iOS signing

| Secret | Description |
|--------|-------------|
| `IOS_DIST_CERTIFICATE_BASE64` | Distribution certificate (.p12) |
| `IOS_DIST_CERTIFICATE_PASSWORD` | P12 password |
| `IOS_PROVISIONING_PROFILE_BASE64` | `.mobileprovision` |
| `APP_STORE_CONNECT_API_KEY_ID` | App Store Connect API |
| `APP_STORE_CONNECT_API_ISSUER_ID` | Issuer ID |
| `APP_STORE_CONNECT_API_KEY_BASE64` | `.p8` key file |

iOS builds require **macOS** runners (`macos-latest` or self-hosted Mac).

---

## Firebase & Huawei (push / analytics)

Many apps commit these files (already in repo):

| File | Platform |
|------|----------|
| `android/app/google-services.json` | Firebase Android |
| `ios/Runner/GoogleService-Info.plist` | Firebase iOS |
| `android/app/agconnect-services.json` | Huawei |

**Migration rule:**

1. Keep committed files if already in GitLab history (no behavior change).
2. For **new** environments, prefer GitHub **Environments** (`development`, `staging`, `production`) with environment-scoped secrets writing files in CI before build.

---

## Envied / dart-define secrets

Apps using `envied` package load API URLs and keys from generated code.

| GitLab source | GitHub destination |
|---------------|-------------------|
| `.env` files on developer machines | Not migrated — developers keep local |
| CI variables injected before `build_runner` | GitHub Actions `env:` + secrets |
| `envied` input files in repo | Audit; remove production secrets from git |

CI pattern:

```yaml
- name: Generate envied
  env:
    API_BASE_URL: ${{ vars.API_BASE_URL }}
    API_KEY: ${{ secrets.API_KEY }}
  run: dart run build_runner build --delete-conflicting-outputs
```

---

## Package publishing (OnePub)

`mitf-core-mobile-banking` `.gitlab-ci.yml`:

```yaml
- onepub import $ONEPUB_TOKEN
- dart pub publish --force
```

On GitHub:

```yaml
env:
  ONEPUB_TOKEN: ${{ secrets.ONEPUB_TOKEN }}
run: |
  dart pub global activate onepub
  onepub import "$ONEPUB_TOKEN"
  dart pub publish --force
```

---

## Secrets checklist by repo type

### mobile-package (M1)

| Repo | Typical secrets |
|------|-----------------|
| `mitf-payment-core` | None (library) |
| `mitf-sharedcomponents` | None |
| `mitf-mobile-widgets` | None |
| `mitf-ozmobile` | None |
| `mitf-mobile-ocr` | None |

### payment app (M2)

| Repo | Typical secrets |
|------|-----------------|
| All payment wallets | Android keystore; Firebase; API base URL vars |

### core banking (M3)

| Repo | Secrets |
|------|---------|
| `mitf-core-mobile-banking` | `ONEPUB_TOKEN` |

### banking white-label (M4)

| Repo | Secrets |
|------|---------|
| Each bank app | Android keystore (per app/bank); iOS signing (per app); Firebase/Huawei JSON; flavor-specific API URLs |

---

## Verification after migration

```bash
gh secret list --repo mitf-dev-space/mitf-dib-bank
gh variable list --repo mitf-dev-space/mitf-dib-bank
gh run list --repo mitf-dev-space/mitf-dib-bank --limit 5
```

Compare variable **count** GitLab vs GitHub before archiving GitLab.

---

## Security remediation (required)

| Issue | Action |
|-------|--------|
| Exposed `glpat-…` in `dib-bank` pubspec comment | **Rotate token** in GitLab; scrub git history on GitHub mirror |
| Keystores in git history | BFG remove; rotate keys if ever committed |

---

## Post-cutover

- [ ] Revoke GitLab deploy tokens and runner-specific credentials
- [ ] Remove `GITLAB_READ_TOKEN` org secret
- [ ] Document secret owners in repo `README.md` → Security section
