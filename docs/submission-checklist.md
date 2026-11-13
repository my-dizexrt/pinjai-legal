# Pinjai — Store submission checklist

**Version 0.1 · 14 Nov 2026 · internal (excluded from Pages).** Not legal advice. Every field that has to be filled in when submitting to App Store Connect and Google Play Console, with where its value comes from.

Status: ✅ ready (value is in the repo) · 🟡 waiting on the team (build or screenshots) · 🔴 **waiting on the owner** (only the owner can do it; ask through PM).

Sources: [store-listing.md](store-listing.md) (listing text and URLs), [store-privacy-labels.md](store-privacy-labels.md) (App Privacy / Data safety), [store-submission-answers.md](store-submission-answers.md) (age rating, export, IARC, audience), [app-review-notes.md](app-review-notes.md) (review notes), [ropa.md](ropa.md).

## ⚠️ Timeline risk: Google Play closed test (owner)
If the Play developer account is a **personal account created after 13 Nov 2023**, Play requires a **closed test with at least 12 testers opted in continuously for 14 days** before production access, and Google's review of the access request "usually takes seven days or less" ([Play Console Help](https://support.google.com/googleplay/android-developer/answer/14151465)). For a 21 Dec submission, the closed test should **start by about 30 Nov** with 12+ testers (recruit a few spare). Organization accounts are exempt.

## 0. Accounts and owner facts (🔴 owner)
| # | Item | Status | Notes |
|---|---|---|---|
| 0.1 | Apple Developer Program membership (individual or organization) | 🔴 | Annual fee, paid by the owner (the team can't spend money). The seller name shown on the App Store is the legal name for an individual account |
| 0.2 | Google Play developer account + identity verification | 🔴 | One-time fee, paid by the owner. Account type (personal/organization) decides the closed-test rule above |
| 0.3 | Data controller name in the policy = legal name used on the accounts | 🔴 confirm | Policy §1 says **Pattarapon Bunchuai**; owner confirms it matches the account/seller name |
| 0.4 | Contact email | ✅ | `support@pinjai.com` (works, confirmed 12 Nov) |
| 0.5 | App Review contact (first/last name, phone, email) | 🔴 | Apple App Review Information; private, not shown to users |
| 0.6 | Countries/regions to release in | 🔴 decision | Thailand only, or more. **If the EU is included**, Apple's trader status (DSA) needs a decision, and a trader's address/phone are shown publicly |
| 0.7 | Price | ✅ | Free, no in-app purchases |
| 0.8 | Accept the Google Maps Platform terms and keep the DPAs (Supabase, Sentry) | 🔴 | ROPA open item |
| 0.9 | Closed-test testers (12+ Google accounts) | 🔴 | See timeline risk |

## 1. Apple — App Store Connect
| # | Field | Status | Value / source |
|---|---|---|---|
| A1 | Bundle ID | ✅ | `com.pinjai.app` |
| A2 | App name / subtitle (TH, EN) | ✅ | store-listing.md |
| A3 | Primary / secondary category | 🟡 PM | Suggest Travel / Navigation (not decided in the repo yet) |
| A4 | Promotional text, description, keywords (TH, EN) | ✅ | store-listing.md v0.2.6 (counts pass) |
| A5 | Support URL | ✅ | `https://my-dizexrt.github.io/pinjai-legal/faq/` |
| A6 | Marketing URL | ✅ | Optional, leave blank |
| A7 | Privacy policy URL (TH / EN locale) | ✅ | `/privacy/th/` · `/privacy/en/` |
| A8 | Copyright | 🔴 confirm | e.g. "2026 Pattarapon Bunchuai" (owner confirms the name) |
| A9 | App Privacy (data types, linked, tracking) | ✅ | store-privacy-labels.md v0.3 |
| A10 | Age rating | ✅ | 4+ (PM decision 14 Nov) |
| A11 | Content rights | ✅ | Yes, third-party content; Yes, rights (GMP terms) |
| A12 | Export compliance | ✅ | Standard encryption only; `ITSAppUsesNonExemptEncryption: false` |
| A13 | Screenshots (iPhone 6.9" set; no iPad, `supportsTablet: false`) | 🟡 Designer | store-screenshots skill, TH/EN |
| A14 | App icon | ✅ | in the build |
| A15 | Build (via EAS / TestFlight) | 🟡 SE | release build |
| A16 | **Sign-in required → demo account for review** | 🟡 SE + 🔴 owner | Sign-in with Apple/Google only, so review needs a working path: a reviewer account or a demo mode. Put the details in Sign-in information (not in Notes). Decide once real auth lands |
| A17 | Review notes | ✅ draft | app-review-notes.md (open items: menu labels, 7-day backup sentence) |
| A18 | Account deletion in the app | 🟡 SE | Required by 5.1.1(v); check on the real-auth build |
| A19 | Version / "What's New" | 🟡 PM | First version: not needed |

## 2. Google Play — Play Console
| # | Field | Status | Value / source |
|---|---|---|---|
| G1 | Package name | ✅ | `com.pinjai.app` |
| G2 | App name, short description, full description (TH, EN) | ✅ | store-listing.md |
| G3 | App icon 512×512, feature graphic 1024×500 | 🟡 Designer | Feature graphic not made yet |
| G4 | Phone screenshots | 🟡 Designer | store-screenshots skill |
| G5 | App category | 🟡 PM | Suggest Travel & Local |
| G6 | Store contact email / website | ✅ | `support@pinjai.com` · website optional (FAQ URL can be used) |
| G7 | Privacy policy URL (single) | ✅ | `/privacy/en/` (links to TH at the top) |
| G8 | Ads | ✅ | No ads |
| G9 | App access | 🟡 SE + 🔴 owner | Same as A16: give reviewer access instructions |
| G10 | Content rating (IARC) | ✅ | store-submission-answers.md |
| G11 | Target audience | ✅ | 13–15, 16–17, 18+; not appealing to children |
| G12 | Data safety | ✅ | store-privacy-labels.md v0.3 |
| G13 | Account deletion URL (Data safety) | ✅ | `/delete-account/` |
| G14 | News / government / financial / health / COVID-19 declarations | ✅ | No / none |
| G15 | Location permissions declaration | ✅ | Should not appear; ST-AND-07 `bundletool dump manifest` on the release AAB (`aapt2` can't read an AAB) |
| G16 | Release AAB, signed by Play App Signing | 🟡 SE | |
| G17 | Closed test 12+ testers × 14 days, then apply for production | 🔴 | Timeline risk above; plan in [play-closed-test-plan.md](play-closed-test-plan.md) |
| G18 | Countries | 🔴 | Same as 0.6 |

## 3. Final checks before pressing Submit
- Run the live-page check: policy TH/EN, FAQ and delete-account all 200; `/docs/*` 404.
- The store text, privacy answers and policy say the same thing (policy-sync-pr if anything changed).
- Re-run `count-listing.py` if the listing changed.
- If any Phase 2 feature is in the build (Shared, posting, sharing location with friends, ads, an in-app browser), stop: privacy labels, age rating, IARC and policy must be redone first.
