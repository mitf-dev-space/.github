# GitLab → GitHub migration waves

Quick reference. Full detail: [GITLAB_TO_GITHUB_MIGRATION_PLAN.md](./GITLAB_TO_GITHUB_MIGRATION_PLAN.md).

**Mobile track (priority):** [MOBILE_MIGRATION_PLAN.md](./MOBILE_MIGRATION_PLAN.md) — package-first multi-repo.

| Wave | Domain | Count | Start after |
|------|--------|-------|-------------|
| **M1** | mobile packages | 5 | **Now** (mobile priority) |
| **M2** | payment-mobile apps | 7 | M1 done |
| **M3** | core-mobile-banking | 1 | M1 banking packages |
| **M4** | banking-mobile apps | 12 | M3 done |
| 0 | web | 4 | Pilot (parallel) |
| 1 | core-services, reporting, providers | 4 | Wave 0 done |
| 2 | office, voucher | 6 | Wave 1 |
| 3 | gateways | 8 | Wave 2 |
| 4 | transactions | 8 | Wave 3 |
| 5 | backend-other | 17 | Wave 4 |

**Total:** 67 GitLab repositories + **4 mobile package repos** (not in original sheet count)

## Mobile wave M1 — Foundation packages (migrate first)

| GitHub name | GitLab path |
|-------------|-------------|
| `mitf-payment-core` | `front-end/payment/payment-core` |
| `mitf-sharedcomponents` | `front-end/payment/sharedcomponents` |
| `mitf-mobile-widgets` | `front-end/banking/mobile-widgets` |
| `mitf-ozmobile` | `front-end/banking/packages/ozmobile` |
| `mitf-mobile-ocr` | `front-end/banking/packages/mitf-ocr` |

## Wave 0 — Sunday pilot (web)

| GitLab name | Proposed GitHub | GitLab URL path |
|-------------|-----------------|-----------------|
| webpages-v2 | `webpages-v2` | `front-end/web/webpages-v2` |
| mitf-office | `mitf-office-web` * | `front-end/web/mitf-office` |
| control-panel | `control-panel` | `front-end/web/control-panel` |
| Biller Aggregator | `biller-aggregator` | `front-end/web/biller-aggregator` |

\* May merge with existing org web assets — decide at pilot.

## Sheet reference

https://docs.google.com/spreadsheets/d/125Hl9a5Rp1VjkzXGDisWniaW02ID2Jo4jpS_GjZrU8Y/edit

Machine-readable: [data/gitlab-inventory.json](./data/gitlab-inventory.json)
