# Pinjai — Closed test tester guide (TH / EN)

**Version 0.1 · 14 Nov 2026 · internal (excluded from Pages).** Owner: QA. What testers do during the Google Play closed test and how they report problems. The invite, opt-in steps and tester-data notice are in `closed-test-invite.md` (P&C). The dates and rules come from [play-closed-test-plan.md](play-closed-test-plan.md) §2–3.

## ภาษาไทย

### 1. สิ่งที่ขอให้ทำตลอด 14 วัน

- อยู่ในโครงการทดสอบไว้และอย่าถอนตัว ถ้าผู้ทดสอบเหลือไม่ถึง 12 คน ต้องเริ่มนับ 14 วันใหม่
- เก็บแอปไว้ในเครื่อง และเปิดใช้อย่างน้อย 2–3 ครั้งต่อสัปดาห์ เพราะ Google ดูว่ามีคนใช้จริง ไม่ได้ดูแค่จำนวนคน
- เมื่อมีอัปเดตใน Play Store ให้กดอัปเดต (ไม่ต้องสมัครใหม่)

### 2. รอบที่ 1 (30 พ.ย. – 13 ธ.ค.): ลองสิ่งที่มีใน build แรก

| # | ลองทำ | ควรเห็น |
|---|---|---|
| 1 | ติดตั้งจากลิงก์ Play Store แล้วเปิดแอป | แอปเปิดได้ ไม่ปิดเอง |
| 2 | เข้าสู่ระบบด้วย Google | เข้าได้และเห็นแท็บด้านล่าง |
| 3 | สร้างทริปใหม่ แล้วเปิดดูทริปนั้น | ชื่อทริปและวันที่ถูกต้อง |
| 4 | ค้นหาสถานที่ แล้วกดเพิ่มเข้าทริป | สถานที่ไปอยู่ในวันที่เลือก และเพิ่มสถานที่เดียวกันซ้ำในทริปเดียวกันไม่ได้ |
| 5 | ลากเรียงสถานที่ในวันเดียวกัน | ลำดับเปลี่ยนและยังอยู่หลังปิดแล้วเปิดแอปใหม่ |
| 6 | เปิดแท็บค้นหาและแผนที่ | แอป **ไม่ถาม** สิทธิ์ตำแหน่ง และไม่มีจุดตำแหน่งของคุณบนแผนที่ (นอกวันเดินทาง) |
| 7 | เปลี่ยนภาษาในหน้าโปรไฟล์ ไทย ↔ English | ข้อความเปลี่ยนทั้งแอป ไม่มีคำที่ค้างเป็นอีกภาษา |

บางข้ออาจยังไม่มีใน build ที่คุณได้ ถ้าไม่เจอปุ่มหรือหน้าจอนั้น ให้ข้ามและบอกเราว่า "ไม่มีใน build"

### 3. รอบที่ 2 (หลังอัปเดตสาย 4 ราว 13–14 ธ.ค.)

| # | ลองทำ | ควรเห็น |
|---|---|---|
| 8 | เปิดทริปในวันเดินทาง (ทีมจะบอกวิธีตั้งทริปให้ตรงกับวันนี้) แล้วเลือก **อนุญาตขณะใช้แอป** | เห็นตำแหน่งของคุณในหน้าวันเดินทาง ไม่มีตัวเลือกหรือคำขอ "ตลอดเวลา" |
| 9 | ทำซ้ำข้อ 8 แต่เลือก **ไม่อนุญาต** | แอปยังใช้ได้ มีข้อความบอกว่าตำแหน่งปิดอยู่ ไม่ถามซ้ำทุกครั้ง |
| 10 | กดไปแอปแผนที่ (Directions) จากสถานที่ | เปิด Google Maps ไปยังสถานที่นั้น |
| 11 | (ทำเป็นข้อสุดท้าย) โปรไฟล์ › ลบบัญชี | ลบได้ภายในแอป แล้วกลับไปหน้าเข้าสู่ระบบ **อย่าถอนการติดตั้งแอปหรือถอนตัวจากโครงการทดสอบ** หลังลบบัญชี |

### 4. วิธีส่ง feedback

ส่งอีเมลไปที่ `support@pinjai.com` หัวเรื่อง `[Closed test] ...` โดยใส่ข้อมูลนี้:

1. รุ่นโทรศัพท์และเวอร์ชัน Android
2. เวอร์ชันแอป (ดูได้ที่ล่างสุดของหน้าโปรไฟล์)
3. ข้อที่ลอง (เลข # จากตารางด้านบน) หรือหน้าจอที่ใช้อยู่
4. ทำอะไร ควรเกิดอะไร และเกิดอะไรขึ้นจริง
5. ภาพหน้าจอหรือคลิป (ถ้ามี) **ครอปหรือเบลออีเมล ชื่อ และตำแหน่งบนแผนที่ออกก่อนส่ง**

เรื่องด่วน ให้ใส่ `[ด่วน]` ไว้หน้าหัวเรื่อง เช่น แอปปิดเอง เข้าสู่ระบบไม่ได้ ทริปหาย หรือแอปถามสิทธิ์ตำแหน่ง "ตลอดเวลา"

อย่าส่งรหัสผ่านหรือรหัสยืนยันใดๆ มาให้เรา ทีมจะไม่ขอข้อมูลเหล่านี้

## English

### 1. What we ask for the whole 14 days

- Stay in the test and don't opt out. If the tester count drops below 12, the 14 days start again.
- Keep the app installed and open it at least 2–3 times a week. Google checks that people really use it, not just the tester count.
- When Play Store shows an update, install it (you don't need to sign up again).

### 2. Round 1 (30 Nov – 13 Dec): try what the first build has

| # | Try | You should see |
|---|---|---|
| 1 | Install from the Play Store link and open the app | The app opens and doesn't close by itself |
| 2 | Sign in with Google | You get in and see the tabs at the bottom |
| 3 | Create a new trip, then open it | The trip name and dates are right |
| 4 | Search for a place and add it to a trip | It lands on the chosen day, and you can't add the same place twice to one trip |
| 5 | Drag to reorder places within a day | The order changes and stays after you close and reopen the app |
| 6 | Open the Search tab and the map | The app does **not** ask for location, and there is no dot for your location on the map (outside a trip day) |
| 7 | Switch the language on the Profile screen, Thai ↔ English | Text changes across the app, with no words left in the other language |

Some of these may not be in the build you get yet. If you can't find the button or screen, skip it and tell us "not in the build".

### 3. Round 2 (after the workstream 4 update, about 13–14 Dec)

| # | Try | You should see |
|---|---|---|
| 8 | Open a trip on its trip day (the team will tell you how to set a trip to today) and choose **Allow while using the app** | You see your location on the trip day screen; there is no "all the time" option or request |
| 9 | Repeat 8 but choose **Don't allow** | The app still works, says location is off, and doesn't ask again every time |
| 10 | Open directions to a place in the maps app | Google Maps opens at that place |
| 11 | (Do this last) Profile › Delete account | You can delete inside the app and land back on sign-in. **Don't uninstall the app or opt out of the test** after deleting |

### 4. How to send feedback

Email `support@pinjai.com` with the subject `[Closed test] ...` and include:

1. Phone model and Android version
2. App version (at the bottom of the Profile screen)
3. Which item you tried (the # from the tables above) or which screen you were on
4. What you did, what should have happened, and what happened
5. A screenshot or clip if you have one. **Crop or blur your email, name and your location on the map before sending**

For urgent problems put `[Urgent]` at the start of the subject: the app closes by itself, you can't sign in, a trip disappears, or the app asks for location "all the time".

Never send us a password or a verification code. The team will never ask for one.
