<div align="center">

<img src="https://raw.githubusercontent.com/mitf-dev-space/.github/main/profile/logo.svg" width="140" alt="MITF Dev Space logo" />

# MITF Dev Space

**Engineering home for Masarat digital platforms** — wallets, payments, banking, compliance, and internal tools.

[![Organization](https://img.shields.io/badge/GitHub-mitf--dev--space-181717?logo=github)](https://github.com/mitf-dev-space)
[![Plan](https://img.shields.io/badge/plan-GitHub%20Free-238636)](https://github.com/pricing)
[![Platforms](https://img.shields.io/badge/platforms-14%2B-2563eb)](https://github.com/mitf-dev-space/.github/blob/main/profile/README.md#platform-catalog)
[![Migration](https://img.shields.io/badge/GitLab→GitHub-in%20progress-06b6d4)](https://github.com/mitf-dev-space/.github/issues/17)

[Platform catalog](#platform-catalog) · [Public docs](#public-documentation) · [Contributing](https://github.com/mitf-dev-space/.github/blob/main/CONTRIBUTING.md) · [Security](https://github.com/mitf-dev-space/.github/blob/main/SECURITY.md)

</div>

---

## What we build

MITF Dev Space is the **company-owned** GitHub organization for MITF / Masarat engineering. We ship **platforms** — full-stack repositories that include backend services, web and mobile apps, infrastructure, and end-to-end tests — not single-layer micro-repos.

| Domain | Examples |
|--------|----------|
| Payments & wallets | Online payment, payment ecosystem, wallet docs |
| Banking & mobile | Core banking apps, white-label bank clients |
| Compliance | AML, sanctions screening |
| Operations | Support AI, notifications, vouchers, release management |
| Productivity | Office assistance, omni studio, agent workspace |

---

## Platform catalog

Each row is one **platform repository** (monolith-style layout).

| Platform | Repository | Stack |
|----------|------------|-------|
| Support | [mitf-support](https://github.com/mitf-dev-space/mitf-support) | C#, TypeScript, Python |
| Notification | [mitf_notification_system](https://github.com/mitf-dev-space/mitf_notification_system) | C#, TypeScript, Flutter |
| Voucher | [voucher-provider-workspace](https://github.com/mitf-dev-space/voucher-provider-workspace) | C#, TypeScript, Python |
| AML | [mitf-aml-system](https://github.com/mitf-dev-space/mitf-aml-system) | C#, TypeScript, Python |
| Insurance | [insurance-provider-hub](https://github.com/mitf-dev-space/insurance-provider-hub) | C# |
| Payment ecosystem | [mitf-payment-ecosystem](https://github.com/mitf-dev-space/mitf-payment-ecosystem) | C#, TypeScript |
| Online payment | [mitf-online-payment](https://github.com/mitf-dev-space/mitf-online-payment) | TypeScript |
| Release management | [release-management](https://github.com/mitf-dev-space/release-management) | C#, TypeScript, Python |
| Sanctions | [ch-sanctions](https://github.com/mitf-dev-space/ch-sanctions) | C#, TypeScript |
| Account assistance | [account_assistance](https://github.com/mitf-dev-space/account_assistance) | C#, Python, Flutter |
| Agent workspace | [agent-workspace](https://github.com/mitf-dev-space/agent-workspace) | Python, Docker |
| Office assistance | [dev-office-assistance](https://github.com/mitf-dev-space/dev-office-assistance) | TypeScript, Python |
| Omni studio | [omni-studio](https://github.com/mitf-dev-space/omni-studio) | TypeScript, Python |
| Trading | [trading_platform](https://github.com/mitf-dev-space/trading_platform) | Flutter, C++ |

**Scaffolding:** [mitf-platform-template](https://github.com/mitf-dev-space/mitf-platform-template) — start a new platform with org standards baked in.

<details>
<summary><strong>Infrastructure &amp; compose stacks</strong></summary>

- [compose-buzz](https://github.com/mitf-dev-space/compose-buzz)
- [compose-omnitest-studio](https://github.com/mitf-dev-space/compose-omnitest-studio) (public)

</details>

---

## Public documentation

Open repositories for partners and integrators:

| Docs | Repository |
|------|------------|
| Wallet | [mitf_wallet_public_docs](https://github.com/mitf-dev-space/mitf_wallet_public_docs) |
| AML | [mitf_aml_public_docs](https://github.com/mitf-dev-space/mitf_aml_public_docs) |
| Online payment | [public_online_payment_docs](https://github.com/mitf-dev-space/public_online_payment_docs) |
| Office assistance (live demo) | [dev-office-assistance](https://github.com/mitf-dev-space/dev-office-assistance) → [GitHub Pages](https://mitf-dev-space.github.io/dev-office-assistance/) |

---

## Engineering standards

We keep one bar across every repository:

- **Branches:** `main` (production) + `develop` (integration) — see [naming standards](https://github.com/mitf-dev-space/.github/blob/main/docs/NAMING_AND_BRANCH_STANDARDS.md)
- **Access:** team-based (`backend`, `web`, `mobile`, `devops`, `platform`, `engineering-leads`)
- **Security:** Dependabot, CodeQL, dependency review, secret scanning on public repos
- **CI/CD:** GitHub Actions with explicit permissions; GHCR for container images

| Resource | Link |
|----------|------|
| Contributing | [CONTRIBUTING.md](https://github.com/mitf-dev-space/.github/blob/main/CONTRIBUTING.md) |
| New platform checklist | [NEW_PLATFORM_CHECKLIST.md](https://github.com/mitf-dev-space/.github/blob/main/docs/NEW_PLATFORM_CHECKLIST.md) |
| GitLab migration (67 repos) | [GITLAB_TO_GITHUB_MIGRATION_PLAN.md](https://github.com/mitf-dev-space/.github/blob/main/docs/GITLAB_TO_GITHUB_MIGRATION_PLAN.md) |
| Platform health board | [Project #2](https://github.com/orgs/mitf-dev-space/projects/2) |

---

## Joining the org

Access is by **invitation** through engineering teams. If you are a Masarat / MITF engineer:

1. Accept your GitHub org invite
2. Confirm you are on the right team (`backend`, `web`, `mobile`, etc.)
3. Read [CONTRIBUTING.md](https://github.com/mitf-dev-space/.github/blob/main/CONTRIBUTING.md) before your first PR

Security issues: follow [SECURITY.md](https://github.com/mitf-dev-space/.github/blob/main/SECURITY.md) — do not open public issues for vulnerabilities.

---

<div align="center">

**MITF Dev Space** · Masarat engineering · Libya

Built with care for reliable financial and government digital services.

</div>
