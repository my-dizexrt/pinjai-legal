## What changed and why

<!-- Which page, which section, and the decision or ticket behind it -->

## Pages affected

- [ ] privacy/th/
- [ ] privacy/en/
- [ ] delete-account/
- [ ] faq/
- [ ] other:

## Checklist (author)

- [ ] TH and EN changed together; same sections, tables and rows in both languages
- [ ] Every table, list and code block has a blank line before it (including right after a `##` heading); table separator rows use ASCII `|---|`
- [ ] No unfilled placeholder (`[CONTROLLER_NAME]` style), no old name (TravelHub), and every contact email is support@pinjai.com
- [ ] Effective / updated date changed if the policy content changed
- [ ] If data collected, processors, retention or sign-in changed: the fact comes from `docs/decisions.md` (or a written decision), and the Apple App Privacy / Google Play Data safety answers are flagged for update

## QA (reviewer)

- [ ] Read the whole file, not only the diff
- [ ] Checked the **rendered** page, not only the source (Jekyll/kramdown or container). If only `gh api markdown -f mode=gfm` is possible: note GFM accepts tables without a blank line, so also run the blank-line lint
- [ ] If kramdown render wasn't possible before merge: comment says **conditional pass, not done until QA's live-page-check**
- [ ] After merge and Pages deploy, live check by QA:
  - [ ] number of tables in source (`^|---`) = number of `<table` in the HTML
  - [ ] no Markdown leaked into page text (`|`, `|—|`, `**`, leading `#`)
  - [ ] TH and EN have the same number of tables, rows (`<tr`) and headings (`<h2`)
  - [ ] all URLs return 200 and cross-page links work
  - [ ] numbers posted in the PR and in the team room
