#!/usr/bin/env python3
"""Generate store-listing.md and a character-count table.

Thai and English are counted by Unicode code points (Python 3 len(str),
equivalent to JS [...str].length). Combining Thai vowels and tone marks
each count as one code point. This is not grapheme-cluster counting and
not UTF-16 code units.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

OUT = Path(__file__).resolve().parent / "store-listing.md"

# ── Limits ──────────────────────────────────────────────────────────
LIMITS = {
    "app_name": 30,
    "subtitle": 30,
    "promotional": 170,
    "description": 4000,
    "keywords": 100,
    "play_title": 30,
    "play_short": 80,
    "play_full": 4000,
}

# ── Copy ────────────────────────────────────────────────────────────
EN_APP_NAME = "Pinjai"
TH_APP_NAME = "Pinjai"  # store title is Latin in every country (AGENTS.md)

EN_SUBTITLE = "Plan your trip, then follow it"
TH_SUBTITLE = "พินใจ วางแผนทริป เที่ยวตามแผน"

EN_PROMO = (
    "Plan every day of your trip, then follow it on the road. "
    "Trip-day location only while the app is open. "
    "Not stored, not shared with friends, not tracked in the background."
)
TH_PROMO = (
    "วางแผนทุกวันของทริป แล้วเที่ยวตามแผนได้เลย "
    "ใช้ตำแหน่งเฉพาะระหว่างวันเดินทางตอนที่เปิดแอป "
    "ไม่เก็บตำแหน่ง ไม่แชร์ให้เพื่อน และไม่ติดตามตำแหน่งเบื้องหลัง"
)

EN_PLAY_SHORT = "Plan every day of your trip, then follow it on the road."
TH_PLAY_SHORT = "วางแผนทุกวันของทริป แล้วเที่ยวตามแผนได้เลย"

EN_KEYWORDS = (
    "trip,planner,itinerary,travel,thailand,route,vacation,roadtrip,"
    "places,tour,holiday,map,stops,driving"
)
TH_KEYWORDS = (
    "วางแผนทริป,ทริป,เที่ยว,แผนเที่ยว,จุดแวะ,เส้นทาง,ท่องเที่ยว,"
    "แผนที่,เที่ยวไทย,จัดทริป,คาเฟ่,ที่เที่ยว"
)

EN_DESCRIPTION = """\
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
Thai and English."""

TH_DESCRIPTION = """\
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
ไทยและอังกฤษ"""

# Play full description is the same as the App Store description in each language.
EN_PLAY_FULL = EN_DESCRIPTION
TH_PLAY_FULL = TH_DESCRIPTION

FIELDS = [
    # locale, store, field_key, label, value, limit_key
    ("EN", "App Store", "app_name", "App name", EN_APP_NAME, "app_name"),
    ("EN", "App Store", "subtitle", "Subtitle", EN_SUBTITLE, "subtitle"),
    ("EN", "App Store", "promotional", "Promotional text", EN_PROMO, "promotional"),
    ("EN", "App Store", "description", "Description", EN_DESCRIPTION, "description"),
    ("EN", "App Store", "keywords", "Keywords", EN_KEYWORDS, "keywords"),
    ("EN", "Google Play", "play_title", "Title", EN_APP_NAME, "play_title"),
    ("EN", "Google Play", "play_short", "Short description", EN_PLAY_SHORT, "play_short"),
    ("EN", "Google Play", "play_full", "Full description", EN_PLAY_FULL, "play_full"),
    ("TH", "App Store", "app_name", "App name", TH_APP_NAME, "app_name"),
    ("TH", "App Store", "subtitle", "Subtitle", TH_SUBTITLE, "subtitle"),
    ("TH", "App Store", "promotional", "Promotional text", TH_PROMO, "promotional"),
    ("TH", "App Store", "description", "Description", TH_DESCRIPTION, "description"),
    ("TH", "App Store", "keywords", "Keywords", TH_KEYWORDS, "keywords"),
    ("TH", "Google Play", "play_title", "Title", TH_APP_NAME, "play_title"),
    ("TH", "Google Play", "play_short", "Short description", TH_PLAY_SHORT, "play_short"),
    ("TH", "Google Play", "play_full", "Full description", TH_PLAY_FULL, "play_full"),
]


def codepoints(s: str) -> int:
    """Count Unicode code points (not grapheme clusters, not UTF-16 units)."""
    return len(s)


def fence(text: str) -> str:
    return "```\n" + text + "\n```"


def status(count: int, limit: int) -> str:
    return "Pass" if count <= limit else "FAIL"


def checks() -> list[str]:
    issues: list[str] = []
    for locale, store, key, label, value, limit_key in FIELDS:
        n = codepoints(value)
        lim = LIMITS[limit_key]
        if n > lim:
            issues.append(f"OVER LIMIT: {locale} {store} {label} is {n}/{lim}")
        if value != value.strip():
            issues.append(f"Leading/trailing whitespace: {locale} {store} {label}")

    for name, kw in (("EN", EN_KEYWORDS), ("TH", TH_KEYWORDS)):
        if re.search(r",\s", kw) or kw.startswith(",") or kw.endswith(","):
            issues.append(f"{name} keywords: comma spacing/format problem")
        if re.search(r"pinjai|พินใจ|travelhub", kw, re.I):
            issues.append(f"{name} keywords repeat the app name or old name")

    body = "\n".join(v for *_, v, _ in FIELDS)
    if re.search(r"ครับ|ค่ะ", body):
        issues.append("Found ครับ/ค่ะ in listing copy")
    if re.search(r"TravelHub", body):
        issues.append("Found TravelHub in listing copy")

    if EN_PLAY_FULL != EN_DESCRIPTION:
        issues.append("EN Play full description differs from App Store description")
    if TH_PLAY_FULL != TH_DESCRIPTION:
        issues.append("TH Play full description differs from App Store description")

    # Phase 2 / out-of-scope claim scan (marketing body only)
    marketing = "\n".join(
        [
            EN_SUBTITLE,
            EN_PROMO,
            EN_DESCRIPTION,
            EN_PLAY_SHORT,
            TH_SUBTITLE,
            TH_PROMO,
            TH_DESCRIPTION,
            TH_PLAY_SHORT,
        ]
    )
    forbidden = [
        (r"\bemail (sign[ -]?in|login|log in)\b", "email sign-in"),
        (r"เข้าสู่ระบบด้วยอีเมล|เข้าสู่ระบบด้วยอีเมลล์", "email sign-in TH"),
        (r"\b(shared trips?|share a trip|invite friends|trip friends)\b", "shared trips"),
        (r"แท็บ Shared|ทริปร่วม|เชิญเพื่อน", "shared trips TH"),
        (r"\b(home feed|videos?|place posts?|social profile)\b", "Phase 2 social"),
        (r"ฟีด|คลิป|โพสต์|โปรไฟล์โซเชียล", "Phase 2 social TH"),
        (r"share (your )?location|share (an |your )?ETA|background tracking(?! is off)", "location sharing"),
        (r"แชร์ตำแหน่ง|แชร์ ETA|แชร์เวลาถึง|ติดตามเบื้องหลัง(?! ตำแหน่ง)", "location sharing TH"),
        (r"automatic check[ -]?in|auto check[ -]?in", "auto check-in"),
        (r"เช็กอินอัตโนมัติ", "auto check-in TH"),
        (r"photo upload|upload a (photo|cover)|cover photo", "photo covers"),
        (r"อัปโหลดรูป|รูปปก", "photo covers TH"),
        (r"\bAlways( Allow)? location\b|background location", "Always/background location"),
        (r"สิทธิ์ตลอดเวลา|(?<!ไม่ติดตาม)ตำแหน่งเบื้องหลัง", "Always/background TH"),
        (r"\bTerms of (Use|Service)\b", "Terms page"),
        (r"ข้อกำหนดการใช้งาน|เงื่อนไขการใช้งาน", "Terms page TH"),
        (r"\bweather\b|พยากรณ์อากาศ", "weather"),
    ]
    for pat, label in forbidden:
        if re.search(pat, marketing, re.I):
            issues.append(f"Possible out-of-scope claim ({label}): /{pat}/")

    th_location_off = "ถ้าปิดตำแหน่ง ก็ยังเที่ยวตามแผนและกด “ถึงแล้ว” เองในแต่ละจุดแวะได้"
    en_location_off = (
        "If location is off, you can still follow the plan and tap “Arrived” yourself at each stop."
    )
    if th_location_off not in TH_DESCRIPTION:
        issues.append("TH description is missing the exact P&C v0.2 location-off sentence")
    if "แผนเที่ยวยังใช้ได้ครบ" in TH_DESCRIPTION:
        issues.append("TH description still has the pre-v0.2 'แผนเที่ยวยังใช้ได้ครบ' wording")
    if en_location_off not in EN_DESCRIPTION:
        issues.append("EN description is missing the v0.2 location-off counterpart")

    if "updated when you start the day, arrive at a stop, or refresh" not in EN_DESCRIPTION.lower():
        issues.append("EN description is missing the bullet2Sub travel-time cadence")
    if "อัปเดตตอนเริ่มวัน ถึงจุดแวะ หรือกดรีเฟรช" not in TH_DESCRIPTION:
        issues.append("TH description is missing the bullet2Sub travel-time cadence")
    if "trip day screen" not in EN_DESCRIPTION:
        issues.append("EN description is missing 'trip day screen' (map.locationTripDayOnly)")
    if "หน้าวันเดินทาง" not in TH_DESCRIPTION:
        issues.append("TH description is missing 'หน้าวันเดินทาง' (map.locationTripDayOnly)")
    if "isn’t stored" not in EN_DESCRIPTION:
        issues.append("EN description should say location is not stored")
    if "ไม่เก็บตำแหน่ง" not in TH_DESCRIPTION:
        issues.append("TH description should say location is not stored")

    if "Powered by Google" in marketing:
        issues.append("Marketing copy still contains 'Powered by Google' (removed in v0.2)")
    for maps_name, blob in (
        ("EN description", EN_DESCRIPTION),
        ("TH description", TH_DESCRIPTION),
    ):
        if "Google Maps" not in blob or "Apple Maps" not in blob:
            issues.append(f"{maps_name} must keep the Google Maps / Apple Maps handoff sentence")

    if re.search(r"gmail\.com|support@|privacy/t[hn]/|ช่วยเหลือและความเป็นส่วนตัว|Support and privacy", marketing):
        issues.append("Support email, privacy URLs, or the Support and privacy section leaked into marketing copy")

    return issues


def build_md(issues: list[str]) -> str:
    rows = []
    for locale, store, _key, label, value, limit_key in FIELDS:
        n = codepoints(value)
        lim = LIMITS[limit_key]
        rows.append(
            f"| {locale} | {store} | {label} | {lim} | {n} | {lim - n} | {status(n, lim)} |"
        )
    table = "\n".join(
        [
            "| Locale | Store | Field | Limit | Count | Remaining | Status |",
            "| --- | --- | --- | ---: | ---: | ---: | --- |",
            *rows,
        ]
    )

    issue_block = (
        "All length, format, tone, and out-of-scope scans passed."
        if not issues
        else "Script flagged:\n" + "\n".join(f"- {i}" for i in issues)
    )

    return f"""# Pinjai (พินใจ) — Store listing copy v0.2.6

_Date: 14 Nov 2026 (14 พ.ย. 2569)._
_Changelog:_
- _v0.2.6 (14 Nov 2026): QA nits — changelog in newest-first order with a v0.2.4 entry; Account deletion URL is a Google Play Console field only (Apple requires in-app deletion); replace /workspace paths with repo-relative names._
- _v0.2.5 (14 Nov 2026): aligned location claims with Map decision (ก) and P&C copy v0.3.6 — location only during an in-progress trip day while the app is open, shown on the trip day screen, travel times update at Start Day / Arrived or Skip / Refresh, and the live location is not stored._
- _v0.2.4 (12 Nov 2026): imported baseline reviewed by P&C._
- _v0.2.3 (12 Nov 2026): Support URL /faq/ is live, so it changed from pending to ready._
- _v0.2.2 (12 Nov 2026): owner renamed everything to Pinjai (PM). Legal URLs move to `https://my-dizexrt.github.io/pinjai-legal/` (live once the owner renames the repo `my-dizexrt/pinjai-legal`; the old travelhub-legal links stop working then). Bundle ID / Android package is now `com.pinjai.app`. Listing text unchanged._
- _v0.2.1 (12 Nov 2026): support@pinjai.com confirmed working by PM; removed the Gmail fallback._
- _v0.2 (12 Nov 2026): Privacy & Compliance review — replaced the location-off sentence (exact TH wording; EN matched in meaning); moved the support email, privacy-policy URLs, and delete-account URL out of the descriptions into Store console fields; set the support email to support@pinjai.com with a 14 Dec 2026 fallback; added a pending Support URL (FAQ, due by 6 Dec 2026); removed “Powered by Google” from the listing and kept the Google Maps / Apple Maps handoff sentences._
- _v0.1 (12 Nov 2026): first draft of App Store and Google Play listing text in Thai and English, limited to MVP features._

Tone matches the in-app copy: friendly, plain, and simple, with no ครับ/ค่ะ. The store **name/title is Pinjai** (Latin) in both languages, per `AGENTS.md` (one Latin store name in every country; พินใจ is the name under the icon on Thai-language devices). Thai body copy uses **พินใจ**, matching `common.appName` in `th.ts`.

App Store and Google Play full descriptions are the same in each language. Counts below were computed by `count-listing.py`.

## Character counts

Counts use **Unicode code points** (Python 3 `len(str)`, same as JavaScript `[...str].length`). A Thai combining vowel or tone mark counts as its own code point. This is not grapheme-cluster counting and not UTF-16 code units.

{table}

{issue_block}

## English

### App Store

**App name** (≤30, subtitle-free)

{fence(EN_APP_NAME)}

**Subtitle** (≤30)

{fence(EN_SUBTITLE)}

**Promotional text** (≤170)

{fence(EN_PROMO)}

**Description** (≤4000)

{fence(EN_DESCRIPTION)}

**Keywords** (≤100; comma-separated, no spaces after commas, app name not repeated)

{fence(EN_KEYWORDS)}

### Google Play

**Title** (≤30)

{fence(EN_APP_NAME)}

**Short description** (≤80)

{fence(EN_PLAY_SHORT)}

**Full description** (≤4000)

Same as the English App Store description above.

## Thai

### App Store

**App name** (≤30, subtitle-free; Latin store name)

{fence(TH_APP_NAME)}

**Subtitle** (≤30)

{fence(TH_SUBTITLE)}

**Promotional text** (≤170)

{fence(TH_PROMO)}

**Description** (≤4000)

{fence(TH_DESCRIPTION)}

**Keywords** (≤100; comma-separated, no spaces after commas, app name not repeated)

{fence(TH_KEYWORDS)}

### Google Play

**Title** (≤30)

{fence(TH_APP_NAME)}

**Short description** (≤80)

{fence(TH_PLAY_SHORT)}

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
| Account deletion URL | https://my-dizexrt.github.io/pinjai-legal/delete-account/ | Google Play Console field only (Data safety form, account-deletion web resource). App Store Connect has no such field — Apple requires in-app deletion (guideline 5.1.1(v)); the URL may be mentioned in App Review notes (`docs/app-review-notes.md`). |
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
| Support email, privacy URLs, delete-account URL, Support URL | Not in the description. See Store console fields. Support email `support@pinjai.com` (P&C v0.2; confirmed working 12 Nov 2026, no fallback). Privacy URLs from v0.3.3 / `AGENTS.md` / `docs/decisions.md`; App Store uses a URL per locale, Play uses the English URL (it links to Thai at the top). Delete-account URL: `.../delete-account/` (Google Play Console field only; see Store console fields). Support URL `.../faq/` is ready (live since 12 Nov 2026, v0.2.3). |
| Store name is the Latin “Pinjai” in every country | `AGENTS.md` rename checklist: “The store name and the Sign in with Apple name use one Latin name in every country; the Thai name is only the name under the icon on Thai-language devices.” |
| No Terms of Use in the listing | `docs/decisions.md` 2026-11-12: no Terms page; Apple’s standard EULA; i18n README |
| Trip covers are colour/gradient only | **Not claimed in the listing.** Source: `tripForm.cover` (“Cover color” / “สีปก”); `docs/decisions.md` (“No photo uploads and no trip cover upload. Trip covers use preset colors.”); i18n README open question 7. The clickable prototype still shows photo covers and an Upload control — that is out of date; the listing follows the later decision. |
| Bundle ID / Android package `com.pinjai.app` (was `com.pattarapon.travelhub`; PM, 12 Nov 2026) | PM room decision 12 Nov 2026; SE records it in `docs/decisions.md` — not mentioned in listing text (users don’t need it) |

### Deliberately not claimed

These appear in older requirements, the prototype, or Phase 2, and are left out of the listing:

- Email sign-in (still mentioned in the app repo’s `REQUIREMENTS.md` Auth row; superseded on 11 Nov 2026)
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
- **The app repo’s `REQUIREMENTS.md` has been behind later PM decisions** (email auth, Shared tab). This draft follows `docs/decisions.md` and `REQUIREMENTS.md` in the app repo (MVP Must features are unchanged), Map decision (ก), the i18n handoff, and P&C copy v0.3.6.

### Open questions for Privacy & Compliance and the Project Manager

1. **PM — store title in the Thai locale.** This draft uses **Pinjai** as the App Store name and Play title in both languages, per `AGENTS.md`. Please confirm that App Store Connect / Play Console should not localise the title to พินใจ. Thai screenshots and body copy will still say พินใจ, and the name under the icon on Thai-language devices is already พินใจ.
2. **PM — support email.** Resolved 12 Nov 2026: `support@pinjai.com` is live; the Gmail fallback is dropped.
3. **P&C — English location-off sentence.** The Thai line is the exact wording from the v0.2 review. The English counterpart is: If location is off, you can still follow the plan and tap “Arrived” yourself at each stop. Please confirm that wording if you want a verbatim check. This is not legal advice.
4. **P&C — Support URL.** Done: `https://my-dizexrt.github.io/pinjai-legal/faq/` is live (12 Nov 2026) and checked by QA.
5. **PM — Apple standard EULA.** There is no Terms URL in this copy. Store Connect should be set to Apple’s standard EULA, per the 12 Nov 2026 decision.

v0.2.6 keeps the P&C decisions on privacy URLs (App Store per locale; Play uses the English URL), removing “Powered by Google” from the listing, and moving support/privacy/deletion out of the description. Software Engineer / PM can paste the fields into App Store Connect and Play Console (submission is 21 Dec 2026).
"""


def main() -> int:
    issues = checks()
    OUT.write_text(build_md(issues), encoding="utf-8")
    print(f"Wrote {OUT}")
    print()
    print(f"{'Locale':<4} {'Store':<12} {'Field':<22} {'Limit':>5} {'Count':>5} {'Left':>5} {'Status'}")
    for locale, store, _key, label, value, limit_key in FIELDS:
        n = codepoints(value)
        lim = LIMITS[limit_key]
        print(f"{locale:<4} {store:<12} {label:<22} {lim:>5} {n:>5} {lim - n:>5} {status(n, lim)}")
    if issues:
        print("\nFLAGS:")
        for i in issues:
            print(" -", i)
        return 1
    print("\nAll checks passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
