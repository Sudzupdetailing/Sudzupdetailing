# SMS Consent Workflow — Sudz Up Detailing LLC

Internal operations document. Not published on the site, not in the sitemap,
excluded in robots.txt.

Covers how SMS consent is collected, recorded and honoured across the website,
Formspree and StrataCRM, and what to do when any of it changes.

Last updated: 2026-08-26

---

## 1. The three systems and what each one holds

| System | Role | Holds consent? |
|---|---|---|
| **sudzupdetail.com** (Vercel, this repo) | Public opt-in page, `/sms-terms/`, `/sms-privacy-policy/`, `/terms/` | Displays the terms; captures the tick |
| **Formspree** | Delivers site form submissions to email | Holds the raw submission record |
| **StrataCRM** | Client records, booking, sends the texts via Twilio | **Must** hold consent for texting to be legitimate |

The important point: **the system that sends the text must be the system that
knows about the consent.** StrataCRM sends. So consent has to end up there,
whichever door the customer came through.

---

## 2. The two doors a customer can come through

### Door A — website booking form
`https://sudzupdetail.com/booking/`

1. Customer fills in name, mobile, vehicle, message.
2. Two separate checkboxes, **unchecked by default, neither required**:
   - `sms_consent` — transactional (appointment, quote, service updates)
   - `promo_consent` — promotional/marketing
3. Submission goes to Formspree, arrives in email.
4. **Manual step required:** when creating the client in StrataCRM, set their
   messaging consent to match what they ticked. If they ticked nothing, do not
   enable texting on that record.

### Door B — StrataCRM booking page
`https://stratacrm.app/book/ec7d33a1-e710-4a5f-bb78-be3114368c42`

1. Customer books a slot directly.
2. Consent is captured by StrataCRM's own form, if that field is enabled.
3. No manual step — the record is created with consent attached.

> **Open item:** confirm StrataCRM's booking form has an SMS consent field
> enabled, with unchecked default. If it does not, Door B produces bookings
> with no consent record and texting those customers is not defensible.
> Check under booking/form settings in StrataCRM.

### Door C — verbal, in person, or they text first
1. Customer gives the number verbally or texts the shop first.
2. Note the consent on their StrataCRM record, with the date and how it was given.
3. A customer texting you first is consent to reply to that conversation. It is
   **not** consent to send them marketing.

---

## 3. Weekly reconciliation

Do this once a week, or whenever site form submissions come in.

- [ ] Open the Formspree submissions inbox
- [ ] For each new submission, find or create the client in StrataCRM
- [ ] Set transactional texting on/off to match the `sms_consent` value
- [ ] Set promotional/marketing on/off to match the `promo_consent` value
- [ ] Keep the Formspree email — it is the evidence of what they agreed to
- [ ] Any submission where both boxes were unticked: create the client with
      texting **off**, and contact them by phone or email instead

---

## 4. Honouring STOP

- Twilio handles STOP automatically at the carrier level; the number is blocked
  from further messages from that sender.
- **Also turn messaging off on the StrataCRM record**, otherwise the account
  keeps queueing messages that will not deliver and the record shows the wrong
  consent state.
- If someone asks to stop by phone, email or in person, that counts. Turn it off
  the same way.
- Do not text them again unless they clearly opt back in. Reply START, or a
  fresh tick on the booking form.

---

## 5. Promotional messages are a higher bar

Transactional (appointment confirmations, "your car is ready") and promotional
(offers, seasonal availability) are treated differently.

- Promotional requires its own express written opt-in. That is why the booking
  form has two boxes rather than one.
- A customer who only ticked the first box gets appointment texts and nothing else.
- Verbal consent, or a customer texting you first, does **not** cover promotional.
- Before any promotional send, filter to customers with promotional consent only.

---

## 6. When something changes, update all of it

The site says specific things about how you handle numbers. If reality changes,
the site has to change with it, or the policy becomes inaccurate.

**Changing what kinds of texts you send** → update:
- `_build/build.py`, SMS policy section, "What we send"
- `_build/build.py`, SMS terms section 1, "Program description"
- The checkbox labels in `booking_cta_html()`

**Changing booking platform away from StrataCRM** → update:
- `BOOKING_URL` constant in `_build/build.py`
- SMS policy, "How we get your consent"
- This document

**Changing the site form endpoint** → update:
- `FORM_ENDPOINT` constant in `_build/build.py`
- Section 2 and 3 of this document

**Starting to share data with a new subcontractor** → check it against the SMS
policy's sharing clause before doing it. The policy permits sharing with support
subcontractors and nothing else.

After any of these, run `python3 _build/build.py`, review, commit, push.

---

## 7. A2P 10DLC campaign submission

URLs to supply:

- **Opt-in / consent flow:** `https://sudzupdetail.com/booking/`
- **SMS program terms:** `https://sudzupdetail.com/sms-terms/`
- **SMS privacy policy:** `https://sudzupdetail.com/sms-privacy-policy/`
- **General terms & conditions:** `https://sudzupdetail.com/terms/`

Most submission forms ask for a messaging-program terms URL separately from the
privacy policy. Give them `/sms-terms/` for that field, not `/terms/` — the
general terms cover detailing services and do not carry the messaging clauses.

Before submitting, confirm all of the following are true on the live site:

- [ ] `/booking/` loads publicly, no login required
- [ ] "Book Now" in the nav reaches it from the homepage
- [ ] The no-sale statement is visible on `/booking/`
- [ ] Both checkboxes render **unchecked**
- [ ] Neither checkbox is required to submit
- [ ] Frequency, rates, STOP and HELP disclosure is visible
- [ ] All three legal links work from `/booking/` and from the footer
- [ ] `/sms-terms/` states rates, STOP, HELP and carrier non-liability
- [ ] Sample message templates match what the policy says you send

If rejected again, the rejection code and reason text say which specific element
failed. Fix that element rather than resubmitting the same thing.

---

## 8. Records to keep

- Formspree submission emails — what each person agreed to and when
- StrataCRM client records — current consent state
- Any opt-out request received outside of STOP

Keep these for as long as you are texting the person, and for a reasonable
period after. They are the only evidence you have if a complaint is raised.

---

## 9. Caveat

This document describes an operational process, not legal advice. The TCPA and
carrier requirements around A2P messaging are enforced with real financial
consequences, and they change. If you scale up promotional messaging
meaningfully, have someone qualified review the setup.
