# GitLab repository inventory (source of truth)

Exported from Google Sheet **Repo It DEP 01**:
https://docs.google.com/spreadsheets/d/125Hl9a5Rp1VjkzXGDisWniaW02ID2Jo4jpS_GjZrU8Y/edit

**GitLab host:** `http://10.10.20.51`  
**Total repositories:** 67  
**Target org:** [mitf-dev-space](https://github.com/mitf-dev-space)

Regenerate after sheet updates:
```bash
# From company network — export tabs then run parse_inventory.py + generate_inventory_md.py
```

---

## Back-End — Core services (2)

| GitLab name | Proposed GitHub name | GitLab path | Pipeline (sheet) | Unit tests (sheet) |
|-------------|----------------------|-------------|------------------|-------------------|
| Mitt.SystemCore | `mitf-mitt-systemcore` | `back-end/core-services` | no | yes |
| SMSChannel | `mitf-smschannel` | `back-end/core-services` | no | yes |

## Back-End — Gateways (8)

| GitLab name | Proposed GitHub name | GitLab path | Pipeline (sheet) | Unit tests (sheet) |
|-------------|----------------------|-------------|------------------|-------------------|
| Masarat.Salaries.Adapter | `masarat-salaries-adapter` | `back-end/gateways` | no | yes |
| Masarat.Salaries.MWAdapter | `masarat-salaries-mwadapter` | `back-end/gateways` | no | yes |
| Mitf.BackOffice | `mitf-backoffice` | `back-end/gateways` | no | yes |
| Mitf.BankBackOffice.API | `mitf-bankbackoffice-api` | `back-end/gateways` | no | yes |
| Mitf.OnlinePayment | `mitf-onlinepayment` | `back-end/gateways` | no | yes |
| Mitf.Whatsapp.Gateway | `mitf-whatsapp-gateway` | `back-end/gateways` | no | yes |
| MobileChannel | `mitf-mobilechannel` | `back-end/gateways/mobile` | no | yes |
| SIBSmsGateway | `mitf-sibsmsgateway` | `back-end/gateways` | no | yes |

## Back-End — Office (2)

| GitLab name | Proposed GitHub name | GitLab path | Pipeline (sheet) | Unit tests (sheet) |
|-------------|----------------------|-------------|------------------|-------------------|
| Mitf.Office.CustomerManagement | `mitf-office-customermanagement` | `back-end/other-projects/office` | no | no |
| MITF.Office.Government | `mitf-office-government` | `back-end/other-projects/office` | no | no |

## Back-End — Other projects (17)

| GitLab name | Proposed GitHub name | GitLab path | Pipeline (sheet) | Unit tests (sheet) |
|-------------|----------------------|-------------|------------------|-------------------|
| BillProviderApi | `mitf-billproviderapi` | `back-end/other-projects` | no | no |
| DPHProject | `mitf-dphproject` | `back-end/other-projects` | no | no |
| Mitf.BillAggregator | `mitf-billaggregator` | `back-end/other-projects` | no | no |
| Mitf.billPayment.Gov.Api | `mitf-billpayment-gov-api` | `back-end/other-projects` | no | no |
| Mitf.Cub3 | `mitf-cub3` | `back-end/other-projects` | no | no |
| Mitf.Customer.OCR | `mitf-customer-ocr` | `back-end/other-projects` | no | no |
| Mitf.CustomerControl | `mitf-customercontrol` | `back-end/other-projects` | no | no |
| Mitf.ExpensesManagement | `mitf-expensesmanagement` | `back-end/other-projects` | no | no |
| Mitf.KYC.Api | `mitf-kyc-api` | `back-end/other-projects` | no | no |
| Mitf.OCR | `mitf-ocr` | `back-end/other-projects` | no | no |
| Mitf.PaymentQueries | `mitf-paymentqueries` | `back-end/other-projects` | no | no |
| Mitf.PortalBridge | `mitf-portalbridge` | `back-end` | no | no |
| Mitf.RequestApplicant.RequestApplicant | `mitf-requestapplicant-requestapplicant` | `back-end` | no | no |
| Mitf.SoftPointOfSale.Management | `mitf-softpointofsale-management` | `back-end/other-projects` | no | no |
| Mitf.Unpay.Gateway | `mitf-unpay-gateway` | `back-end/other-projects` | no | no |
| OutBoundAPI | `mitf-outboundapi` | `back-end/other-projects/cub3` | no | yes |
| SoundBox | `mitf-soundbox` | `back-end/other-projects` | no | no |

## Back-End — Providers (1)

| GitLab name | Proposed GitHub name | GitLab path | Pipeline (sheet) | Unit tests (sheet) |
|-------------|----------------------|-------------|------------------|-------------------|
| Mitf.Providers.DocumentGeneratorApi | `mitf-providers-documentgeneratorapi` | `back-end/providers` | no | no |

## Back-End — Reporting (1)

| GitLab name | Proposed GitHub name | GitLab path | Pipeline (sheet) | Unit tests (sheet) |
|-------------|----------------------|-------------|------------------|-------------------|
| Mitf.ReportingApii | `mitf-reportingapii` | `back-end/reporting` | no | no |

## Back-End — Transactions (8)

| GitLab name | Proposed GitHub name | GitLab path | Pipeline (sheet) | Unit tests (sheet) |
|-------------|----------------------|-------------|------------------|-------------------|
| Mitf.ArchiveTransactionsApi | `mitf-archivetransactionsapi` | `back-end/transactions` | no | no |
| Mitf.BankAdapter | `mitf-bankadapter` | `back-end/transactions` | no | no |
| Mitf.OnePayAdapter | `mitf-onepayadapter` | `back-end/transactions` | no | no |
| Mitf.OnePaySettlements | `mitf-onepaysettlements` | `back-end/transactions` | no | no |
| Mitf.PayBill | `mitf-paybill` | `back-end/transactions/paybill` | no | no |
| Mitf.Transactions.CrossBankS2MAdapter | `mitf-transactions-crossbanks2madapter` | `back-end/transactions` | no | no |
| Mitf.Transactions.ExternalS2MAdapter | `mitf-transactions-externals2madapter` | `back-end/transactions` | no | no |
| Mitf.Transactions.TransactionsHubApi | `mitf-transactions-transactionshubapi` | `back-end/transactions` | no | no |

## Back-End — Voucher provider (4)

| GitLab name | Proposed GitHub name | GitLab path | Pipeline (sheet) | Unit tests (sheet) |
|-------------|----------------------|-------------|------------------|-------------------|
| voucher.external | `mitf-voucher-external` | `back-end/other-projects/voucher-provider` | no | no |
| voucher.internal | `mitf-voucher-internal` | `back-end/other-projects/voucher-provider` | no | no |
| voucher.management | `mitf-voucher-management` | `back-end/other-projects/voucher-provider` | no | no |
| Voucher.PurchaseOrchestrator | `mitf-voucher-purchaseorchestrator` | `back-end/other-projects/voucher-provider` | no | no |

## Front-End Mobile — Banking (13)

| GitLab name | Proposed GitHub name | GitLab path | Pipeline (sheet) | Unit tests (sheet) |
|-------------|----------------------|-------------|------------------|-------------------|
| Core Mobile Banking | `mitf-core-mobile-banking` | `front-end/banking` | yes | yes |
| DIB bank | `mitf-dib-bank` | `front-end/banking` | no | yes |
| Finish Date | `mitf-finish-date` | `front-end/banking` | no | no |
| Masrfi Business | `mitf-masrfi-business` | `front-end/banking` | no | yes |
| Masrfi Plus | `mitf-masrfi-plus` | `front-end/banking` | no | yes |
| Mobimal | `mitf-mobimal` | `front-end/banking` | no | yes |
| Ncb Business | `mitf-ncb-business` | `front-end/banking` | no | yes |
| Sahara Business | `mitf-sahara-business` | `front-end/banking` | no | yes |
| Sahara Mobile | `mitf-sahara-mobile` | `front-end/banking` | no | yes |
| Siraj Business | `mitf-siraj-business` | `front-end/banking` | no | yes |
| Siraj Mobile | `mitf-siraj-mobile` | `front-end/banking` | no | yes |
| Waha Mobile | `mitf-waha-mobile` | `front-end/banking` | no | yes |
| Wahda Business | `mitf-wahda-business` | `front-end/banking` | no | yes |

## Front-End Mobile — Payment (7)

| GitLab name | Proposed GitHub name | GitLab path | Pipeline (sheet) | Unit tests (sheet) |
|-------------|----------------------|-------------|------------------|-------------------|
| Daman pay | `mitf-daman-pay` | `front-end/payment` | no | yes |
| Musrfy pay | `mitf-musrfy-pay` | `front-end/payment` | no | yes |
| Payment core | `mitf-payment-core` | `front-end/payment` | no | yes |
| Sahara pay | `mitf-sahara-pay` | `front-end/payment` | no | yes |
| Siraj Payment | `mitf-siraj-payment` | `front-end/payment` | no | yes |
| waha_pay | `mitf-waha-pay` | `front-end/payment` | no | yes |
| Yussor pay | `mitf-yussor-pay` | `front-end/payment` | no | yes |

## Front-End Web (4)

| GitLab name | Proposed GitHub name | GitLab path | Pipeline (sheet) | Unit tests (sheet) |
|-------------|----------------------|-------------|------------------|-------------------|
| Biller Aggregator | `mitf-biller-aggregator` | `front-end/web` | yes | no |
| control-panel | `mitf-control-panel` | `front-end/web` | yes | no |
| mitf-office | `mitf-office` | `front-end/web` | yes | no |
| webpages-v2 | `mitf-webpages-v2` | `front-end/web` | yes | yes |
