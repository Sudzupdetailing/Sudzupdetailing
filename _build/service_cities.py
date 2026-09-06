# -*- coding: utf-8 -*-
"""
Service x city pages: /services/<service>/<city>/

THE RULE FOR THIS FILE. Every entry is hand-written for that specific
combination and must answer one question: why does THIS service in THIS town
need its own page? If the honest answer is "it doesn't", the combination does
not get built. A page whose local content would work equally well with the
town name swapped out is exactly the thing that gets a local site filtered,
and it is worse than not having the page at all.

Practically that means each entry needs a real local hook -- a specific road,
employer, lake, track, subdivision pattern, industry, commute or seasonal
event -- that changes what we actually find in vehicles from that town for
that service. Population figures and "conveniently located near" filler do
not count.

Build order is deliberate: combinations with the strongest local hook first.
A weak combination is left unbuilt rather than padded.

Sources for local facts: Washington County / Ozaukee County / Waukesha County
public information, WisDOT, Wisconsin DNR, and venue operators. Anything not
verified stays out.
"""

# (service_slug, city_slug) -> content
# h1/title/meta/lede/glance/body/faq are all per combination.
SERVICE_CITIES = [

{
 "service": "interior-detailing",
 "city": "slinger-wi",
 "title": "Interior Car Detailing in Slinger, WI | Sudz Up Detailing",
 "meta": "Interior car detailing for Slinger, WI drivers. Ten minutes from our Hartford shop. Track dust, commuter wear and winter salt handled properly. Call 414-286-1609.",
 "h1": "Interior Detailing in Slinger, Wisconsin",
 "lede": "Slinger is about ten minutes from our shop, and it sends us a kind of interior work we do not get from anywhere else in the county.",
 "glance": [("From our shop", "About 10 minutes"), ("Cars", "$135"), ("SUVs & trucks", "$150"), ("Booking", "Often same week")],
 "body": [
   ("The Speedway changes what we pull out of Slinger cars",
    ["Slinger Super Speedway runs a quarter-mile high-banked asphalt oval right in the village, and on race nights the paddock and the surrounding lots fill with vehicles that have spent an evening parked next to a track surface being scrubbed by tyres.",
     "What that produces is a very fine, dark rubber-and-asphalt dust that behaves differently from ordinary road dirt. It is light enough to stay airborne for hours, so it settles through open windows and into the cabin rather than staying on the outside of the car. Then it works into seat stitching, seat belt webbing and the felt lining of door pockets, where it is stubborn precisely because it is greasy rather than gritty.",
     "You cannot vacuum it out. A vacuum needs airflow across a surface and this material is bonded into fibre. It needs compressed air to break it loose first and then extraction to lift it, which is the same reason we do that sequence on every interior but it matters more here than on a car that has only seen supermarket car parks."]),
   ("Two very different Slinger vehicles",
    ["The village has grown a lot on the residential side, and a good share of what we see is the newer-subdivision commuter profile: a car that runs Highway 60 and then I-41 south toward Milwaukee five days a week, with all the wear that implies concentrated in the driver's quarter of the cabin.",
     "The other half is the older village core and the surrounding farmland, and those vehicles carry a completely different problem set. Field dust in spring, hay chaff, and the fine grit that comes off gravel drives and settles into every horizontal surface in the car.",
     "We treat those as separate jobs even though they book as the same service. A commuter car needs the driver's seat, sill and floor mat worked hard and the rest done normally. A farm vehicle needs the whole cabin blown out before anything else happens, because starting with a vacuum just redistributes the dust."]),
   ("Winter, and why we push January here",
    ["Highway 60 through Slinger gets treated early and often, and the I-41 interchange means a lot of local vehicles pick up brine from a much wider road network than the village itself.",
     "That salt ends up in the carpet backing, and because it draws in and holds moisture, a Slinger commuter car that does short trips in January never dries out between drives. That is what produces the February smell people blame on a spill they cannot find.",
     "January is our quietest month and it is when the salt is actually sitting in the carpet, so it is both the most effective and the easiest time to get a Slinger vehicle booked in."]),
 ],
 "faq": [
   ("How far is your shop from Slinger?",
    "About ten minutes down WI-83. We are at 2948 WI-83 in Hartford. Call or text 414-286-1609 before you head over so we can confirm we are on site."),
   ("Do you deal with race night dust?",
    "Regularly. It is greasy rather than gritty, so it bonds into seat stitching and belt webbing where a vacuum cannot reach it. Compressed air first, then extraction, is what actually removes it."),
   ("Can I get in the same week?",
    "Usually, yes. Slinger is close enough that local vehicles are easy for us to slot in. January is by far the easiest month to book."),
 ],
},

{
 "service": "interior-detailing",
 "city": "west-bend-wi",
 "title": "Interior Car Detailing in West Bend, WI | Sudz Up Detailing",
 "meta": "Interior detailing for West Bend, WI drivers. High-mileage commuter cars, river-valley damp and winter salt handled properly. About 20 minutes from our shop. Call 414-286-1609.",
 "h1": "Interior Detailing in West Bend, Wisconsin",
 "lede": "West Bend is the largest community we serve, and its vehicles arrive with the most consistent wear pattern of anywhere in the county.",
 "glance": [("From our shop", "About 20 minutes"), ("Cars", "$135"), ("SUVs & trucks", "$150"), ("Common issue", "Driver's-quarter wear")],
 "body": [
   ("County-seat mileage concentrates the damage",
    ["West Bend is the county's employment centre, which means West Bend vehicles are doing real daily mileage rather than weekend errands. That shows up in the cabin in a very specific and very lopsided way.",
     "A high-mileage commuter wears out one quarter of its interior and leaves the rest nearly untouched. The driver's outer seat bolster goes first, from the friction of getting in and out twice a day. Then the steering wheel develops a polished patch at ten and two. Then the driver's floor mat holds ground-in dirt far worse than the other three, and the door sill takes a thousand boot scuffs.",
     "We treat that quarter as its own job with its own time budget. It is the part of the car you look at every single day, and it is the part a rushed detail always averages out across the whole cabin."]),
   ("The Milwaukee River holds damp longer than the rest of the county",
    ["The city sits on the Milwaukee River, and the low ground near the water holds humidity noticeably longer into spring than the higher ground west toward Hartford.",
     "For vehicles that park outside near the river, that means condensation forms under floor mats and stays there. If you have ever lifted a mat and found the carpet underneath damp when nothing was spilled, that is the mechanism, and it is far more common in West Bend cars than in cars from the hills around Erin or Richfield.",
     "Damp carpet plus road salt in the backing is the combination that produces a persistent musty smell. Surface cleaning will not touch it. Extraction pulls the moisture and the salt out together, which is the only thing that actually resolves it."]),
   ("Worth the twenty minutes",
    ["West Bend has its own options, so the honest question is why drive to Hartford. The answer is that we book one vehicle at a time rather than rotating between several, and interior work is where that difference is most visible.",
     "Dwell time is most of interior detailing. Chemicals need to sit. Carpet needs to be extracted, allowed to release and extracted again. None of that survives a schedule with another car waiting.",
     "Drop the vehicle in the morning and it is a twenty minute run each way. For an interior service you are usually looking at getting it back the same day."]),
 ],
 "faq": [
   ("How long does the drive from West Bend take?",
    "About twenty minutes to 2948 WI-83 in Hartford. Most West Bend customers drop off in the morning and collect the same day for interior work."),
   ("My carpet is damp but nothing was spilled \u2014 what is that?",
    "Condensation under the floor mats, which is common in vehicles parked outside near the Milwaukee River where humidity lingers. Combined with road salt in the carpet backing, it is the usual cause of a musty smell with no obvious source."),
   ("Why does only the driver's side look worn?",
    "Because that is where all the use is. On a high-mileage commuter the driver's bolster, wheel, mat and sill take essentially all the wear while the rest of the cabin stays close to new. We budget time to that quarter specifically."),
 ],
},

{
 "service": "odor-removal",
 "city": "kewaskum-wi",
 "title": "Car Odor Removal in Kewaskum, WI | Sudz Up Detailing",
 "meta": "Car odor removal for Kewaskum, WI. Dog, field, hunting season and damp-carpet smells removed at the source, not masked. Call or text 414-286-1609.",
 "h1": "Odor Removal in Kewaskum, Wisconsin",
 "lede": "Kewaskum sits at the north end of our area, right against the Kettle Moraine, and the odor work we get from up there is genuinely different from what comes out of the suburbs.",
 "glance": [("From our shop", "About 25 minutes"), ("Price", "Quoted"), ("Common source", "Dogs, field, damp"), ("First step", "Find the source")],
 "body": [
   ("Rural vehicles carry different smells",
    ["The Northern Unit of the Kettle Moraine State Forest starts just outside Kewaskum, and the village sits surrounded by working farmland. Vehicles from up there do things that suburban cars do not.",
     "Dogs are the most common single source, and specifically wet dogs after a field or a trail. The smell people describe is not really the dog, it is bacteria in the moisture the dog left in the seat foam and the carpet backing. That is why it fades when the car is dry and comes roaring back on the first humid day.",
     "The second most common is organic field material tracked in on boots. Mud, silage, manure, decaying plant matter. It works down into the carpet backing where it stays damp and continues to break down, which is a genuinely biological process rather than a cleaning problem."]),
   ("Hunting season is its own category",
    ["Every autumn we get vehicles that carried game, wet gear, or both, and those are among the harder jobs we do because the source is often blood or fluid that soaked into the boot carpet or the spare wheel well and was cleaned only on the surface.",
     "The spare well is the place people never look. It is below the load floor, it is not visible, and liquid that gets in there has nowhere to drain. We lift the floor and check it on every odor job for exactly that reason, and on hunting-season vehicles it is the source more often than not.",
     "If it soaked into the boot carpet backing rather than sitting on top of it, extraction is the answer and it usually takes more than one pass."]),
   ("Why we look before we quote",
    ["The range on this work is enormous, and quoting a rural odor job over the phone would mean guessing. Something under a seat is twenty minutes. Fluid that has been in the spare well since November is not.",
     "We will also tell you when the honest answer is replacement rather than cleaning. Foam that has absorbed a large volume of organic liquid and sat for months sometimes cannot be recovered, and we would rather tell you that than take money for a treatment that gets you halfway.",
     "If the vehicle also needs general cleaning, the <a href=\"/services/interior-detailing/\">interior detail</a> may cover part of it and the <a href=\"/services/full-detail/\">full detail</a> is better value than booking separately."]),
 ],
 "faq": [
   ("Why does the dog smell come back on humid days?",
    "Because the source is bacteria in moisture that soaked into seat foam and carpet backing. Dry conditions suppress it; humidity reactivates it. Removing the moisture and the organic material is what actually stops it, rather than treating the air."),
   ("Do you handle vehicles used in hunting season?",
    "Yes, and we always lift the load floor and check the spare wheel well. Fluid that gets in there cannot drain and is the source far more often than people expect."),
   ("How far is Kewaskum from your shop?",
    "About twenty-five minutes down to 2948 WI-83 in Hartford. Odor work is assessed before we quote, so call or text 414-286-1609 and we will arrange a look."),
 ],
},

{
 "service": "full-detail",
 "city": "oconomowoc-wi",
 "title": "Full Interior & Exterior Detailing in Oconomowoc, WI | Sudz Up Detailing",
 "meta": "Full interior and exterior detailing for Oconomowoc, WI. Lake Country vehicles, boat-tow grime and beach sand handled properly. $200 cars, $250 SUVs. Call 414-286-1609.",
 "h1": "Full Detailing for Oconomowoc, Wisconsin",
 "lede": "Oconomowoc is Lake Country, and lake vehicles take a specific kind of beating that a standard detail schedule does not account for.",
 "glance": [("From our shop", "About 25 minutes"), ("Cars", "$200"), ("SUVs & trucks", "$250"), ("Peak need", "End of summer")],
 "body": [
   ("Lake vehicles are wet vehicles",
    ["Oconomowoc sits between Lac La Belle, Fowler Lake and Okauchee Lake, and a large share of what we see from there spends its summer hauling people and gear to and from water.",
     "That produces a combination we rarely see elsewhere in one vehicle: wet swimsuits and towels sitting on seats, sand ground into carpet, and sunscreen transferred onto every hard surface and every seat back. Sunscreen is the underrated one. It is oily, it holds dirt, and on light-coloured leather and vinyl it will stain if it is left through a hot week.",
     "The wet-and-sandy combination is worse than either alone. Wet sand tracked onto carpet dries into a crust bonded to the fibre, and a household vacuum passes straight over it without lifting anything. It needs to be broken up mechanically and extracted."]),
   ("Towing changes the exterior half",
    ["A vehicle that tows a boat trailer accumulates things that a commuter car does not. Ramp grit thrown up behind the trailer coats the rear of the vehicle. Tar and road film build up on the lower panels from summer highway miles. And the rear bumper and tailgate take repeated contact from loading gear.",
     "Lake water also leaves mineral deposits. Water thrown up at a ramp dries on hot paint and leaves spotting that is not dirt sitting on the surface but mineral bonded to it, and washing does nothing for it. That comes off in the decontamination stage.",
     "This is why a full detail suits Lake Country vehicles better than either half on its own. The exterior needs decontamination and the interior needs extraction, and doing one without the other on a boat-towing vehicle leaves half the summer in place."]),
   ("Time it for the end of the season",
    ["The instinct is to detail before summer so the car looks good for it. For a lake vehicle that is backwards.",
     "Everything that damages the interior and the paint happens between June and September. Detailing in May means the work is undone by July. Detailing in September means the sand, sunscreen, mineral spotting and tar all come out at once, and the paint gets protected heading into the salt season.",
     "September is also the right month for anyone considering a <a href=\"/services/ceramic-coating/\">ceramic coating</a>, because the summer damage can be corrected first and conditions still support a proper cure."]),
 ],
 "faq": [
   ("How far is Oconomowoc from your shop?",
    "About twenty-five minutes. A full detail is a full-day booking, so plan on dropping the vehicle in the morning and collecting it later that day."),
   ("Will you get sunscreen off leather?",
    "Usually, and how completely depends on how long it sat and how hot the car got. Caught within a few weeks it comes off well. Left through a hot summer on light-coloured leather it can leave a shadow, and we will tell you which you are looking at before starting."),
   ("When should a lake vehicle be detailed?",
    "September, once the season is over. Detailing in spring means the work gets undone by July. Doing it at the end pulls out the whole summer at once and protects the paint before salt season."),
 ],
},

{
 "service": "full-detail",
 "city": "mequon-wi",
 "title": "Full Interior & Exterior Detailing for Mequon, WI | Sudz Up Detailing",
 "meta": "Full interior and exterior detailing for Mequon, WI drivers. One vehicle a day, not a rotation. $200 cars, $250 SUVs and trucks. About 30 minutes. Call 414-286-1609.",
 "h1": "Full Detailing for Mequon, Wisconsin",
 "lede": "Mequon drivers pass a lot of detailers on the way here, so this page is mostly an argument about why some of them do it anyway.",
 "glance": [("From our shop", "About 30 minutes"), ("Cars", "$200"), ("SUVs & trucks", "$250"), ("Booking", "One vehicle per day")],
 "body": [
   ("The honest case for the drive",
    ["We are not going to pretend Mequon is short of options. It is a well-served part of Ozaukee County and there are competent detailers considerably closer to you than Hartford.",
     "What we offer that most volume shops do not is that we book one vehicle a day for a full detail rather than running three in parallel. That sounds like a small operational difference and it is actually the whole product, because most of the value in detailing is dwell time and the second pass.",
     "Chemicals need to sit before they are agitated. Carpet needs to be extracted, allowed to release, then extracted again. Paint needs to be assessed after it is clean, which is the only point at which its actual condition is visible. Every one of those steps is the first thing cut when another car is waiting on the same bay."]),
   ("Garage-kept cars have the opposite problem to commuters",
    ["A lot of what comes to us from Mequon is well-maintained, garage-kept and low-mileage, and those vehicles need a different approach from a high-mileage commuter.",
     "The interior is usually in good condition, so the work is preservation rather than recovery: keeping leather from drying at the bolsters, keeping the dash from taking UV damage, and dealing with the fine dust that accumulates in a car that is driven gently and often sits.",
     "The exterior is where the real work is, and it is almost always wash-induced. A cherished car that has been through automatic washes for years carries a swirl pattern that is invisible in a garage and obvious in direct sun. That is not something a full detail fixes \u2014 it needs <a href=\"/services/paint-correction/\">paint correction</a> \u2014 but a full detail is where you first see it clearly, because the paint has to be decontaminated before defects are visible at all."]),
   ("What the logistics actually look like",
    ["It is roughly thirty minutes each way, and a full detail is a full-day booking, so this is a drop-off rather than a wait.",
     "Most Mequon customers drop off in the morning and collect late afternoon. If you are combining it with correction or coating, that becomes a multi-day job and we will tell you the real timeline before you commit rather than an optimistic one.",
     "Call or text 414-286-1609 and we will be straight with you about whether the drive is worth it for what you actually need. If it is a wash and a vacuum, it is not, and we will say so."]),
 ],
 "faq": [
   ("Why drive to Hartford when there are detailers in Mequon?",
    "The only real answer is that we book one vehicle a day for a full detail instead of rotating between several, and dwell time is most of what makes detailing work. If what you need is a wash and a vacuum, the drive is not worth it and we will tell you so."),
   ("Is this a drop-off or can I wait?",
    "Drop-off. A full detail takes most of a working day. Most Mequon customers leave the vehicle in the morning and collect it in the late afternoon."),
   ("My car is garage-kept \u2014 do I need a full detail?",
    "Often what a garage-kept car actually needs is exterior decontamination and correction rather than a full clean, because the paint carries years of wash-induced swirls while the interior is close to new. We would rather assess it and recommend the narrower service than sell you the bigger one."),
 ],
},

{
 "service": "ceramic-coating",
 "city": "germantown-wi",
 "title": "Ceramic Coating for Germantown, WI | Sudz Up Detailing",
 "meta": "Ceramic coating for Germantown, WI drivers. Real protection against I-41 corridor brine and winter salt. From $599, prep assessed per vehicle. Call 414-286-1609.",
 "h1": "Ceramic Coating for Germantown, Wisconsin",
 "lede": "Germantown sits on the I-41 corridor, which makes it one of the strongest cases for coating anywhere in our area \u2014 and one of the places the honest downside matters most.",
 "glance": [("From our shop", "About 20 minutes"), ("From", "$599"), ("Prep", "Assessed per vehicle"), ("Best month", "September")],
 "body": [
   ("Corridor miles are what coatings are actually for",
    ["A large share of Germantown vehicles run I-41 south toward Milwaukee or north toward Fond du Lac daily, and interstate winter miles are a different exposure from village driving.",
     "Interstate lanes get treated first, most often and most heavily, and at highway speed you are not just driving over brine, you are driving through a continuous mist of it thrown up by everything around you. That mist reaches the whole vehicle rather than just the lower panels, and it dries into a film across the paint.",
     "A coating does not stop salt reaching the paint and nobody should tell you it does. What it does is make the surface far less willing to hold it. Brine film releases with a rinse instead of needing to be scrubbed off, and scrubbing is where winter paint damage actually comes from \u2014 not from the salt itself but from people dragging it across their own clear coat trying to remove it."]),
   ("The maintenance obligation nobody mentions when selling it",
    ["Here is the part that matters more for a Germantown commuter than for most people. A coating is not a substitute for washing. It is a surface that makes washing effective.",
     "A coated car that is never washed through a winter of corridor miles ends up with brine film bonded on top of the coating, at which point you have the same problem you started with plus a bill. A coated car that gets rinsed regularly through winter stays genuinely clean with very little effort, which is the actual benefit.",
     "So if you commute I-41 and you are not going to rinse the car every couple of weeks in winter, be honest with yourself about that before spending the money. We would rather tell you that up front than have you feel it did not deliver."]),
   ("Prep is the price variable",
    ["The $599 starting figure covers the coating on paint that is in good condition. What moves it is what has to happen before the coating goes on.",
     "A coating is clear and it seals in whatever is under it. If the paint carries swirls from years of automatic washes, coating it locks those in for the life of the coating, and removing them later means removing the coating first. So the paint has to be decontaminated, and often corrected, before anything is applied.",
     "That is why we assess rather than quote a flat number. A three-year-old garage-kept car might need decontamination only. A daily-driven corridor car that has been through brush washes for five winters may need <a href=\"/services/paint-correction/\">correction</a> first, and that is the larger part of the job."]),
 ],
 "faq": [
   ("Will a ceramic coating protect my car from road salt?",
    "It does not stop salt reaching the paint. It makes the surface far less willing to hold brine film, so it rinses off instead of needing to be scrubbed \u2014 and scrubbing is where most winter paint damage actually comes from."),
   ("Do I still have to wash a coated car?",
    "Yes, and on an I-41 commute that matters more than most. A coating makes washing effective, it does not replace it. Never washing a coated car through winter gets you brine bonded on top of the coating."),
   ("Why is the price a starting figure rather than fixed?",
    "Because prep is the variable. Coating is clear, so it seals in whatever is underneath. Paint in good condition needs decontamination only; paint with years of wash swirls needs correction first, and that is the bigger part of the job."),
   ("When should I book it?",
    "September. Temperatures and humidity still support a proper cure, summer damage can be corrected first, and the coating goes on with a full winter of corridor brine ahead of it."),
 ],
},

]
