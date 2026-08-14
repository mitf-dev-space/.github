# Sunday migration runbook — MITF Dev Space

**Org:** https://github.com/mitf-dev-space (GitHub Free)  
**Project board:** https://github.com/orgs/mitf-dev-space/projects/2  
**When:** From company domain (Sunday or later)

> **Primary work Sunday:** [GitLab → GitHub migration](./GITLAB_TO_GITHUB_MIGRATION_PLAN.md) (67 repos on `10.10.20.51`).  
> This runbook covers **Track A** — transferring repos already on personal GitHub.

---

## Pre-flight (org is ready)

| Check | Status |
|-------|--------|
| Org created, Free plan | OK |
| 22 repos in org (20 platforms + `.github` + template + archived `AMLSystem`) | OK |
| 6 teams with platform permissions | OK |
| Default repo permission: **None** | OK |
| Members cannot delete repos | OK |
| CodeQL + dependency-review on platform repos | OK |
| Platform Health project (4 views, 15 tracker issues) | OK |
| `mitf-platform-template` for new platforms | OK |

**Accepted members today:** `anstwechy`, `JihadEjdaydhom`, `Siraj95Abudaber`  
**Owners:** `anstwechy`, `JihadEjdaydhom` only (add Rashad + Fayroz when invites accept)

---

## Do NOT migrate yet

| Repo | Reason |
|------|--------|
| `anstwechy/wallet-services` | Team still working — migrate when they confirm |
| `anstwechy/tw-os` | Personal |
| `anstwechy/masarat-portfolio` | Personal |

---

## Sunday queue — transfer one by one

Run from company network if GitHub blocks transfers from home IP.

| # | Personal repo | Target org name | Team notes |
|---|---------------|-----------------|------------|
| 1 | `compose-aml-system` | same | `devops`, `platform` |
| 2 | `compose-office-assistance` | same | `devops`, `platform` |
| 3 | `compose-release-management` | same | `devops`, `platform` |
| 4 | `compose-repo-hub` | same | `devops`, `platform` |
| 5 | `compose-voucher-provider` | same | `devops`, `platform` |
| 6 | `compose-mitf-wallet` | same | `devops`, `platform` (not wallet-services) |
| 7 | `wallet-services` | same | **Only after team sign-off** |

### Per-repo transfer checklist

1. `gh repo transfer anstwechy/REPO mitf-dev-space --target anstwechy`
2. Re-apply team permissions (backend, platform, engineering-leads, devops as appropriate)
3. Verify outside collaborators → remove after invitees join org teams
4. Smoke test: one Actions run on `main`
5. Close tracker issue on `.github` when done

**Transfer command template:**

```powershell
gh api -X POST repos/anstwechy/REPO/transfer -f new_owner=mitf-dev-space
```

If transfer fails (network/policy), retry from company domain or use GitHub UI: **Settings → Danger zone → Transfer**.

---

## Pending invites (chase on Sunday)

14 invites outstanding. Priority:

| User | Current invite | Action |
|------|----------------|--------|
| `FayrozBasher` | **admin** (Owner) | Accept — assistant admin |
| `rashadshayoup` | **member** | Cancel + re-invite as **admin** (engineering lead) |
| Others | member + teams | Accept when ready |

```powershell
# Re-invite Rashad as Owner (after cancelling member invite)
gh api orgs/mitf-dev-space/invitations -q '.[] | select(.login=="rashadshayoup") | .id'
gh api -X DELETE orgs/mitf-dev-space/invitations/INVITE_ID
gh api -X POST orgs/mitf-dev-space/invitations -f invitee_id=138626157 -f role=admin
```

---

## Manual org settings (5 min, company day)

1. **Member privileges** → uncheck **Allow members to change repository visibility**  
   https://github.com/organizations/mitf-dev-space/settings/member_privileges

2. **2FA requirement** → enable after all members enrolled  
   https://github.com/organizations/mitf-dev-space/settings/security

3. **Project workflow access** → grant `mitf-dev-space/.github`  
   https://github.com/orgs/mitf-dev-space/projects/2/settings

4. **Org secret** `DOCKERHUB_TOKEN` (optional) — see [ACTIONS_SECRETS_RUNBOOK.md](./ACTIONS_SECRETS_RUNBOOK.md)

---

## After each migration day

- Update [platform catalog](../profile/README.md) if a new platform lands
- Mark items **Done** on [Platform Health project](https://github.com/orgs/mitf-dev-space/projects/2)
- Do **not** touch `MW-Development-Team` org

---

## Quick links

- [Platform catalog](https://github.com/mitf-dev-space/.github/blob/main/profile/README.md)
- [**GitLab migration plan**](./GITLAB_TO_GITHUB_MIGRATION_PLAN.md)
- [GitLab per-repo runbook](./GITLAB_MIGRATION_RUNBOOK.md)
- [New platform checklist](./NEW_PLATFORM_CHECKLIST.md)
- [Access review](./ACCESS_REVIEW.md)
- [Platform Health setup](./PLATFORM_HEALTH_PROJECT.md)
