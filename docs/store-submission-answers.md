# Pinjai — Store submission answers (non-privacy forms)

**Version 0.1 · 14 Nov 2026 · internal (excluded from Pages).** Not legal advice. Privacy forms (App Privacy, Data safety) are in [store-privacy-labels.md](store-privacy-labels.md); review notes and the location declaration are in [app-review-notes.md](app-review-notes.md).

Facts checked against `my-dizexrt/pinjai` main (`apps/mobile/app.config.ts`, `REQUIREMENTS.md`) on 14 Nov 2026. **Re-check before submission (21 Dec)** if a feature on the "MVP facts" list changes.

## MVP facts these answers rely on
- No ads, no ad SDK, no in-app purchases or subscriptions, no gambling or cash rewards.
- No chat or messaging, no social feed, no Shared tab; notes and trips are private to the user (Shared and posting are Phase 2).
- No in-app web browser: external links (partner, Directions, legal pages) open with the system `Linking.openURL`, outside the app.
- Third-party content shown: Google Places data (name, rating, opening hours, photos) and Google Maps tiles, under the Google Maps Platform terms. No Google review text.
- Location: When In Use only, never shared with other users (see policy §2).
- Encryption: HTTPS/TLS only via the OS and standard libraries; no custom or proprietary crypto. `ITSAppUsesNonExemptEncryption: false` is already in `app.config.ts`.
- Intended users: 13 and over (policy §7, `REQUIREMENTS.md`); age isn't collected.

## Apple — App Store Connect

### Age rating (current questionnaire: in-app controls, capabilities, mature themes, medical/wellness, sexuality/nudity, violence, chance-based activities)
| Section | Answer | Why |
|---|---|---|
| Parental controls | No | None in the app |
| Age assurance | No | We don't check age |
| Unrestricted web access | **No** | No embedded browser; links leave the app |
| User-generated content | No | Trips and notes aren't distributed to other users |
| Social media / Messaging and chat | No | Not in MVP |
| Advertising | No | No ads |
| Mature themes (profanity, horror, alcohol/tobacco/drug references) | None | Travel content we write has none. Google place names/photos (for example a bar) are third-party listings, not our themes; answer None |
| Medical or wellness | None | |
| Sexuality or nudity | None | |
| Violence (all types) | None | |
| Gambling, simulated gambling, contests, loot boxes | No / None | |

**Expected result: 4+.** The app is still meant for 13+ users (policy). Apple's rating describes content, so 4+ doesn't contradict the policy. **Decided (PM, 14 Nov 2026): use the calculated 4+.** Reason: Apple's age rating describes the app's content, which has nothing that needs a higher rating, so honest answers give 4+. The 13+ minimum stays in the privacy policy (§7) as who the service is for. The two don't conflict, so nothing in the policy changes.

### Export compliance (encryption)
- "Does your app use encryption?" — **Yes**, only standard encryption (HTTPS/TLS through the OS) that qualifies for the exemption. Because `ITSAppUsesNonExemptEncryption` is `false` in the build, App Store Connect normally won't ask per build.
- No export compliance documents or French declaration are needed for this case.
- If someone adds a crypto library or custom encryption, this answer has to be reviewed again.

### Content rights
- "Does your app contain, show, or access third-party content?" — **Yes.**
- "Do you have all necessary rights?" — **Yes**: Google Places and Maps content under the Google Maps Platform Terms, with the required Google attribution shown (Powered by Google and photo credits, per `REQUIREMENTS.md`). Our own icons and images are ours; store screenshots follow the store-screenshots skill (no unlicensed photos).

## Google Play — Play Console › App content

### Content rating (IARC)
| Item | Answer |
|---|---|
| Category | **All Other App Types** (not a game, not Social/Communication) |
| Contact email | support@pinjai.com |
| Violence, sexuality, language, controlled substances, crude humour | No |
| Users interact or exchange content (chat, media, voice) | **No** |
| Shares the user's current location with other users | **No** |
| Online content / promotes age-restricted products | No. Partner booking links are travel services, not age-restricted products |
| Digital purchases | No |
| Cash rewards, gift cards | No |
| Web browser or search engine | No. Place search is inside our own feature, not a general web search |
| News or educational app | No |

**Expected result:** lowest ratings (for example IARC 3+ / PEGI 3 / ESRB Everyone).

### Target audience and content
- Age groups: **13–15, 16–17, 18 and over** (not under 13, so the Families policy doesn't apply). This matches policy §7.
- "Could the app unintentionally appeal to children?" — **No** (no cartoon characters, games or child-focused themes).
- Teacher Approved — don't include.

### Other App content declarations (short)
| Declaration | Answer |
|---|---|
| Ads | No, the app has no ads |
| App access | Sign-in required. Give reviewer access as in [app-review-notes.md](app-review-notes.md) (**open item:** reviewer account or demo sign-in once real auth lands) |
| News app | No |
| Government app | No |
| Financial features | None |
| Health | None |
| COVID-19 contact tracing/status | Not this kind of app |
| Location permissions declaration | Should not appear (no background location); see app-review-notes |
| Data safety | See store-privacy-labels.md |

## Open items
1. ~~4+ or 13+ on Apple~~: decided 4+ (PM, 14 Nov 2026).
2. Reviewer sign-in method for Apple and Play once real auth is built.
3. If any Phase 2 feature ships (Shared, posting, sharing location with friends, an in-app browser, ads), redo the age rating, IARC and target audience: chat/UGC/location sharing change these answers. Note that `REQUIREMENTS.md` plans to limit location sharing and posting to 20+.
4. Owner enters these in the consoles. Console wording may change, so match each answer by meaning and flag anything new to P&C.

Sources: [Apple age ratings values and definitions](https://developer.apple.com/help/app-store-connect/reference/app-information/age-ratings-values-and-definitions/), [Apple: set an app age rating](https://developer.apple.com/help/app-store-connect/manage-app-information/set-an-app-age-rating/), [Apple: export compliance overview](https://developer.apple.com/help/app-store-connect/manage-app-information/overview-of-export-compliance/), [Play Console Help: content ratings](https://support.google.com/googleplay/android-developer/answer/9898843), [Play Console Help: target audience and content](https://support.google.com/googleplay/android-developer/answer/9867159).
