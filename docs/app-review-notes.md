# Pinjai — App review notes (Apple) + Play location declaration + prominent disclosure check

_Owner: Privacy & Compliance. v0.1, 13 Nov 2026. Draft for the 21 Dec 2026 submission. Sources: app `apps/mobile/app.config.ts` on pinjai main (58e6294), `copy/location-permission-copy.md` v0.3.4, WS4 handoff round 2 (QA + P&C pass 13 Nov), privacy policy §2–3, `docs/store-privacy-labels.md` v0.3. Not legal advice. Kept off the public site (`docs/` is excluded from Pages)._

## 1. Apple — App Review Information › Notes

Paste the EN text into App Store Connect (reviewers read English). The TH text is for the team and for our own records. Keep it under 4,000 characters.

**EN**

> Pinjai is a trip planner for travelers in Thailand. Sign-in is with Sign in with Apple or Google, so no demo password is needed: you can sign in with your own Apple ID.
>
> **Location (When In Use only).** Pinjai asks for location only when the user taps **Start Day** on a trip, after an in-app screen that explains why. It is never requested from Search, Map or Profile. Location is used only while a trip day is in progress and the app is on screen, to (1) show the user's position on today's route and (2) calculate the travel time to the next stop. For that time, the current position is sent through our server to Google Routes only when the day starts, when the user taps Arrived or Skip, and when they tap Refresh; it is not stored or logged. There is no background location, no Always permission, no geofencing and no automatic check-in: the user taps **Arrived** at each stop. The whole trip day works without location ("Start Day without location"), and approximate location is supported.
>
> **How to test location:** open a trip → **Start Day 1** → read the explainer → **Continue** → choose an option in the system dialog.
>
> **Account deletion:** Profile tab → **Delete account** → confirm. This deletes the account and its trips; backup copies are removed within 7 days. Web page: https://my-dizexrt.github.io/pinjai-legal/delete-account/
>
> Privacy policy: https://my-dizexrt.github.io/pinjai-legal/privacy/en/ (Thai: /privacy/th/). Support: https://my-dizexrt.github.io/pinjai-legal/faq/

**TH**

> พินใจเป็นแอปวางแผนทริปสำหรับนักเดินทางในไทย เข้าสู่ระบบด้วย Apple หรือ Google จึงไม่ต้องใช้รหัสผ่านทดสอบ ผู้ตรวจใช้ Apple ID ของตัวเองเข้าได้เลย
>
> **ตำแหน่ง (เฉพาะขณะใช้แอป)** พินใจขอสิทธิ์ตำแหน่งเฉพาะตอนที่ผู้ใช้กด **เริ่มวัน** ในทริป หลังจากแสดงหน้าอธิบายเหตุผลในแอปแล้ว ไม่ขอจากหน้าค้นหา แผนที่ หรือโปรไฟล์ ใช้ตำแหน่งเฉพาะตอนวันเดินทางกำลังดำเนินอยู่และแอปเปิดอยู่บนหน้าจอ เพื่อ (1) แสดงตำแหน่งของผู้ใช้บนเส้นทางวันนี้ และ (2) คำนวณเวลาเดินทางไปจุดแวะถัดไป โดยส่งตำแหน่งปัจจุบันผ่านเซิร์ฟเวอร์ของเราไป Google Routes เฉพาะตอนเริ่มวัน ตอนกดถึงแล้วหรือข้าม และตอนกดรีเฟรช ไม่บันทึกและไม่ log ไม่มีตำแหน่งเบื้องหลัง ไม่มีสิทธิ์แบบตลอดเวลา ไม่มี geofence และไม่เช็กอินอัตโนมัติ ผู้ใช้กด **ถึงแล้ว** เองในแต่ละจุด วันเดินทางใช้ได้ครบโดยไม่ต้องเปิดตำแหน่ง ("เริ่มวันโดยไม่ใช้ตำแหน่ง") และรองรับตำแหน่งโดยประมาณ
>
> **วิธีทดสอบ:** เปิดทริป → **เริ่มวันที่ 1** → อ่านหน้าอธิบาย → **ดำเนินการต่อ** → เลือกในหน้าต่างของระบบ
>
> **ลบบัญชี:** แท็บโปรไฟล์ → **ลบบัญชี** → ยืนยัน ระบบลบบัญชีและทริปทั้งหมด สำเนาสำรองจะถูกลบภายใน 7 วัน หน้าเว็บ: https://my-dizexrt.github.io/pinjai-legal/delete-account/
>
> นโยบายความเป็นส่วนตัว: https://my-dizexrt.github.io/pinjai-legal/privacy/th/ (EN: /privacy/en/) ช่วยเหลือ: https://my-dizexrt.github.io/pinjai-legal/faq/

Open items before submission:
- Confirm the menu labels and the 7-day backup sentence against the real-auth build (deleteAccount.doneBody).
- If the reviewer build has no seeded trip, add one line: "Create a trip with + on My Trips, add two stops from Search, then Start Day 1."

## 2. Google Play — Location permissions declaration

**Expected result: the declaration form should not appear.** Play Console asks for the Location permissions declaration only when the app bundle requests `ACCESS_BACKGROUND_LOCATION`. Pinjai requests only `ACCESS_FINE_LOCATION` and `ACCESS_COARSE_LOCATION`, and `app.config.ts` puts `ACCESS_BACKGROUND_LOCATION`, `FOREGROUND_SERVICE` and `FOREGROUND_SERVICE_LOCATION` in `blockedPermissions`, with `isAndroidBackgroundLocationEnabled: false`.

If Play Console still shows the question "Does your app access location in the background?", answer **No**, with this note:

> EN: Pinjai uses location only in the foreground, while a trip day is open on screen, to show the user's position on the route and the time to the next stop. It does not request ACCESS_BACKGROUND_LOCATION and has no foreground service for location.
>
> TH: พินใจใช้ตำแหน่งเฉพาะตอนเปิดแอปอยู่บนหน้าจอระหว่างวันเดินทาง เพื่อแสดงตำแหน่งบนเส้นทางและเวลาไปจุดถัดไป ไม่ขอ ACCESS_BACKGROUND_LOCATION และไม่มี foreground service สำหรับตำแหน่ง

If the form appears anyway, stop: it means some library added the permission. Do not fill in a background justification; fix the build.

QA check (store checklist): run `bundletool dump manifest` on the release AAB (`aapt2` can't read an AAB) and confirm there is no `ACCESS_BACKGROUND_LOCATION` or `FOREGROUND_SERVICE_LOCATION`.

## 3. Prominent disclosure checklist (vs WS4 handoff round 2)

Strictly required by Google Play only for background location or uses users would not expect. Pinjai has neither, but the explainer is built to meet the bar anyway, and Apple 5.1.1 rules apply to the iOS version.

| # | Requirement | WS4 handoff | Result |
|---|---|---|---|
| 1 | Shown in the app, during normal use (not only in the store listing or policy) | Explainer on first tap of Start Day (`permissions.explainer.*`) | Pass |
| 2 | Shown **before** the system permission dialog | Explainer → Continue → OS dialog | Pass |
| 3 | Says which data: location | "Use your location during this trip" | Pass |
| 4 | Says how it is used | Three bullets: you on the route, time to the next stop, hand-off to Google/Apple Maps | Pass |
| 5 | Says when / scope: while using only, no background | Note: "Only while you're using Pinjai. No background tracking…" | Pass |
| 6 | Says if it is shared | Note says not shared with friends; Google Routes is named in policy §3, linked from the explainer ("Read privacy policy") | Pass (see nit A) |
| 7 | Needs an affirmative action; the user can decline | Android: Continue / Not now. iOS: Continue only, Don't Allow in the OS dialog (Apple 5.1.1: no "Not now" before the system dialog) | Pass |
| 8 | App still works if declined | `permissions.startDayWithout`, plan times, `errors.noLocationForEta` | Pass |
| 9 | Not re-shown after a decision | Mid-day revoke / Allow Once expiry: banner, no explainer again | Pass |
| 10 | Purpose string matches the disclosure | `NSLocationWhenInUseUsageDescription` (copy §1) matches the explainer | Pass |
| 11 | No Always / background wording or option anywhere | No Always in boards or i18n (QA round 2) | Pass |
| 12 | Approximate location accepted, honest copy | Banner v0.3.4, no "near the stop" hint | Pass |

Nits (not blocking, decide by 30 Nov):
- A. The explainer doesn't say location is sent to Google for travel times. Policy §3 covers it and is one tap away, which is enough for a foreground use. Only add a line if a reviewer asks.
- B. bullet2Sub "Drive time updates while the app is open" could read as constant polling. ETA updates only at day start, Arrived/Skip and Refresh. Suggested if we touch the copy: "Updated when you start, arrive or refresh." / "อัปเดตตอนเริ่มวัน กดถึงแล้ว หรือกดรีเฟรช". This is not a compliance issue.
