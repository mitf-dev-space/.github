# GitLab → GitHub migration waves

Quick reference for Sunday planning. Full detail: [GITLAB_TO_GITHUB_MIGRATION_PLAN.md](./GITLAB_TO_GITHUB_MIGRATION_PLAN.md).

| Wave | Domain | Count | Start after |
|------|--------|-------|-------------|
| 0 | web | 4 | Pilot Sunday |
| 1 | core-services, reporting, providers | 4 | Wave 0 done |
| 2 | office, voucher | 6 | Wave 1 |
| 3 | gateways | 8 | Wave 2 |
| 4 | transactions | 8 | Wave 3 |
| 5 | backend-other | 17 | Wave 4 |
| 6 | payment-mobile | 7 | Wave 5 |
| 7 | banking-mobile | 13 | Wave 6 |

**Total:** 67 GitLab repositories

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
