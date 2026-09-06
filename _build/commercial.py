# -*- coding: utf-8 -*-
"""
Commercial and trade pages: /commercial/<slug>/

Written for a business buyer, not a consumer. The questions are different --
turnaround, capacity, consistency, invoicing, what it does to their margin --
and so the pages do not reuse consumer service copy at all.

POSITIONING NOTE. The consumer site argues "one vehicle a day, not a
rotation." High-volume lot washing contradicts that, so these pages position
trade work as the specialty end: the trade-ins that need real correction or
odor work, and protection products sold at the desk with Sudz Up as the
installer. Not $40 lot washes. Gio should confirm this is the work he wants
before these go live.

Nothing here claims an existing dealer relationship. No dealer is named.
"""

COMMERCIAL = [

{
 "slug": "car-dealers",
 "name": "Car Dealers",
 "nav": "Car Dealers",
 "title": "Detailing & Reconditioning for Car Dealers | Washington County, WI | Sudz Up",
 "meta": "Dealer reconditioning in Washington County, WI. Trade-ins that need real odor, interior or paint work before they are lot-ready. Predictable turnaround, invoiced monthly. Call 414-286-1609.",
 "h1": "Detailing & Reconditioning for Car Dealers",
 "lede": "We are not a lot-wash service. We are where a dealer sends the trade-in that the lot wash cannot fix.",
 "glance": [("Best fit", "Problem trade-ins"), ("Turnaround", "Quoted per unit"), ("Billing", "Monthly invoice"), ("Location", "2948 WI-83, Hartford")],
 "body": [
   ("The trade-in the lot crew hands back",
    ["Every dealer has a reconditioning process that handles most inventory perfectly well. Wash, vacuum, dress the tyres, photograph, list. It works for the majority of trade-ins and it should \u2014 it is fast and cheap and most cars only need that.",
     "Then there is the other category. The trade that smells and the smell did not come out. The interior with a stain the lot crew could not lift. The paint that photographs badly under lot lighting and nobody can say exactly why. The high-value unit where a recon that is merely adequate costs real money on the front end.",
     "That is the work we take. It is not competing with your lot crew. It is the overflow they hand back, and the difference between a car sitting for sixty days and one that moves."]),
   ("What actually changes the number on the windshield",
    ["A used car is priced against condition, and buyers price condition from three things in about this order: smell, the driver's seat, and paint in direct sun.",
     "Odor is the deal-killer. A buyer who opens a door and smells smoke or dog has already discounted the car in their head, and nothing on the window sticker recovers it. Most lot recon masks odor rather than removing it, which is why the smell reappears during the test drive on a warm afternoon. We find and remove the source, which is a different process entirely and is explained on the <a href=\"/services/odor-removal/\">odor removal page</a>.",
     "Paint is the one that photographs. A trade that has spent years in automatic washes carries swirl marring that is invisible on a cloudy day and obvious in your listing photos and on the lot at noon. A single-stage <a href=\"/services/paint-correction/\">correction</a> on a higher-value unit routinely pays for itself in the asking price."]),
   ("How we work with dealers",
    ["We take units at 2948 WI-83 in Hartford. We do not do mobile lot work, because the equipment that does this properly \u2014 extraction, polishing under inspection light, coating cure conditions \u2014 does not travel.",
     "Each unit is assessed and quoted before work starts, so you know what a car is going to cost you before you decide whether it is worth it against the margin on that specific unit. We will tell you when it is not.",
     "Turnaround is quoted per unit and we hit it. For dealers sending regular volume we invoice monthly against a per-unit rate sheet rather than per job, and we can work around your delivery schedule rather than assuming a weekday drop."]),
   ("Protection products sold at the desk",
    ["A separate conversation from reconditioning: protection products sold during the deal.",
     "Ceramic coating is one of the more defensible back-end products a dealer can offer, because unlike a lot of F&I add-ons it is a real physical thing that does something. The problem is that it is often applied by whoever is available, over paint that was never properly prepared, which is how it earns a bad reputation.",
     "We install coatings as the named applicator for the product you sell. The unit comes to us after the sale, gets decontaminated and corrected as needed, coated, and returned with the customer knowing who did the work and where to come for maintenance. That is worth more to your customer than a sticker and it is worth something to you when they come back for the next car. Details on the process are on the <a href=\"/commercial/car-dealers/\">dealer coating page</a>."]),
 ],
 "faq": [
   ("Do you do lot washes or mobile detailing at the dealership?",
    "No. We take units at the shop in Hartford, because the equipment that does reconditioning properly does not travel. We are the overflow for the units your lot crew cannot fix, not a replacement for them."),
   ("How do you price dealer work?",
    "Per unit, assessed before work starts, so you can decide against the margin on that specific car. Dealers sending regular volume get a per-unit rate sheet and a monthly invoice."),
   ("What turnaround can we expect?",
    "Quoted per unit and held. An odor job and a full correction are very different timelines, and we would rather tell you the real one than an optimistic one."),
   ("Can you install the ceramic coating we sell?",
    "Yes, as the named applicator. The unit comes to us after the sale, gets properly prepped, coated and returned, and the customer knows who did the work and where to come for maintenance."),
 ],
},

{
 "slug": "dealer-ceramic-coating",
 "disabled": True,  # ceramic paused by owner 2026-09-06
 "name": "Dealer Ceramic Coating Programs",
 "nav": "Dealer Coating Programs",
 "title": "Ceramic Coating Installer for Car Dealers | Washington County, WI | Sudz Up",
 "meta": "Ceramic coating installation for dealer-sold protection packages in Washington County, WI. Proper prep, named applicator, customer maintenance handoff. Call 414-286-1609.",
 "h1": "Ceramic Coating for Dealer Protection Packages",
 "lede": "Dealer-sold coatings get a bad name for one reason: they are usually applied badly. We are the installer that fixes that.",
 "glance": [("Role", "Named applicator"), ("Prep", "Decon + correction as needed"), ("Handoff", "Customer maintenance"), ("Location", "Hartford, WI")],
 "body": [
   ("Why dealer coatings fail",
    ["A ceramic coating is clear. It seals whatever is under it and it bonds to whatever surface it meets. Both of those are the entire reason dealer-applied coatings so often disappoint.",
     "Applied over paint that was washed but not decontaminated, the coating bonds to the contamination rather than to the clear coat, and it fails early when that layer lets go. Applied over swirl marring from the lot wash, it locks the marring in for the life of the coating, so the customer paid for protection and got a permanently hazy finish.",
     "None of that is the product's fault. It is a prep problem, and prep is time \u2014 which is precisely the thing a busy delivery schedule does not have."]),
   ("What proper installation involves",
    ["The unit comes to us after the sale rather than before delivery, so the work does not sit on your delivery timeline.",
     "It is fully decontaminated \u2014 chemical iron removal, clay \u2014 so the coating meets clean clear coat. It is then assessed under inspection light and, where the paint carries marring, corrected before coating. New cars frequently need this; transport and dealer-prep marring on a brand new vehicle is common and it is exactly what a coating would otherwise preserve.",
     "Then it is coated in controlled conditions and given the cure time the product actually requires. The <a href=\"/services/ceramic-coating/\">consumer coating page</a> covers the chemistry; the short version is that cure conditions matter and a cold or damp bay produces a coating that never reaches its rated durability."]),
   ("What your customer gets, and why that matters to you",
    ["The customer gets the vehicle back with a named installer, an explanation of how to maintain it, and a place to bring it for maintenance washes and an annual check.",
     "That last part is the one dealers underrate. A customer with a properly installed coating and a maintenance relationship is a customer who has a reason to think well of the dealership two years later, when they are deciding where to buy the next car. A customer whose dealer-applied coating went hazy in a year has a very different memory.",
     "We are happy to be the face of that maintenance relationship on your behalf, or to hand it back to your service department \u2014 whichever suits how you run the store."]),
   ("Working with us as your installer",
    ["We install the product you sell, or we can recommend one. We do not push a brand; what matters is prep and application, not the label.",
     "Units are booked on a schedule we agree with you, and we hold the turnaround we quote. Coating work is multi-day when correction is involved, and we would rather tell your customer the real timeline than have them chasing you.",
     "Call or text 414-286-1609 and we will talk through volume, scheduling and rate. If your current arrangement is working, we will say so \u2014 we would rather be honest than take on work that does not fit."]),
 ],
 "faq": [
   ("Why not just have the lot crew apply it?",
    "Because a coating seals in whatever is under it. Applied over lot-wash marring or undecontaminated paint, it locks in the defects and fails early. Prep is most of the job and prep is time the delivery schedule usually does not have."),
   ("Does a brand new car really need correction before coating?",
    "Often, yes. Transport and dealer-prep marring on new vehicles is common, and a coating would preserve it permanently. We assess under inspection light and correct where needed."),
   ("Which coating product do you use?",
    "Whichever you sell, or we can recommend one. Prep and application determine the result far more than the brand."),
   ("How does the handoff to the customer work?",
    "The customer gets the vehicle back with a named installer, maintenance guidance, and a place to bring it for upkeep \u2014 either us or your service department, whichever suits the store."),
 ],
},

{
 "slug": "fleet-detailing",
 "name": "Fleet & Company Vehicles",
 "nav": "Fleet Vehicles",
 "title": "Fleet & Company Vehicle Detailing | Washington County, WI | Sudz Up Detailing",
 "meta": "Fleet and company vehicle detailing in Washington County, WI. Work trucks, service vans and company cars reset on a schedule, invoiced monthly. Call or text 414-286-1609.",
 "h1": "Fleet & Company Vehicle Detailing",
 "lede": "A company vehicle is a rolling advertisement and a workplace at the same time, and it takes a beating that no private car does.",
 "glance": [("Best fit", "Trades, service, sales"), ("Cadence", "Scheduled per vehicle"), ("Billing", "Monthly invoice"), ("Location", "Hartford, WI")],
 "body": [
   ("What a work vehicle actually does all day",
    ["A service van or work truck is used harder than a private car in every way that matters to an interior. It carries tools, materials and people in work clothing. It gets in and out dozens of times a day. It eats lunch. It sits outside overnight.",
     "The cabin wear is concentrated and fast: driver's seat bolsters worn through by abrasive workwear, floor mats destroyed, door sills scuffed to bare plastic, and a console that has held every kind of drink and food a working day produces. The load area collects grit, spilled product and organic material that never gets addressed because the vehicle is always in use.",
     "The exterior takes lettering damage, tar and road film from continuous miles, and industrial or agricultural fallout depending on the trade."]),
   ("Why it is worth doing on a schedule",
    ["Two reasons, and neither is vanity.",
     "The first is the customer's driveway. A tradesman's van is the first thing a homeowner sees, before the tradesman, and it sets the expectation for the work. A vehicle that is visibly cared for reads as a business that is careful. That is not a theory \u2014 it is why every large service company in the country spends money on fleet presentation.",
     "The second is the vehicle's life. A cabin that gets reset periodically wears far more slowly than one that never does, because ground-in grit is abrasive and it works on seats, carpet and plastics every hour the vehicle is in use. Removing it periodically is genuinely cheaper than replacing seats and mats early or taking a hit on the trade value."]),
   ("How we run fleet work",
    ["Vehicles come to 2948 WI-83 in Hartford on a schedule we set with you \u2014 per vehicle, on a rotation that fits how you run the business, rather than a fixed calendar that ignores when a van is actually free.",
     "Each vehicle gets a defined scope that we agree up front, so the result is consistent across the fleet and you know exactly what a visit costs. Problem vehicles \u2014 the van with the smell, the truck with the paint that has gone matte \u2014 get flagged and quoted separately rather than silently absorbed.",
     "Billing is a monthly invoice against the agreed scope. No surprises, and an itemised record if you want it for the accounts."]),
   ("What this is not",
    ["It is not a lot wash and it is not mobile. We do not send someone to your yard with a pressure washer, because that is not the work we do and it is not the work that makes the difference above.",
     "If what you need is a weekly rinse to keep the fleet presentable between resets, we will tell you that and point you at someone who does it. What we are for is the periodic proper reset that keeps the vehicles from wearing out and keeps them looking like the business you want to be."]),
 ],
 "faq": [
   ("Do you come to our yard?",
    "No. Vehicles come to the shop in Hartford on a schedule we agree. The equipment and time that make a proper reset work do not travel, and we would rather do the job well than conveniently."),
   ("How often should a work vehicle be done?",
    "It depends on the trade and the mileage, and we would rather set a rotation per vehicle than quote a number. Ground-in grit is abrasive, so the interval matters more for the life of the cabin than for how it looks."),
   ("How is fleet work billed?",
    "Monthly invoice against a scope agreed per vehicle. Problem vehicles get flagged and quoted separately rather than absorbed into the standard rate."),
   ("Can you handle the van that smells?",
    "Yes, and that is exactly the kind of vehicle that gets flagged rather than run through the standard scope. Odor work is assessed and quoted per vehicle."),
 ],
},

{
 "slug": "partners",
 "name": "Trade Partners",
 "nav": "Trade Partners",
 "title": "Detailing Partner for Body Shops, Mechanics & Auto Businesses | Sudz Up",
 "meta": "Detailing partner for body shops, repair shops, tint and wrap installers and auto businesses in Washington County, WI. Overflow, post-repair reset and referral work. Call 414-286-1609.",
 "h1": "A Detailing Partner for Auto Businesses",
 "lede": "If you run an auto business and detailing is not what you do, you still get asked for it. We are the answer to that question.",
 "glance": [("Best fit", "Body, repair, tint, wrap"), ("Work", "Overflow + post-repair"), ("Referrals", "Two-way"), ("Location", "Hartford, WI")],
 "body": [
   ("The job that comes back with the repair",
    ["A body shop returns a car with a flawless panel and a cabin full of sanding dust. A repair shop returns a car with a fixed engine and greasy fingerprints on the door card. A tint or wrap installer returns a car that looks new on the outside and untouched on the inside.",
     "None of that is the shop's fault and none of it is the shop's job. But the customer experiences it as part of the repair, and it is the last thing they see before deciding how they feel about the work.",
     "We take that vehicle for a post-repair reset before it goes back. The customer gets a car that feels finished. You get a job that ends well instead of with a complaint about dust."]),
   ("Overflow and the work you do not want",
    ["Most auto businesses get detailing requests they would rather not handle. A customer asks the body shop if they can get the interior done while it is in. A dealer's service department gets asked about a smell.",
     "Saying no loses goodwill. Saying yes and doing it badly loses more. Sending it to us keeps the customer inside your relationship and gets the work done by someone whose whole business is exactly that.",
     "We are happy to take the vehicle from you and return it to you, so from the customer's side it is simply part of what your shop arranged."]),
   ("Referrals run both ways",
    ["We are asked constantly for things we do not do. Paint repair, dent removal, tint, wrap, mechanical work. We would rather send those people to businesses we trust than leave them searching.",
     "If you are a shop in Washington County or the surrounding area that does good work, we would like to know you exist. That is the entire pitch. No commission structure, no formal arrangement \u2014 just two businesses that would rather refer to each other than to a stranger."]),
   ("How to start",
    ["Call or text 414-286-1609 and tell us what you do and what you get asked for. We will tell you honestly whether we are a fit and how we would handle the handoff.",
     "For shops sending regular work we can set a rate and invoice monthly. For occasional referrals it is simpler than that. Either way, the customer's experience of your shop is the thing we are protecting, and we take that seriously."]),
 ],
 "faq": [
   ("Do you pay referral fees?",
    "No, and we do not ask for them. The arrangement is two businesses that would rather refer to each other than to a stranger. If that is not enough, we are probably not the right fit."),
   ("Can you collect and return the vehicle to our shop?",
    "Yes. From the customer's side it is part of what your shop arranged, and they never have to deal with a second business."),
   ("What kind of businesses does this suit?",
    "Body shops, mechanical repair, tint and wrap installers, dealer service departments, and anyone else who gets asked about detailing and would rather not do it themselves."),
   ("We get asked about smells in cars. Is that you?",
    "Yes. Odor removal is one of the most common things we take as overflow, and it is assessed and quoted per vehicle rather than guessed at."),
 ],
},

]
