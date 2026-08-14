# Public profile checklist — MITF Dev Space

Steps to polish the **public image** of https://github.com/mitf-dev-space. Most are one-time UI changes; logo asset is already in this repo.

---

## Done in repo (automated)

- [x] Org profile README with logo, badges, platform catalog — `profile/README.md`
- [x] SVG logo — `profile/logo.svg`
- [x] Public doc repos linked from profile
- [x] Governance and migration docs in `.github`

---

## Do in GitHub UI (recommended, ~15 minutes)

### 1. Organization avatar (logo)

1. Export `profile/logo.svg` to **512×512 PNG** (Figma, Inkscape, or any SVG→PNG tool)
2. Open https://github.com/organizations/mitf-dev-space/settings/profile
3. Upload PNG as **Organization picture**

Until then, the README displays the logo via raw GitHub URL.

### 2. Organization profile fields

https://github.com/organizations/mitf-dev-space/settings/profile

| Field | Suggested value |
|-------|-----------------|
| **Display name** | MITF Dev Space |
| **Description** | Company engineering organization for Masarat / MITF digital platforms |
| **URL** | Your company site (e.g. Masarat corporate URL when approved) |
| **Location** | Tripoli, Libya (or company HQ) |
| **Email** | `a.almesbahi@masarat.ly` or team engineering alias |

```bash
gh api orgs/mitf-dev-space -X PATCH \
  -f description="Company engineering organization for Masarat / MITF digital platforms" \
  -f location="Tripoli, Libya" \
  -f blog="https://YOUR-COMPANY-URL"
```

### 3. Pin repositories on org home

https://github.com/mitf-dev-space — **Customize pins**

Suggested pins (mix product + docs):

1. `dev-office-assistance` — live public app + Pages
2. `mitf_wallet_public_docs`
3. `mitf_aml_public_docs`
4. `public_online_payment_docs`
5. `mitf-platform-template`
6. `.github` — profile + governance

### 4. Social preview (link sharing)

When someone shares `github.com/mitf-dev-space`, GitHub uses the org avatar + description. For richer previews on specific repos, add `social-preview.png` (1280×640) to public repos under **Settings → Social preview**.

Template idea: logo left, “MITF Dev Space — Masarat Engineering” right, gradient `#0d1117` → `#2563eb`.

### 5. Consistent public repo READMEs

For each **public** repo, ensure:

- [ ] One-line description in repo settings
- [ ] Topics: `mitf`, product name, stack (`csharp`, `flutter`, `docs`)
- [ ] README with link back to org profile
- [ ] LICENSE file (MIT for docs, proprietary notice for code if required by legal)

### 6. GitHub Pages org site (optional, Free)

Publish a simple landing page from `.github` or a dedicated `mitf-dev-space.github.io` repo:

- Link to public docs
- Link to careers / contact (if allowed)
- Status: “Engineering migration in progress” banner during GitLab cutover

### 7. Open source posture (optional)

| Option | Cost | Benefit |
|--------|------|---------|
| **GitHub Sponsors** | Free to enable | Community goodwill (if applicable) |
| **Discussions** on `.github` | Free | Q&A for integrators on public docs |
| **Public roadmap** | Free | Use Platform Health project (private) or public GitHub Project when ready |

We currently keep **Discussions disabled** on platform repos for noise control — enable only on doc repos if needed.

---

## Brand guidelines (lightweight)

| Element | Value |
|---------|--------|
| Primary blue | `#2563eb` |
| Accent cyan | `#06b6d4` |
| Dark background | `#0d1117` |
| Text on dark | `#f0f6fc` |
| Logo | `profile/logo.svg` — do not stretch; min 64px display |
| Name | **MITF Dev Space** (not “MITFDevSpace” in prose) |

If Masarat has an official brand kit, replace gradient colors with approved palette and swap `logo.svg` for brand-approved artwork.

---

## Future upgrades (when budget allows)

| Upgrade | Unlocks |
|---------|---------|
| GitHub Team ($4/user/mo) | Required CODEOWNERS enforcement on private repos, more Actions minutes |
| Verified domain | `mitf-dev-space` badge on profile, SAML SSO |
| Custom GitHub Enterprise | Audit log retention, advanced security at scale |

Staying on **GitHub Free** is fine until CODEOWNERS enforcement or SSO is required.

---

## Quick audit command

```bash
gh api orgs/mitf-dev-space --jq '{name: .login, description, blog, location, public_repos}'
gh repo list mitf-dev-space --visibility public --json name,description,homepageUrl
```
