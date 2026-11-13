# Pinjai — Personal data breach response (PDPA s.37(4))

**Version 0.1 · 14 Nov 2026 · internal (excluded from Pages).** Not legal advice. Based on PDPA s.37(4) and the PDPC notice on breach notification B.E. 2565 (ประกาศ คปช. เรื่อง หลักเกณฑ์และวิธีการในการแจ้งเหตุการละเมิดข้อมูลส่วนบุคคล พ.ศ. 2565).

**Rule in one line:** notify the PDPC Office (สคส.) without undue delay and **within 72 hours of becoming aware**, unless the breach is unlikely to risk people's rights and freedoms. If the risk is **high**, also tell the affected users without delay, with remedies.

## Who does what
| Role | Who |
|---|---|
| Decides and notifies (controller) | Owner (Pattarapon Bunchuai) |
| Contains and investigates | Software Engineer, with the owner |
| Risk assessment and wording | Privacy & Compliance |
| Processors must tell us without delay (s.40(2)) | Supabase, Google, Sentry |

## Steps and clock
The 72 hours start when we have reasonable grounds to believe a breach happened (aware), not when the investigation ends.

| When | Step |
|---|---|
| Hour 0 | Anyone who sees a possible breach (alert, report, processor email) posts it to the owner at once. Write down the time: this starts the clock. |
| 0–24 h | **Check** the report is credible and **contain** it: rotate keys, revoke sessions, fix RLS, turn off the affected function, keep logs. Don't delete evidence. |
| by 24 h | **Assess risk** (see below) and decide: no risk / risk / high risk. Write down why. |
| by 72 h | If risk or high risk: **notify สคส.** through the PDPC channel (e-service on pdpc.or.th; check the current channel at that time). If some facts are still missing, send what we know and follow up; give reasons for any delay. |
| without delay | If high risk: **tell affected users** by email and in the app, in Thai and English: what happened, what data, what we did, what they should do, contact. |
| after | Fix the root cause, update this file and the ROPA, and keep the incident record. |

## Risk assessment
Consider: what data (location, email, notes with other people's names are worse than app version), how many users, whether it's identifiable, whether it was encrypted, whether it's already contained, and the likely harm (fraud, stalking, embarrassment).
- **No risk:** e.g. encrypted data with the key safe, or data that identifies no one. Don't notify, but **keep the record**, because we must be able to show PDPC why.
- **Risk:** notify สคส.
- **High risk:** e.g. emails plus trip plans (where and when someone will be) leaked publicly. Notify สคส. **and** users.

## What to include in the notice to สคส.
1. What happened, when it happened and when we found out.
2. Categories and rough number of people and records.
3. Contact: owner, support@pinjai.com.
4. Likely consequences.
5. Measures taken or planned, to stop it and reduce harm, including what users have been told.

## User notice template (high risk)
> **TH:** เรียนผู้ใช้พินใจ เมื่อวันที่ [วันที่] เราพบว่า [เหตุการณ์] ทำให้ข้อมูล [ประเภทข้อมูล] ของคุณอาจถูกเข้าถึงโดยไม่ได้รับอนุญาต เราได้ [สิ่งที่ทำแล้ว] และแจ้งสำนักงานคณะกรรมการคุ้มครองข้อมูลส่วนบุคคลแล้ว แนะนำให้คุณ [สิ่งที่ควรทำ] สอบถามได้ที่ support@pinjai.com
>
> **EN:** Dear Pinjai user, on [date] we found that [what happened], so your [data types] may have been accessed without permission. We have [actions] and notified Thailand's PDPC Office. We recommend you [steps]. Questions: support@pinjai.com

## Incident record (keep every case, even "no risk")
| Field | |
|---|---|
| ID / date found / who reported | |
| Aware time (clock start) | |
| What happened, systems, data, people affected | |
| Containment actions and times | |
| Risk level and reasoning | |
| สคส. notified? when, reference | |
| Users notified? when, how | |
| Root cause and fix | |

## Open items (owner, via PM)
- Confirm processor breach contacts and that each DPA requires notice to us without delay.
- Confirm the current PDPC notification channel before launch.
- Keep an out-of-band contact (phone) so the 72-hour clock isn't lost over a weekend.
