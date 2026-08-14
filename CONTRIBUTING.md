# Contributing to MITF Dev Space

## Repository model

Each **platform** repository is a full-stack monorepo (backend, web, infrastructure, E2E). Do not split layers into separate repos unless there is a strong technical reason.

## Teams and access

- Access is granted through GitHub teams, not individual repo invites
- `engineering-leads` — cross-platform visibility
- `backend`, `web`, `mobile`, `devops`, `platform` — domain teams

## Pull requests

- Use the PR template (platform name, test plan, CI status)
- Prefer team review from `@mitf-dev-space/engineering-leads` for platform-wide changes
- Keep PRs focused; avoid mixing unrelated platforms

## Branching

- `main` — production-ready (protected review recommended; enforcement requires GitHub Team on private repos)
- `dev` — integration branch where used by the platform

## Security

- Never commit secrets, API keys, or production credentials
- Report security issues per `SECURITY.md`; do not open public issues for vulnerabilities
- Dependabot alerts are enabled on new repositories

## CI/CD

- GitHub Actions minutes are shared at org level (2,000 min/month on Free)
- Use `workflow_dispatch` for manual deploys where gated workflows exist
- See `docs/ACTIONS_SECRETS_RUNBOOK.md` for required secrets after repo transfer

## Naming (new repositories)

- Lowercase kebab-case: `notification-service`, `admin-web`
- Avoid redundant prefixes when team ownership is clear
