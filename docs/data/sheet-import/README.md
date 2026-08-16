# Google Sheet import guide — mobile migration

Use these files to fix the [repository sheet](https://docs.google.com/spreadsheets/d/125Hl9a5Rp1VjkzXGDisWniaW02ID2Jo4jpS_GjZrU8Y/edit) and track progress.

## Files

| File | Purpose |
|------|---------|
| [mobile-repos-corrected.csv](./mobile-repos-corrected.csv) | **24 mobile rows** (20 apps + 4 packages) with corrected branches |
| [pubspec-dependency-map.csv](./pubspec-dependency-map.csv) | Legacy path → GitHub git URL mapping |

## How to import (repo sheet)

1. Open the **Front-End Mobile** tab (or create a **Mobile migration** tab).
2. **File → Import → Upload** → select `mobile-repos-corrected.csv`.
3. Choose **Replace current sheet** or **Insert new columns** if you want to keep history.
4. Add columns if missing: `migration_wave`, `migration_status`, `github_url`, `branch_count`, `notes`.
5. Fix row **Finish Date** → **Daman 360** (already corrected in CSV).

## Developer sheet

[Developer mapping sheet](https://docs.google.com/spreadsheets/d/14QkyaksE7fNKcHETQpSauii-ELzxXsimaMXIZGUPHzM/edit)

Add columns:

| Column | Example |
|--------|---------|
| `github_username` | `anstwechy` |
| `github_team` | `mobile` |
| `gitlab_username` | from GitLab |
| `invite_accepted` | yes/no |
| `mobile_apps_owned` | `mitf-daman-pay`, … |

After invites accepted, run:

```bash
gh api orgs/mitf-dev-space/teams/mobile/memberships/anstwechy -X PUT -f role=member
```

## Regenerate CSVs

From repo root (company network):

```bash
python scripts/mobile/update-mobile-inventory.py
```
