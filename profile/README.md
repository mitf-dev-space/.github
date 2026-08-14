# MITF Dev Space — Platform Catalog

Company-owned full-stack platform repositories. Each repo is a **platform** (backend + web + infrastructure + E2E), not a single-layer service.

## Active platforms (organization)

| Platform | Repository | Primary stack | Teams |
|----------|------------|---------------|-------|
| Support | [mitf-support](https://github.com/mitf-dev-space/mitf-support) | C#, TypeScript, Python, Docker | engineering-leads, backend, platform |
| Notification | [mitf_notification_system](https://github.com/mitf-dev-space/mitf_notification_system) | C#, TypeScript, Flutter | engineering-leads, backend, platform |
| Voucher | [voucher-provider-workspace](https://github.com/mitf-dev-space/voucher-provider-workspace) | C#, TypeScript, Python | engineering-leads, backend, platform |
| AML | [mitf-aml-system](https://github.com/mitf-dev-space/mitf-aml-system) | C#, TypeScript, Python | engineering-leads, backend, platform |
| Insurance | [insurance-provider-hub](https://github.com/mitf-dev-space/insurance-provider-hub) | C# | engineering-leads, backend, platform |
| Payment ecosystem | [mitf-payment-ecosystem](https://github.com/mitf-dev-space/mitf-payment-ecosystem) | C#, TypeScript | engineering-leads, backend, platform |
| Online payment | [mitf-online-payment](https://github.com/mitf-dev-space/mitf-online-payment) | TypeScript | engineering-leads, backend, platform |
| Release management | [release-management](https://github.com/mitf-dev-space/release-management) | C#, TypeScript, Python | engineering-leads, backend, platform |
| Sanctions | [ch-sanctions](https://github.com/mitf-dev-space/ch-sanctions) | C#, TypeScript | engineering-leads, backend, platform |
| Account assistance | [account_assistance](https://github.com/mitf-dev-space/account_assistance) | C#, Python, Flutter | engineering-leads, backend, platform |
| Agent workspace | [agent-workspace](https://github.com/mitf-dev-space/agent-workspace) | Python, Docker | engineering-leads, backend, platform |
| Office assistance | [dev-office-assistance](https://github.com/mitf-dev-space/dev-office-assistance) | TypeScript, Python (public) | engineering-leads, web, backend |
| Omni studio | [omni-studio](https://github.com/mitf-dev-space/omni-studio) | TypeScript, Python | engineering-leads, web, backend |
| Trading (mobile) | [trading_platform](https://github.com/mitf-dev-space/trading_platform) | Flutter, C++ | engineering-leads, mobile, backend |

## Infrastructure compose stacks (in org)

- [compose-buzz](https://github.com/mitf-dev-space/compose-buzz)
- [compose-omnitest-studio](https://github.com/mitf-dev-space/compose-omnitest-studio) (public)

## Deferred / personal (not in org)

| Item | Location | Notes |
|------|----------|-------|
| Wallet platform | `anstwechy/wallet-services` | Migrate when team is ready |
| Personal | `anstwechy/tw-os`, `anstwechy/masarat-portfolio` | Do not transfer |

## Access model

- Org default permission: **None** — access via teams only
- Platform repos: `engineering-leads` + `backend` + `platform` (Write)
- CODEOWNERS documents ownership; enforcement on private repos requires GitHub Team

## Governance docs

- [Actions secrets runbook](https://github.com/mitf-dev-space/.github/blob/main/docs/ACTIONS_SECRETS_RUNBOOK.md)
- [Quarterly access review](https://github.com/mitf-dev-space/.github/blob/main/docs/ACCESS_REVIEW.md)
- [New platform checklist](https://github.com/mitf-dev-space/.github/blob/main/docs/NEW_PLATFORM_CHECKLIST.md)
- [OIDC & supply chain hardening](https://github.com/mitf-dev-space/.github/blob/main/docs/OIDC_AND_SUPPLY_CHAIN.md)
- [Contributing guide](https://github.com/mitf-dev-space/.github/blob/main/CONTRIBUTING.md)
