# Pinjai — Record of Processing Activities (ROPA), PDPA s.39

**Version 0.1 · 14 Nov 2026 · internal (excluded from Pages).** Not legal advice; the owner should have a Thai lawyer confirm it before launch.

Source of truth for facts: [privacy policy](../privacy/en/index.md), [store privacy labels](store-privacy-labels.md), [app review notes](app-review-notes.md). If a fact changes, update the policy first (policy-sync-pr), then this record.

**Do we have to keep this?** The 2024 PDPC notice on small businesses (ประกาศ คปช. เรื่อง การยกเว้นการบันทึกรายการของผู้ควบคุมข้อมูลส่วนบุคคลซึ่งเป็นกิจการขนาดเล็ก พ.ศ. 2567) may exempt a controller who is an individual from most s.39 items, but not if there's a high-risk activity or a DPO duty. Pinjai processes precise location and has no DPO decision yet, so **we keep the full record anyway**. It's cheap and it's what PDPC asks for first after a complaint or breach. Open item: owner/lawyer to confirm whether the exemption applies (and whether s.41 DPO is needed).

## 1. Controller (s.39(3))
| Item | Value |
|---|---|
| Controller | Pattarapon Bunchuai (individual), operating the Pinjai app (bundle `com.pinjai.app`) |
| Contact | support@pinjai.com |
| DPO | None appointed (open item above) |
| Representative outside Thailand | Not applicable (controller is in Thailand) |

## 2. Processing activities (s.39(1), (2), (4))
| # | Activity | Data subjects | Personal data | Purpose | Legal basis | Recipients / processors | Transfer outside TH | Retention |
|---|---|---|---|---|---|---|---|---|
| A1 | Account and sign-in | App users (13+) | Name, email, sign-in method (Apple/Google), Google profile photo if any, user ID | Create and secure the account | Contract, s.24(3) | Supabase (auth, DB); Apple / Google (sign-in the user starts) | Supabase Singapore; Apple/Google per their terms | While the account is active; deleted within 30 days of account deletion; backups overwritten within 7 days |
| A2 | Trips and plans | App users; people the user names in notes (incidental) | Trip names, destinations, dates, accommodation, stops, notes, Arrived/Skip status and time (no coordinates) | Plan and run trips | Contract, s.24(3) | Supabase | Singapore | Same as A1 |
| A3 | Stop places | App users | Google `place_id`, stop coordinates (no Google place names stored) | Show stops and calculate routes | Contract, s.24(3) | Supabase; Google Maps Platform | Singapore; Google (US and other) | Coordinates refreshed or purged within 30 days (`coords_fetched_at`); `place_id` with the trip |
| A4 | Place search | App users | Search text, search area | Find places | Contract, s.24(3) | Google Places via our Edge Function | Google (US and other) | Not stored on our server; last 8 searches kept **only on the device**, cleared in Search, at sign-out and at account deletion |
| A5 | Live location on a trip day | App users who allow When In Use | Precise or approximate current position | Show the user on today's route; travel time to next stop | Contract, s.24(3); user can refuse and the trip still works | Google Routes via our Edge Function | Google (US and other) | **Not stored or logged.** Sent only at Start Day, Arrived/Skip and Refresh, while the day is on screen. No background location |
| A6 | Crash and error reports | App users | Device model, OS and app version, error details; no location, no email | Fix bugs | Legitimate interest, s.24(5) | Sentry | Sentry region: **to confirm** (US or EU) | Up to 30 days |
| A7 | Support and rights requests | Users and anyone who emails us | Email address, message, account ID if given | Answer questions and PDPA requests | Legal obligation s.24(6) (rights requests); legitimate interest s.24(5) (support) | Email provider: **to confirm** | **To confirm** | **To set:** suggest 1 year after the request is closed |
| A8 | Account deletion on the web | Users | Email, account ID | Honour deletion | Legal obligation, s.24(6) | Supabase | Singapore | Request log kept 1 year as proof (**to confirm**) |
| A9 | Google Play closed test | Testers who sign up | Google account email only | Run the Play closed test required for production access | Consent, s.19 | Google Play | Google (US and other) | Until production access is granted + 30 days, then deleted |

Not processed: sensitive data under s.26, advertising IDs, tracking across apps, sale of data, background location, location history.

Cross-border (s.28–29): providers with adequate safeguards and contract terms (Supabase DPA, Google Maps Platform terms, Sentry DPA). **Open item:** owner keeps a copy or link of each accepted DPA.

## 3. Data subject rights (s.39(5))
Access, copy, portability, objection, deletion, restriction, correction and withdrawal of consent, by email to support@pinjai.com; deletion also in the app (Profile › Delete account) and on the web delete-account page. Target: answer within 30 days (s.30 sets 30 days for access requests).

## 4. Use or disclosure without consent (s.39(6), s.27 para 3)
None so far. Log any disclosure to an authority here (date, requester, legal basis, data).

## 5. Refused requests (s.39(7))
None so far. Log each refusal under s.30 para 3, s.31 para 3, s.32 para 3 or s.36 para 1 here (date, request, reason).

## 6. Security measures (s.39(8), s.37(1))
- TLS in transit; Supabase encryption at rest.
- Row Level Security: each user reads and writes only their own rows.
- Server-side Google keys only in Supabase secrets; app keys restricted by bundle ID; no keys in git.
- No location or email in logs or Sentry; location not logged with the user ID.
- Least-privilege access: only the owner has production access; 2FA on Supabase, Google Cloud, Sentry, GitHub, Apple and Google developer accounts (**owner to confirm**).
- Breach handling: [breach-response.md](breach-response.md).

## 7. Review
Review this record whenever a policy-sync PR changes data, processors or retention, and at least every 6 months. Change log:
- 0.1 (14 Nov 2026): first draft.
