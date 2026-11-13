# Pinjai (พินใจ) — Store listing copy v0.2.5

_Date: 14 Nov 2026 (14 พ.ย. 2569)._
_Changelog:_
- _v0.2.5 (14 Nov 2026): aligned location claims with Map decision (ก) and P&C copy v0.3.6 — location only during an in-progress trip day while the app is open, shown on the trip day screen, travel times update at Start Day / Arrived or Skip / Refresh, and the live location is not stored._
- _v0.2 (12 Nov 2026): Privacy & Compliance review — replaced the location-off sentence (exact TH wording; EN matched in meaning); moved the support email, privacy-policy URLs, and delete-account URL out of the descriptions into Store console fields; set the support email to support@pinjai.com with a 14 Dec 2026 fallback; added a pending Support URL (FAQ, due by 6 Dec 2026); removed “Powered by Google” from the listing and kept the Google Maps / Apple Maps handoff sentences._
- _v0.2.1 (12 Nov 2026): support@pinjai.com confirmed working by PM; removed the Gmail fallback._
- _v0.2.2 (12 Nov 2026): owner renamed everything to Pinjai (PM). Legal URLs move to `https://my-dizexrt.github.io/pinjai-legal/` (live once the owner renames the repo `my-dizexrt/pinjai-legal`; the old travelhub-legal links stop working then). Bundle ID / Android package is now `com.pinjai.app`. Listing text unchanged._
- _v0.2.3 (12 Nov 2026): Support URL /faq/ is live, so it changed from pending to ready._
- _v0.1 (12 Nov 2026): first draft of App Store and Google Play listing text in Thai and English, limited to MVP features._

Tone matches the in-app copy: friendly, plain, and simple, with no ครับ/ค่ะ. The store **name/title is Pinjai** (Latin) in both languages, per `AGENTS.md` (one Latin store name in every country; พินใจ is the name under the icon on Thai-language devices). Thai body copy uses **พินใจ**, matching `common.appName` in `th.ts`.

App Store and Google Play full descriptions are the same in each language. Counts below were computed by `count-listing.py`.

## Character counts

Counts use **Unicode code points** (Python 3 `len(str)`, same as JavaScript `[...str].length`). A Thai combining vowel or tone mark counts as its own code point. This is not grapheme-cluster counting and not UTF-16 code units.

| Locale | Store | Field | Limit | Count | Remaining | Status |
| --- | --- | --- | ---: | ---: | ---: | --- |
| EN | App Store | App name | 30 | 6 | 24 | Pass |
| EN | App Store | Subtitle | 30 | 30 | 0 | Pass |
| EN | App Store | Promotional text | 170 | 170 | 0 | Pass |
| EN | App Store | Description | 4000 | 1730 | 2270 | Pass |
| EN | App Store | Keywords | 100 | 100 | 0 | Pass |
| EN | Google Play | Title | 30 | 6 | 24 | Pass |
| EN | Google Play | Short description | 80 | 56 | 24 | Pass |
| EN | Google Play | Full description | 4000 | 1730 | 2270 | Pass |
| TH | App Store | App name | 30 | 6 | 24 | Pass |
| TH | App Store | Subtitle | 30 | 29 | 1 | Pass |
| TH | App Store | Promotional text | 170 | 150 | 20 | Pass |
| TH | App Store | Description | 4000 | 1371 | 2629 | Pass |
| TH | App Store | Keywords | 100 | 99 | 1 | Pass |
| TH | Google Play | Title | 30 | 6 | 24 | Pass |
| TH | Google Play | Short description | 80 | 42 | 38 | Pass |
| TH | Google Play | Full description | 4000 | 1371 | 2629 | Pass |

All length, format, tone, and out-of-scope scans passed.

## English

### App Store

**App name** (≤30, subtitle-free)

```
Pinjai
```

**Subtitle** (≤30)

```
Plan your trip, then follow it
```

**Promotional text** (≤170)

```
Plan every day of your trip, then follow it on the road. Trip-day location only while the app is open. Not stored, not shared with friends, not tracked in the background.
```

**Description** (≤4000)

```
Pinjai helps you plan every day of your trip, then follow that plan on the road.

Create a trip, search for places, and add them to a day. Reorder your stops, see driving times between them, and use Optimize route when a different order would save driving time. On a trip day, follow your plan stop by stop: see the next stop, see how long it takes to get there (updated when you start the day, arrive at a stop, or refresh), and tap Arrived when you get there. For turn-by-turn directions, open the stop in Google Maps or Apple Maps.

Plan your trip
• Create trips and add places or quick stops to each day
• Reorder stops by dragging, or use Optimize route to find a faster order
• See driving time and distance between stops
• Search for attractions, cafés, food, stays and more
• See your saved places on the map

On the road
• Start a day and follow your plan stop by stop
• See time to the next stop, updated when you start the day, arrive at a stop, or refresh
• Tap Arrived at each stop, or Skip if you move on
• Open Google Maps or Apple Maps for turn-by-turn directions
• If you’re running late, keep your times or shift later stops
• See a recap when the day is done

Your location
On a trip day, while the app is open, Pinjai uses your location to show where you are on the trip day screen and how long it takes to reach your next stop. Travel time updates when you start the day, arrive at a stop, or refresh. Your location isn’t stored, isn’t shared with friends, and isn’t tracked in the background. If location is off, you can still follow the plan and tap “Arrived” yourself at each stop.

Sign in and your account
Sign in with Apple or Google. You can delete your account in the app.

Languages
Thai and English.
```

**Keywords** (≤100; comma-separated, no spaces after commas, app name not repeated)

```
trip,planner,itinerary,travel,thailand,route,vacation,roadtrip,places,tour,holiday,map,stops,driving
```

### Google Play

**Title** (≤30)

```
Pinjai
```

**Short description** (≤80)

```
Plan every day of your trip, then follow it on the road.
```

**Full description** (≤4000)

Same as the English App Store description above.

## Thai

### App Store

**App name** (≤30, subtitle-free; Latin store name)

```
Pinjai
```

**Subtitle** (≤30)

```
พินใจ วางแผนทริป เที่ยวตามแผน
```

**Promotional text** (≤170)

```
วางแผนทุกวันของทริป แล้วเที่ยวตามแผนได้เลย ใช้ตำแหน่งเฉพาะระหว่างวันเดินทางตอนที่เปิดแอป ไม่เก็บตำแหน่ง ไม่แชร์ให้เพื่อน และไม่ติดตามตำแหน่งเบื้องหลัง
```

**Description** (≤4000)

```
พินใจช่วยให้วางแผนทุกวันของทริป แล้วเที่ยวตามแผนได้เลย

สร้างทริป ค้นหาสถานที่ แล้วเพิ่มลงทริปในแต่ละวัน จัดลำดับจุดแวะ ดูเวลาขับรถระหว่างจุดแวะ และใช้จัดลำดับอัตโนมัติเมื่อลำดับใหม่ช่วยลดเวลาขับรถ ในวันเดินทาง ทำตามแผนทีละจุดแวะ ดูจุดแวะถัดไป ดูว่าอีกนานแค่ไหนจะถึง (อัปเดตตอนเริ่มวัน ถึงจุดแวะ หรือกดรีเฟรช) และกด “ถึงแล้ว” เมื่อถึง หากต้องการนำทางทีละขั้น เปิดจุดแวะนั้นใน Google Maps หรือ Apple Maps

วางแผนทริป
• สร้างทริป แล้วเพิ่มสถานที่หรือจุดแวะสั้นในแต่ละวัน
• ลากเพื่อจัดลำดับจุดแวะ หรือใช้จัดลำดับอัตโนมัติเพื่อหาลำดับที่เร็วขึ้น
• ดูเวลาขับรถและระยะทางระหว่างจุดแวะ
• ค้นหาที่เที่ยว คาเฟ่ อาหาร ที่พัก และอื่น ๆ
• ดูสถานที่ที่บันทึกไว้บนแผนที่

ระหว่างทาง
• เริ่มวันแล้วเที่ยวตามแผนทีละจุดแวะ
• ดูเวลาถึงจุดแวะถัดไป อัปเดตตอนเริ่มวัน ถึงจุดแวะ หรือกดรีเฟรช
• กด “ถึงแล้ว” ในแต่ละจุดแวะ หรือกดข้ามถ้าไม่แวะ
• เปิด Google Maps หรือ Apple Maps เพื่อนำทางทีละขั้น
• ถ้าช้ากว่าแผน จะคงเวลาเดิมหรือเลื่อนจุดแวะที่เหลือได้
• ดูสรุปวันเมื่อวันนั้นเสร็จ

ตำแหน่งของคุณ
ในวันเดินทาง ขณะที่เปิดแอป พินใจใช้ตำแหน่งของคุณเพื่อแสดงว่าคุณอยู่ตรงไหนในหน้าวันเดินทาง และอีกนานแค่ไหนจะถึงจุดแวะถัดไป เวลาเดินทางอัปเดตตอนเริ่มวัน ถึงจุดแวะ หรือกดรีเฟรช โดยไม่เก็บตำแหน่ง ไม่แชร์ให้เพื่อน และไม่ติดตามตำแหน่งเบื้องหลัง ถ้าปิดตำแหน่ง ก็ยังเที่ยวตามแผนและกด “ถึงแล้ว” เองในแต่ละจุดแวะได้

เข้าสู่ระบบและบัญชี
เข้าสู่ระบบด้วย Apple หรือ Google และลบบัญชีได้ในแอป

ภาษา
ไทยและอังกฤษ
```

**Keywords** (≤100; comma-separated, no spaces after commas, app name not repeated)

```
วางแผนทริป,ทริป,เที่ยว,แผนเที่ยว,จุดแวะ,เส้นทาง,ท่องเที่ยว,แผนที่,เที่ยวไทย,จัดทริป,คาเฟ่,ที่เที่ยว
```

### Google Play

**Title** (≤30)

```
Pinjai
```

**Short description** (≤80)

```
วางแผนทุกวันของทริป แล้วเที่ยวตามแผนได้เลย
```

**Full description** (≤4000)

Same as the Thai App Store description above.

## Store console fields (not description)

These values go in App Store Connect and Google Play Console only. They are not part of the promotional text or the description, so they are not in the character-count table above.

| Field | Value | Notes |
| --- | --- | --- |
| Support email | `support@pinjai.com` | Use this address in both stores. Confirmed working by PM on 12 Nov 2026 (forwards to the owner's inbox); no fallback. |
| App Store Connect — privacy policy URL (Thai locale) | https://my-dizexrt.github.io/pinjai-legal/privacy/th/ | One URL per locale. |
| App Store Connect — privacy policy URL (English locale) | https://my-dizexrt.github.io/pinjai-legal/privacy/en/ | One URL per locale. |
| Google Play — privacy policy URL (single) | https://my-dizexrt.github.io/pinjai-legal/privacy/en/ | Play accepts one privacy URL. The English page links to the Thai policy at the top. |
| Account deletion URL | https://my-dizexrt.github.io/pinjai-legal/delete-account/ | For the Play Console and App Store Connect account-deletion fields. In-app deletion remains the user-facing path described in the listing. |
| Support URL | https://my-dizexrt.github.io/pinjai-legal/faq/ | **Ready.** Live since 12 Nov 2026 (P&C, pinjai-legal PR #11, `fb53f88`); QA live-page check passed: 200, 12 questions per language, `#en`/`#th` anchors and links all work. |

## TH/EN parity

Both languages make the same claims. Product terms follow the in-app glossary (trip / ทริป, stop / จุดแวะ, Add to Trip / เพิ่มลงทริป, Arrived / ถึงแล้ว, Optimize route / จัดลำดับอัตโนมัติ, quick stop / จุดแวะสั้น, Directions / นำทาง).

| # | Claim | EN | TH |
| ---: | --- | --- | --- |
| 1 | Tagline: plan every day, then follow the plan | Plan every day of your trip, then follow it on the road | วางแผนทุกวันของทริป แล้วเที่ยวตามแผนได้เลย |
| 2 | Create trips, search places, add them to a day | Yes | Yes (เพิ่มลงทริปในแต่ละวัน) |
| 3 | Reorder stops (drag) | Yes | Yes (ลากเพื่อจัดลำดับ) |
| 4 | Optimize route when a new order would save driving time | Optimize route | จัดลำดับอัตโนมัติ |
| 5 | Driving time and distance between stops | Yes (driving, not transit) | Yes (เวลาขับรถ) |
| 6 | Search: attractions, cafés, food, stays and more | Yes | Yes (ที่เที่ยว คาเฟ่ อาหาร ที่พัก) |
| 7 | Saved places on the map | Yes | Yes |
| 8 | Quick stops | Yes | Yes (จุดแวะสั้น) |
| 9 | Trip day: follow the plan stop by stop | Yes | Yes |
| 10 | Time to the next stop updates when you start the day, arrive at a stop, or refresh | Updated when you start the day, arrive at a stop, or refresh | อัปเดตตอนเริ่มวัน ถึงจุดแวะ หรือกดรีเฟรช |
| 11 | Tap Arrived; Skip | Arrived / Skip | “ถึงแล้ว” / ข้าม |
| 12 | Turn-by-turn is a handoff to Google or Apple Maps | Yes | Yes |
| 13 | Running late: keep times or shift later stops | Yes | Yes (คงเวลาเดิม / เลื่อนจุดแวะที่เหลือ) |
| 14 | Day recap (view only, not share) | See a recap | ดูสรุปวัน |
| 15 | Location: only on a trip day while the app is open; shown on the trip day screen; times update at Start Day / Arrived or Skip / Refresh; not stored; not shared with friends; not tracked in the background | Matches P&C copy v0.3.6 and decision (ก) | Same meaning (หน้าวันเดินทาง, ไม่เก็บตำแหน่ง, อัปเดตตอนเริ่มวัน ถึงจุดแวะ หรือกดรีเฟรช) |
| 16 | If location is off, you can still follow the plan and tap Arrived yourself at each stop | If location is off, you can still follow the plan and tap “Arrived” yourself at each stop. | ถ้าปิดตำแหน่ง ก็ยังเที่ยวตามแผนและกด “ถึงแล้ว” เองในแต่ละจุดแวะได้ (P&C v0.2, exact TH) |
| 17 | Sign in with Apple or Google only | Yes | Yes |
| 18 | Delete account in the app | Yes | Yes |
| 19 | Languages: Thai and English | Yes | Yes (ไทยและอังกฤษ) |
| 20 | Store name/title | Pinjai | Pinjai (body copy uses พินใจ) |

Support email, privacy-policy URLs, the delete-account URL, and the Support URL are not in the descriptions. They are listed once in Store console fields, so they are not rows in this table.

Intentional non-claim differences (not feature differences):

- EN keywords include `vacation` and `holiday` as short discovery terms. The Thai keyword budget went to longer script words (`วางแผนทริป`, `ที่เที่ยว`, `เที่ยวไทย`) instead of `วันหยุด`.
- The EN App Store subtitle is 30 code points; the TH subtitle is 29 and starts with “พินใจ” so Thai-script searches find the app (PM decision, 12 Nov).
- Promotional text and the Play short description do not list every feature; the full description does, on both sides.

## Notes: factual claims and sources

This is store marketing copy, not legal advice. v0.2.5 applies Map decision (ก) and P&C location copy v0.3.6. P&C owns `copy/location-permission-copy.md`; do not edit it from this listing.

| Claim in the listing | Source |
| --- | --- |
| Tagline / “plan every day of your trip, then follow it on the road” | `handoff/i18n/en.ts` and `th.ts` — `auth.tagline` |
| Create trips; My Trips (upcoming / past only — no Shared tab) | `en.ts`/`th.ts` `trips.*`, `tripForm.*`; i18n README “Phase 2 isn’t included (… Shared tab …)” |
| Search places and Add to Trip | `search.*`, `addToTrip.*`; `REQUIREMENTS.md` Search row (Google Places) |
| Quick stops | `addStop.*`; `REQUIREMENTS.md` trip-day row |
| Reorder by dragging | `reorder.*`; `REQUIREMENTS.md` Trip detail (“ลากเรียงลำดับ”) |
| Optimize route / จัดลำดับอัตโนมัติ, only when it would save driving time | `optimize.*` (`confirmBody`, `alreadyFastest`, `buttonSave`); `REQUIREMENTS.md` Routes API |
| Driving time and distance between stops | `units.byCar`, `tripDetail.summaryPlaces_*`; Routes API in `REQUIREMENTS.md` |
| Search categories (attractions, cafés, food, stays, and more) | `search.categories` (also Gas, Nature — covered by “and more”). “Powered by Google” stays in the in-app UI only; P&C v0.2 removed it from the store listing. |
| Map of saved places | `map.*`; `REQUIREMENTS.md` Map row |
| Trip-day mode, next stop, time to the next stop updated at Start Day, Arrived or Skip, and Refresh | `tripDay.*`; `permissions.explainer.bullet2` / `bullet2Sub` (“Updated when you start the day, arrive at a stop, or refresh.” / “อัปเดตตอนเริ่มวัน ถึงจุดแวะ หรือกดรีเฟรช”; Routes called once via Edge Function at Start Day, Arrived/Skip, or manual refresh — pinjai #40 / WS4 decision 4); `errors.noLocationForEta` |
| Tap Arrived / “ถึงแล้ว”; Skip; no automatic check-in | `tripDay.arrivedAt`, `tripDay.skip`, `tripDay.checkInManual`; `docs/decisions.md` (manual Arrived); `REQUIREMENTS.md` (เช็กอินอัตโนมัติ = Phase 2) |
| Turn-by-turn opens in Google Maps or Apple Maps (not in-app navigation) | `tripDay.navigateHint`, `navigation.openIn`; `REQUIREMENTS.md` (“สรุปก่อนออก → Google/Apple Maps”) |
| Running late: Keep times / Shift later stops | `tripDay.lateBody`, `keepTimes`, `shift`; `REQUIREMENTS.md` |
| Day recap is something you view, not share | `recap.*`; i18n README lists “Share recap” as Phase 2 |
| Location used only during an in-progress trip day while the app is open (foreground), shown on the trip day screen, not stored, not shared with friends, not tracked in the background | Map decision (ก); `map.locationTripDayOnly` (“Your location shows on the trip day screen.” / “ตำแหน่งของคุณจะแสดงในหน้าวันเดินทาง”); `copy/location-permission-copy.md` v0.3.6 §7; When-In-Use only (`AGENTS.md`, `REQUIREMENTS.md`). Live location is never stored; Routes is called through an Edge Function at Start Day, Arrived/Skip, or Refresh (app-review notes; store-privacy-labels). The published privacy policy and FAQ still say “only while the app is open” more broadly — listing follows (ก); P&C should review. |
| If location is off, you can still follow the plan and tap Arrived yourself at each stop | P&C review, 12 Nov 2026 (v0.2). The TH sentence is the exact wording they asked for. The EN sentence is the meaning match (it no longer says the plan “still works fully,” which was the older v0.3.3 denied-body phrase “แผนเที่ยวยังใช้ได้ครบ”). |
| Sign in with Apple or Google only (no email sign-in) | `auth.continueWithApple` / `continueWithGoogle`; `docs/decisions.md` 2026-11-11 (“This supersedes the earlier requirements line that listed email”); i18n README 12 Nov changelog; prototype `README.md` |
| Delete account in the app | `deleteAccount.*`; `docs/decisions.md` (in-app button is the primary path, Apple 5.1.1(v)); `REQUIREMENTS.md` |
| Thai and English | `handoff/i18n/*`; `AGENTS.md` |
| Support email, privacy URLs, delete-account URL, Support URL | Not in the description. See Store console fields. Support email `support@pinjai.com` (P&C v0.2; confirmed working 12 Nov 2026, no fallback). Privacy URLs from v0.3.3 / `AGENTS.md` / `docs/decisions.md`; App Store uses a URL per locale, Play uses the English URL (it links to Thai at the top). Delete-account URL: `.../delete-account/`. Support URL `.../faq/` is ready (live since 12 Nov 2026, v0.2.3). |
| Store name is the Latin “Pinjai” in every country | `AGENTS.md` rename checklist: “The store name and the Sign in with Apple name use one Latin name in every country; the Thai name is only the name under the icon on Thai-language devices.” |
| No Terms of Use in the listing | `docs/decisions.md` 2026-11-12: no Terms page; Apple’s standard EULA; i18n README |
| Trip covers are colour/gradient only | **Not claimed in the listing.** Source: `tripForm.cover` (“Cover color” / “สีปก”); `docs/decisions.md` (“No photo uploads and no trip cover upload. Trip covers use preset colors.”); i18n README open question 7. The clickable prototype still shows photo covers and an Upload control — that is out of date; the listing follows the later decision. |
| Bundle ID / Android package `com.pinjai.app` (was `com.pattarapon.travelhub`; PM, 12 Nov 2026) | PM room decision 12 Nov 2026; SE records it in `docs/decisions.md` — not mentioned in listing text (users don’t need it) |

### Deliberately not claimed

These appear in older requirements, the prototype, or Phase 2, and are left out of the listing:

- Email sign-in (still mentioned in `/workspace/travelhub/REQUIREMENTS.md` Auth row; superseded on 11 Nov 2026)
- Shared trips / Shared tab (Should in `REQUIREMENTS.md`; not in i18n; called out as Phase 2 in the i18n README)
- Place posts, social profiles, videos, a home feed, photo upload, share trip recap, share location or ETA, automatic check-in, Always / background location (`REQUIREMENTS.md` Phase 2; `docs/decisions.md`)
- In-app turn-by-turn navigation (the app hands off to Google or Apple Maps)
- Weather (i18n README: no weather API in the MVP)
- Offline mode as a selling point (`REQUIREMENTS.md` Should: cached trips; Must: “needs internet” message). i18n has `errors.offlineBody`, but this is not marketed here.
- A Terms of Use URL
- Support email, privacy-policy URLs, and the web delete-account URL in the marketing body (moved to Store console fields in v0.2)
- “Powered by Google” in the store listing (in-app attribution is unchanged; P&C v0.2)
- User location on the saved-places Map (decision (ก): that Map never reads or shows the user; location is shown on the trip day screen)
- Continuous or “live” location updates while the app is merely open (times update only at Start Day, Arrived/Skip, or Refresh)

### Claims I am less sure about

- **Colour vs gradient covers:** the brief says colour/gradient; `tripForm` and `docs/decisions.md` say preset colours. Covers are omitted from the listing, so this does not affect the copy.
- **“And more” on search categories:** i18n also has Gas and Nature, which `REQUIREMENTS.md` does not list in the Search row. “And more” covers them without naming them.
- **Travel-time wording:** times to the next stop update when you start the day, arrive at a stop, or refresh (`bullet2Sub`, WS4 decision 4), not continuously while the app is open. v0.2.5 states that cadence in the description.
- **`REQUIREMENTS.md` in `/workspace/travelhub` is behind later PM decisions** (email auth, Shared tab). This draft follows `docs/decisions.md`, `REQUIREMENTS.md` (MVP Must features are unchanged), Map decision (ก), the i18n handoff, and P&C copy v0.3.6.

### Open questions for Privacy & Compliance and the Project Manager

1. **PM — store title in the Thai locale.** This draft uses **Pinjai** as the App Store name and Play title in both languages, per `AGENTS.md`. Please confirm that App Store Connect / Play Console should not localise the title to พินใจ. Thai screenshots and body copy will still say พินใจ, and the name under the icon on Thai-language devices is already พินใจ.
2. **PM — support email.** Resolved 12 Nov 2026: `support@pinjai.com` is live; the Gmail fallback is dropped.
3. **P&C — English location-off sentence.** The Thai line is the exact wording from the v0.2 review. The English counterpart is: If location is off, you can still follow the plan and tap “Arrived” yourself at each stop. Please confirm that wording if you want a verbatim check. This is not legal advice.
4. **P&C — Support URL.** Done: `https://my-dizexrt.github.io/pinjai-legal/faq/` is live (12 Nov 2026) and checked by QA.
5. **PM — Apple standard EULA.** There is no Terms URL in this copy. Store Connect should be set to Apple’s standard EULA, per the 12 Nov 2026 decision.

v0.2.5 keeps the P&C decisions on privacy URLs (App Store per locale; Play uses the English URL), removing “Powered by Google” from the listing, and moving support/privacy/deletion out of the description. Software Engineer / PM can paste the fields into App Store Connect and Play Console (submission is 21 Dec 2026).
