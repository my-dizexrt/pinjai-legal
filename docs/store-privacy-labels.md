# Pinjai: Apple App Privacy and Google Play Data safety (v0.3 draft)

_v0.3 (12 Nov 2026): updated for the WS3 decisions: recent searches kept on the device, `place_id` stored, stop coordinates kept at most 30 days (pinjai #37), and no Google place names stored. The form answers themselves don't change; only the notes and decisions 5–7 are new. PM enters the forms once the owner opens the store accounts._

_Owner: Privacy & Compliance. 12 Nov 2026. Source: the live privacy policy (https://my-dizexrt.github.io/pinjai-legal/privacy/en/), REQUIREMENTS.md (MVP) and docs/decisions.md. MVP only: sign in with Apple or Google, location only While Using, Sentry with no PII, no ads, no analytics SDK, no photo access. Update this file through the policy-sync rule whenever data, processors, retention or sign-in change. Not legal advice._

## Apple App Store Connect › App Privacy

**Do you or your third-party partners collect data from this app?** Yes.
**Tracking:** No data is used to track. No ATT prompt is needed.

| Apple data type | Collected | Linked to the user | Used for tracking | Purpose | Notes |
|---|---|---|---|---|---|
| Contact Info › Name | Yes | Yes | No | App Functionality | Display name from Apple or Google, editable in Profile |
| Contact Info › Email Address | Yes | Yes | No | App Functionality | Account email (may be an Apple relay address) |
| Identifiers › User ID | Yes | Yes | No | App Functionality | Supabase account ID |
| User Content › Other User Content | Yes | Yes | No | App Functionality | Trips, stops, notes, Arrived times. A Google stop is stored as `place_id` plus its coordinates (at most 30 days, then deleted and fetched again); the Google place name is not stored. Custom-pin names are the user's own text. |
| Location › Precise Location | Yes | No | No | App Functionality | Only while the app is open, for the position on today's route and the ETA. Sent through our server to Google Routes. Not stored. |
| Search History | Yes | No | No | App Functionality | Place searches sent through our server to Google Places. Not stored on our servers. The last 8 searches stay only on the phone, so that list is not "collected". |
| Diagnostics › Crash Data | Yes | No | No | App Functionality | Sentry, `sendDefaultPii: false` |
| Diagnostics › Other Diagnostic Data | Yes | No | No | App Functionality | Device model, OS and app version in Sentry events |

Not collected: Coarse Location (the approximate option is still the same declared location type), Photos or Videos, Contacts, Browsing History, Purchases, Financial Info, Health, Sensitive Info, Usage Data/Product Interaction (no analytics SDK), Advertising Data, Device ID.

**Privacy Policy URL (per locale):** Thai: `https://my-dizexrt.github.io/pinjai-legal/privacy/th/`. English: `https://my-dizexrt.github.io/pinjai-legal/privacy/en/`.

## Google Play Console › Data safety

- Does your app collect or share any of the required user data types? **Yes**
- Is all user data encrypted in transit? **Yes**
- Do you provide a way for users to request that their data is deleted? **Yes**, in the app and at `https://my-dizexrt.github.io/pinjai-legal/delete-account/`
- Shared with third parties? **No** for every type. Supabase, Google Maps Platform and Sentry are service providers acting for us, and Apple/Google sign-in is started by the user, so Play does not count these as sharing.
- Independent security review: No. Families / Designed for Families: No (13+).

| Play category › type | Collected | Ephemeral | Required or optional | Purposes |
|---|---|---|---|---|
| Location › Precise location | Yes | Yes | Optional (the trip works without it) | App functionality |
| Personal info › Name | Yes | No | Required | App functionality, Account management |
| Personal info › Email address | Yes | No | Required | App functionality, Account management |
| Personal info › User IDs | Yes | No | Required | App functionality, Account management |
| App activity › Other user-generated content | Yes | No | Required | App functionality (trips and stops; Google stops are `place_id` plus coordinates kept at most 30 days) |
| App activity › In-app search history | Yes | Yes | Required | App functionality |
| App info and performance › Crash logs | Yes | No | Required | App functionality |
| App info and performance › Diagnostics | Yes | No | Required | App functionality |

Not collected: Approximate location as a separate type (only if Android grants approximate, it is the same location request), Photos and videos, Contacts, Messages, Financial info, Health, Web browsing, Device or other IDs, App interactions (no analytics).

Privacy policy URL (one only): `https://my-dizexrt.github.io/pinjai-legal/privacy/en/` (it links to Thai at the top).

## Decisions (PM, 12 Nov 2026)

1. **Location is Not linked.** Rule for WS3: the Edge Function must not log coordinates together with the user ID and must not store coordinates. QA checks Edge Function logs and Sentry breadcrumbs. If this ever changes, Apple Linked becomes Yes.
2. **Searches are declared** (Apple Search History, Play In-app search history), because queries go to Google. Declaring more is safer than missing one.
3. **Google profile photo** counts as account data, not Photos. The app never accesses the photo library.
4. **No trip sharing in the MVP.** Before any sharing ships, update the privacy policy, the FAQ and these answers first.
5. **Recent searches stay on the device.** Apple and Google count data as collected only when it leaves the device, so the 8-item list adds no type. The searches themselves are still declared (decision 2). The list holds only the typed text and an optional `place_id`, and is cleared on sign-out and account deletion.
6. **Stop coordinates are place data, not user location.** They are the location of a place the user picked, stored with the trip, so they fall under Other User Content. They are kept at most 30 days under Google's terms. Precise Location covers only the device's live position, which is never stored.
7. **No Google place content is stored** except `place_id`. Names, photos and reviews stay in memory for the current session, and Sentry scrubs Places fields. Nothing new to declare.
