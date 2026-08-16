#!/usr/bin/env python3
"""Update gitlab-inventory.json with corrected mobile data and generate sheet CSVs."""

from __future__ import annotations

import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DATA = ROOT / "docs" / "data" / "gitlab-inventory.json"
SHEET_OUT = ROOT / "docs" / "data" / "sheet-import"

# Live GitLab HEAD branches (2026-08-16 audit)
BRANCH_CORRECTIONS: dict[str, dict[str, str | bool | int]] = {
    "Core Mobile Banking": {
        "main_branch_gitlab": "develop",
        "dev_branch_gitlab": "master",
        "has_pipeline": True,
        "branch_count": 59,
        "migration_wave": "M3",
    },
    "DIB bank": {
        "has_pipeline": True,
        "main_branch_gitlab": "development",
        "dev_branch_gitlab": "develop",
        "branch_count": 13,
        "migration_wave": "M4",
    },
    "Finish Date": {
        "name": "Daman 360",
        "github_name": "mitf-daman-360",
        "main_branch_gitlab": "main",
        "dev_branch_gitlab": "develop",
        "has_unit_test": True,
        "branch_count": 5,
        "migration_wave": "M4",
    },
    "Masrfi Business": {"branch_count": 7, "migration_wave": "M4"},
    "Masrfi Plus": {"branch_count": 42, "migration_wave": "M4"},
    "Mobimal": {"branch_count": 30, "migration_wave": "M4"},
    "Ncb Business": {
        "main_branch_gitlab": "develop",
        "dev_branch_gitlab": "master",
        "branch_count": 19,
        "migration_wave": "M4",
    },
    "Sahara Business": {"branch_count": 8, "migration_wave": "M4"},
    "Sahara Mobile": {
        "main_branch_gitlab": "develop",
        "dev_branch_gitlab": "master",
        "branch_count": 27,
        "migration_wave": "M4",
    },
    "Siraj Business": {
        "main_branch_gitlab": "develop",
        "dev_branch_gitlab": "main",
        "branch_count": 4,
        "migration_wave": "M4",
    },
    "Siraj Mobile": {"branch_count": 11, "migration_wave": "M4"},
    "Waha Mobile": {"branch_count": 4, "migration_wave": "M4"},
    "Wahda Business": {
        "main_branch_gitlab": "develop",
        "dev_branch_gitlab": "master",
        "branch_count": 7,
        "migration_wave": "M4",
    },
    "Daman pay": {"branch_count": 7, "migration_wave": "M2"},
    "Musrfy pay": {"branch_count": 11, "migration_wave": "M2"},
    "Payment core": {"branch_count": 22, "migration_wave": "M1", "layer": "mobile-package"},
    "Sahara pay": {"branch_count": 10, "migration_wave": "M2"},
    "Siraj Payment": {"branch_count": 5, "migration_wave": "M2"},
    "Yussor pay": {"branch_count": 17, "migration_wave": "M2"},
    "waha_pay": {
        "main_branch_gitlab": "main",
        "dev_branch_gitlab": "",
        "branch_count": 1,
        "migration_wave": "M2",
    },
}

MOBILE_PACKAGES: list[dict] = [
    {
        "name": "mobile-widgets",
        "gitlab_url": "http://10.10.20.51/front-end/banking/mobile-widgets",
        "gitlab_group": "front-end/banking",
        "layer": "mobile-package",
        "github_name": "mitf-mobile-widgets",
        "has_pipeline": False,
        "has_unit_test": True,
        "main_branch_gitlab": "master",
        "dev_branch_gitlab": "develop",
        "domain": "banking-mobile",
        "migration_wave": "M1",
        "branch_count": 26,
        "depends_on": [],
        "notes": "Shared UI package; path dep from all banking white-label apps",
    },
    {
        "name": "sharedcomponents",
        "gitlab_url": "http://10.10.20.51/front-end/payment/sharedcomponents",
        "gitlab_group": "front-end/payment",
        "layer": "mobile-package",
        "github_name": "mitf-sharedcomponents",
        "has_pipeline": False,
        "has_unit_test": True,
        "main_branch_gitlab": "main",
        "dev_branch_gitlab": "develop",
        "domain": "payment-mobile",
        "migration_wave": "M1",
        "branch_count": 4,
        "depends_on": [],
        "notes": "Shared UI package; path dep from all payment wallet apps",
    },
    {
        "name": "ozmobile",
        "gitlab_url": "http://10.10.20.51/front-end/banking/packages/ozmobile",
        "gitlab_group": "front-end/banking/packages",
        "layer": "mobile-package",
        "github_name": "mitf-ozmobile",
        "has_pipeline": False,
        "has_unit_test": False,
        "main_branch_gitlab": "main",
        "dev_branch_gitlab": "devolop",
        "domain": "banking-mobile",
        "migration_wave": "M1",
        "branch_count": 2,
        "depends_on": [],
        "notes": "Git dep from core-mobile-banking pubspec (ozsdk)",
    },
    {
        "name": "mitf-ocr (mobile)",
        "gitlab_url": "http://10.10.20.51/front-end/banking/packages/mitf-ocr",
        "gitlab_group": "front-end/banking/packages",
        "layer": "mobile-package",
        "github_name": "mitf-mobile-ocr",
        "has_pipeline": False,
        "has_unit_test": False,
        "main_branch_gitlab": "main",
        "dev_branch_gitlab": "refactor/new-flow",
        "domain": "banking-mobile",
        "migration_wave": "M1",
        "branch_count": 2,
        "depends_on": [],
        "notes": "Git dep from banking apps (mitf_ocr package)",
    },
]

PUBSPEC_GIT_MAP = {
    "../payment-core": "https://github.com/mitf-dev-space/mitf-payment-core.git",
    "../sharedcomponents": "https://github.com/mitf-dev-space/mitf-sharedcomponents.git",
    "../core-mobile-banking": "https://github.com/mitf-dev-space/mitf-core-mobile-banking.git",
    "../mobile-widgets": "https://github.com/mitf-dev-space/mitf-mobile-widgets.git",
    "http://10.10.20.51/front-end/banking/packages/ozmobile.git": "https://github.com/mitf-dev-space/mitf-ozmobile.git",
    "http://10.10.20.51/front-end/banking/packages/mitf-ocr.git": "https://github.com/mitf-dev-space/mitf-mobile-ocr.git",
}


def main() -> None:
    items: list[dict] = json.loads(DATA.read_text(encoding="utf-8"))
    by_name = {i["name"]: i for i in items}

    for name, patch in BRANCH_CORRECTIONS.items():
        if name not in by_name:
            continue
        by_name[name].update(patch)

    for pkg in MOBILE_PACKAGES:
        if pkg["name"] not in by_name:
            items.append(pkg)
            by_name[pkg["name"]] = pkg

    # Default migration_wave on remaining mobile apps
    for item in items:
        if item.get("layer") == "mobile" and "migration_wave" not in item:
            item["migration_wave"] = "M4" if item.get("domain") == "banking-mobile" else "M2"

    DATA.write_text(json.dumps(items, indent=2) + "\n", encoding="utf-8")

    SHEET_OUT.mkdir(parents=True, exist_ok=True)
    mobile_rows = [i for i in items if i.get("layer") in ("mobile", "mobile-package")]
    mobile_rows.sort(key=lambda x: (x.get("migration_wave", "M9"), x.get("github_name", "")))

    csv_path = SHEET_OUT / "mobile-repos-corrected.csv"
    fields = [
        "migration_wave",
        "name",
        "github_name",
        "gitlab_url",
        "gitlab_group",
        "layer",
        "domain",
        "main_branch_gitlab",
        "dev_branch_gitlab",
        "has_pipeline",
        "has_unit_test",
        "branch_count",
        "github_url",
        "migration_status",
        "notes",
    ]
    with csv_path.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
        w.writeheader()
        for row in mobile_rows:
            row = dict(row)
            row["github_url"] = f"https://github.com/mitf-dev-space/{row['github_name']}"
            row["migration_status"] = row.get("migration_status", "planned")
            w.writerow(row)

    map_path = SHEET_OUT / "pubspec-dependency-map.csv"
    with map_path.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["legacy_path_or_git_url", "github_git_url", "github_repo"])
        for legacy, gh in PUBSPEC_GIT_MAP.items():
            repo = gh.split("/")[-1].replace(".git", "")
            w.writerow([legacy, gh, repo])

    print(f"Updated {DATA} ({len(items)} repos, {len(mobile_rows)} mobile)")
    print(f"Wrote {csv_path}")
    print(f"Wrote {map_path}")


if __name__ == "__main__":
    main()
