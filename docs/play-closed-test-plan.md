# Pinjai — Google Play closed test plan

**Version 0.1 · 14 Nov 2026 · internal (excluded from Pages).** Not legal advice. Plan for getting Play **production access** in time to submit on **21 Dec 2026**.

Sources (Play Console Help, read 14 Nov 2026):
[testing requirements for new personal accounts](https://support.google.com/googleplay/android-developer/answer/14151465) ·
[device verification](https://support.google.com/googleplay/android-developer/answer/14316361) ·
[information to create an account](https://support.google.com/googleplay/android-developer/answer/13628312).
Google has changed these numbers before (20 testers until Dec 2024), so recheck the first link before starting.

## 1. Which rule applies (🔴 owner decides the account type)
The account type is picked when the account is created and **cannot be changed later**.

| | Personal account | Organization account |
|---|---|---|
| Closed test before production | **Required** if created after 13 Nov 2023: ≥ 12 testers opted in **continuously for the 14 days before you apply** | Not required |
| Device check | Verify a real Android phone with the Play Console app (no emulator) | Not required |
| Identity | Legal name and address checked through the Google payments profile | **D-U-N-S number** (free, can take **up to 30 days**), business registration document, organization address and phone |
| Shown on Google Play | Developer name and contact email (and more if the app is paid or has in-app purchases; Pinjai has neither) | Legal name, address, developer email and phone |
| Fits 21 Dec? | Yes, if the test starts by 30 Nov | Only if a D-U-N-S number already exists; a new one may take until mid-Dec |

**Suggestion:** a personal account plus the closed test below, unless the owner already has a registered business with a D-U-N-S number. Either way, the public developer name must match the data controller in the privacy policy (Pattarapon Bunchuai) or the policy must be updated.

## 2. Countdown from 21 Dec (personal account)
| Date (2026) | Step | Owner |
|---|---|---|
| By **20 Nov** | Create the Play developer account (one-time fee, paid by the owner), verify identity, verify the Android device | 🔴 owner |
| 20–25 Nov | Finish **app setup** in Play Console: store listing, privacy policy URL, Data safety, content rating, target audience, ads, app access, account deletion URL (values: [submission-checklist.md](submission-checklist.md) §2) | 🔴 owner fills, P&C gives values |
| 20–25 Nov | Collect **≥ 15 tester Google accounts** (12 plus 3 spare, because if one leaves the 14 days restart) | 🔴 owner + PM |
| By **27 Nov** | Upload a release AAB (real backend and sign-in, **not mock mode**; trip day and the location screens may not be in it yet) to the **closed testing** track, add the testers (email list or Google Group), send them the opt-in link. The closed track release is reviewed by Google first | SE (build) + 🔴 owner (upload) |
| By **30 Nov** | All testers **opted in** (the 14-day clock starts per tester at opt-in, not at invite) | testers |
| 30 Nov – 13 Dec | Testers use what the build has: sign-in, My Trips, Add to Trip, Search, map (Google checks engagement, not just the count). QA tester guide; collect feedback | QA + PM |
| 7–13 Dec, **as soon as it's ready** | Upload an updated build to the same closed track with workstream 4 (trip day, location permission; real build lands 7–13 Dec). It's reviewed by Google like the first one, so don't wait for 13 Dec. Testers stay opted in, so the 14 days keep counting | SE + 🔴 owner |
| 13–14 Dec | Testers try the trip day screen with location **allowed and denied**, and account deletion, so the production form has real feedback | testers + QA |
| **14 Dec** | Apply for production on the Dashboard: three sections, about the closed test, the app, and readiness | 🔴 owner, P&C drafts answers |
| 14–21 Dec | Google review, "usually 7 days or less" | Google |
| **21 Dec** | Submit the production release for review | 🔴 owner |

Slack is 0 days. If the opt-ins slip past 30 Nov, the Android launch moves day for day; iOS doesn't depend on this.

## 3. During the test
- Stay at **12 or more** testers the whole time. If it drops to 11, wait until it's back at 12, then count 14 days again.
- Updating the build during the test is fine; the testers stay opted in.
- Testers use the **real app and real backend**, so the published privacy policy applies to them as users. Don't use a test-only data flow.
- Trip day and location are tested only after the workstream 4 build (see §2). Invite text and tester notice: [closed-test-invite.md](closed-test-invite.md).
- Don't promise anything about the test in the store listing (it isn't public until production).

## 4. Tester data (PDPA)
The tester list (**Google account emails only**, no names) is personal data held by the controller. Logged as ROPA **A9**: basis is consent (they sign up), keep it only until production access is granted plus 30 days, then delete it, and don't share it outside the team and Google Play.

## 5. Waiting on the owner (ask through PM)
1. Personal or organization account (and whether a D-U-N-S number already exists).
2. Create the account, pay the fee, verify identity and device by 20 Nov.
3. Public developer name = data controller name in the policy.
4. Provide or recruit 15 tester Google accounts.
5. Upload the build and send the opt-in link by 27 Nov.
