# MITF Dev Space

Company engineering organization for MITF platform development.

## Teams

| Team | Scope |
|------|-------|
| `engineering-leads` | Cross-platform visibility for full-stack platform repositories |
| `backend` | Platform services (API, workers, domain logic) |
| `web` | Web applications and frontends |
| `mobile` | Mobile applications |
| `devops` | Infrastructure, compose stacks, CI/CD |
| `platform` | Shared tooling, release management, documentation |

## Repository model

Each **platform** repository (e.g. notification, voucher, support, insurance) is a full-stack monorepo containing backend, web, infrastructure, and E2E components. Access is granted per platform based on team membership.

## Security

- Private by default
- Team-based access (no org-wide write)
- 2FA required for members (enable after onboarding)