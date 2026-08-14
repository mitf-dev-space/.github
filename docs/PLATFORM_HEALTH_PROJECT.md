# MITF Platform Health — Project setup guide

Project board: **https://github.com/orgs/mitf-dev-space/projects/2**

This document covers what was automated in the org and what you configure once in the **Project UI** (requires org owner).

---

## Already automated (via `.github` repo)

- **15 tracker issues** created in `mitf-dev-space/.github` with label `platform-health`
- **Auto-add workflow** on `.github` (and can be copied to platform repos) — adds items to project 2 when labeled `platform-health`
- Label `platform-health` on the org profile repo

After you complete **Step 1** below (grant workflow access), new issues will appear on the board automatically.

---

## Step 1 — Grant workflow access (required, 2 minutes)

1. Open https://github.com/orgs/mitf-dev-space/projects/2/settings
2. Scroll to **Workflow access** (or **Manage access**)
3. Set **Repository access** to include `mitf-dev-space/.github` (or **All repositories**)
4. Save

Without this, the auto-add Action cannot add cards to the project.

---

## Step 2 — Add custom fields

In the project table, click **+** next to column headers → **New field**:

| Field name | Type | Options |
|------------|------|---------|
| Platform | Single select | Support, AML, Wallet, Payment, Notification, DevOps, Org, Other |
| Priority | Single select | P0, P1, P2, P3 |
| Work type | Single select | CI/CD, Security, Migration, Feature, Bug, Ops |
| Health | Single select | Green, Yellow, Red |

Keep built-in **Status**: Backlog → Todo → In progress → In review → Done

---

## Step 3 — Create views

Click **+ New view** for each:

### Platform health (Table) — default
- Group by: **Repository**
- Sort: **Health** (asc), then **Priority**
- Filter: Status is not Done

### CI & security (Table)
- Filter: Label contains `security` OR `devops` OR Work type is `CI/CD`

### Active work (Board)
- Layout: Board
- Group by: **Status**
- Filter: Status is Todo, In progress, or In review

### Roadmap (Roadmap) — optional
- Add field **Target date** (Date) first
- Layout: Roadmap, group by **Platform**

---

## Step 4 — Built-in project workflows

Project **⋯** menu → **Workflows**:

| Workflow | Action |
|----------|--------|
| Item added to project | Set Status → **Backlog** |
| Pull request merged | Set Status → **Done** |
| Item closed | Set Status → **Done** |
| Auto-add to project | Repository: `mitf-dev-space/.github`, filter: label `platform-health` |

Repeat **Auto-add** for other repos as you onboard them.

---

## Step 5 — Bulk-add existing issues

1. Open project → **Add item** → **Add item from repository**
2. Select `mitf-dev-space/.github`
3. Select all issues with label `platform-health`
4. Set **Health** / **Priority** on each row in Table view

---

## Step 6 — Save as org template (optional)

Project **⋯** → **Settings** → **Make template** → On

Org owners can recommend it under **Organization settings → Projects → Customize recommended templates**.

---

## Weekly routine

| When | View | Action |
|------|------|--------|
| Monday | Platform health table | Review Red / P0 items |
| Daily | Active work board | WIP limit ~3 per person |
| Friday | All | Mark Done, archive completed |
| Quarterly | + ACCESS_REVIEW.md | Access audit |

---

## Enable API automation (optional, for Cursor agent)

Run once on your machine so the agent can manage the project via API:

```bash
gh auth refresh -h github.com -s project,read:project
```

Enter the device code when prompted.

---

## Tracker issues

All seed work items live here: https://github.com/mitf-dev-space/.github/issues?q=label%3Aplatform-health
