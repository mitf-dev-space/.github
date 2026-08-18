# Team repository inventory — sheet import

Canonical CSV inventories for **mitf-dev-space** team access and migration tracking.

## Files

| File | Team | Rows | Purpose |
|------|------|------|---------|
| [backend-repos.csv](./backend-repos.csv) | backend | 45 | Active backend services (running + in development) |
| [mobile-repos-corrected.csv](./mobile-repos-corrected.csv) | mobile | 25 | Mobile apps and packages (excludes blocked vendor mirrors) |
| [web-repos.csv](./web-repos.csv) | web | 4 | Web front-end repositories |
| [pubspec-dependency-map.csv](./pubspec-dependency-map.csv) | mobile | — | Legacy path → GitHub git URL mapping |

`agent-workspace` is shared across teams but is **not** listed in these CSVs. Only org super-admins (`anstwechy`, `FayrozBasher`, `JihadEjdaydhom`) and engineering-leads retain admin on it; all team members have read-only access.

## Access model (Aug 2026)

| Role | Web (4) | Mobile (25) | Backend (45) | agent-workspace |
|------|---------|-------------|--------------|-----------------|
| Super-admins | admin | admin | admin | admin |
| Engineering leads (`rashadshayoup`) | admin | admin | admin | admin |
| Team lead | admin | admin (2 maintainers) | admin (`mohamed49altarhuni`) | read |
| Team members | write | write | write | read |

Apply permissions with:

```powershell
pwsh -File scripts/Apply-TeamPermissions.ps1
```

## Regenerate CSVs

```bash
python scripts/mobile/update-mobile-inventory.py
```

Backend inventory source: GitLab activity analysis + owner matrix (see `BACKEND_INVENTORY_RECONCILIATION.md` in migration workspace).
