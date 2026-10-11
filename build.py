# -*- coding: utf-8 -*-
import os, html

SITE   = "LabelFirst"
DOMAIN = "labelfirst.org"
EDITOR = "Ernesto Luciano"
HOP    = "https://c5b6c6yqqlf5rr69yar2rroic4.hop.clickbank.net"
YEAR   = "2026"

NAV = """<a href="/reviews/">Reviews</a><a href="/guides/">Guides</a><a href="/how-we-review/">How we review</a><a href="/about/">About</a>"""

DISCLOSURE = ('<strong>Advertising disclosure:</strong> %s is reader-supported. If you buy through a link '
 'on this site we may earn a commission from the seller, at no extra cost to you. That commission does not '
 'change what we write, and we are not paid by the manufacturers we cover. '
 '<a href="/affiliate-disclosure/">Full disclosure</a>.') % SITE

FOOT_DISC = ('<p><strong>Disclaimer.</strong> Statements about dietary supplements on this site have not been '
 'evaluated by the Food and Drug Administration. No product covered here is intended to diagnose, treat, cure '
 'or prevent any disease. Our articles are general information, not medical advice. Consult a qualified '
 'healthcare professional before starting any supplement, particularly if you are pregnant, nursing, taking '
 'medication, or managing a health condition.</p>')

TRACK = """<script>
/* Carries ad tracking parameters through to the merchant link.
   Without this, sales arrive at the network with no known source. */
(function () {
  var keep = ['traffic_source','traffic_type','offer','campaign',
              'adgroup','ad','creative','fbclid','extclid'];
  try {
    var qs = new URLSearchParams(window.location.search);
    var links = document.querySelectorAll('a[data-hop]');
    for (var i = 0; i < links.length; i++) {
      var u = new URL(links[i].href);
      for (var j = 0; j < keep.length; j++) {
        var v = qs.get(keep[j]);
        if (v) u.searchParams.set(keep[j], v);
      }
      var ms = qs.get('msclkid');
      if (ms) u.searchParams.set('extclid', ms);
      links[i].href = u.toString();
    }
  } catch (e) {}
})();
</script>"""

TPL = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="https://{domain}{path}">
<link rel="stylesheet" href="/assets/style.css">
</head>
<body>
<header class="masthead">
  <div class="masthead-in">
    <a class="brand" href="/">Label<span>First</span></a>
    <nav>{nav}</nav>
  </div>
</header>
<div class="disclosure"><div>{disclosure}</div></div>
<div class="wrap{wide}">
{body}
<footer>
{footdisc}
<p><strong>Advertising disclosure.</strong> {site} participates in affiliate programs and may earn a commission on purchases made through links on this site. This does not affect our assessment. ClickBank is the retailer for some products we cover; ClickBank's role as retailer does not constitute an endorsement.</p>
<p>&copy; {year} {site} &middot; <a href="/about/">About</a> &middot; <a href="/how-we-review/">How we review</a> &middot; <a href="/contact/">Contact</a> &middot; <a href="/privacy/">Privacy</a> &middot; <a href="/affiliate-disclosure/">Affiliate disclosure</a></p>
</footer>
</div>
{track}
</body>
</html>
"""

def page(path, title, desc, body, wide=False, track=False):
    out = TPL.format(title=title, desc=desc, path=path, nav=NAV, disclosure=DISCLOSURE,
                     body=body, footdisc=FOOT_DISC, site=SITE, year=YEAR, domain=DOMAIN,
                     wide=" wrap-wide" if wide else "", track=TRACK if track else "")
    d = "." + path
    os.makedirs(d, exist_ok=True)
    with open(os.path.join(d, "index.html"), "w") as f:
        f.write(out)
    print("wrote", path)


# ---------------------------------------------------------------- HOME
page("/", "LabelFirst — Supplement and sleep product reviews that start with the label",
 "Independent reviews of supplements and sleep products. We read the label, check the claims, and say plainly what we could not verify.",
 """
<h1>We read the label before we read the promise.</h1>
<p class="lede-home">Most reviews of supplements and sleep products online were written by people who never opened the box. We take a different route: the label, the terms, the refund window, and an honest account of where the evidence stops.</p>

<div class="grid">
  <article class="card">
    <p class="kicker">Review</p>
    <h3><a href="/reviews/prodentim/">ProDentim: what's actually in it, and who it's for</a></h3>
    <p>A probiotic lozenge aimed at the mouth rather than the gut. Three named strains, a modest CFU count, and a 60-day refund window.</p>
    <a class="more" href="/reviews/prodentim/">Read the review &rarr;</a>
  </article>
  <article class="card">
    <p class="kicker">Guide</p>
    <h3><a href="/guides/clinically-studied-claims/">"Clinically studied" does not mean what you think</a></h3>
    <p>An ingredient can be studied while the product containing it has never been tested. The gap between those two sentences is where most supplement marketing lives.</p>
    <a class="more" href="/guides/clinically-studied-claims/">Read the guide &rarr;</a>
  </article>
  <article class="card">
    <p class="kicker">Guide</p>
    <h3><a href="/guides/reading-supplement-labels/">How to read a supplement label in two minutes</a></h3>
    <p>Proprietary blends, CFU counts, "at time of manufacture", and the three things worth checking before you spend anything.</p>
    <a class="more" href="/guides/reading-supplement-labels/">Read the guide &rarr;</a>
  </article>
  <article class="card">
    <p class="kicker">Guide</p>
    <h3><a href="/guides/oral-microbiome-basics/">The oral microbiome, without the marketing</a></h3>
    <p>What researchers actually know about the bacteria in your mouth, and what gets overstated when someone is selling something.</p>
    <a class="more" href="/guides/oral-microbiome-basics/">Read the guide &rarr;</a>
  </article>
</div>

<h2>Why this site exists</h2>
<p>Search for almost any supplement and you will find dozens of pages describing a dramatic personal transformation over 30, 60 or 90 days, often on hijacked domains, often with stock photographs attached to invented names. Some of them do not even describe the right product.</p>
<p>That is not a review. It is a sales page wearing a review's clothes, and it is why people have stopped trusting the format.</p>
<p>We publish what can be checked and we are explicit about what cannot. If a product has no published trial, we say so. If a claim has no verifiable source, we give it no weight. If we have not used something, we do not pretend we have. <a href="/how-we-review/">Our method is written down</a>, and you can hold us to it.</p>
""", wide=True)

# ---------------------------------------------------------------- REVIEWS INDEX
page("/reviews/", "Reviews — LabelFirst",
 "Independent product reviews: what the label says, what the company claims, what we could verify, and what we could not.",
 """
<h1>Reviews</h1>
<p class="standfirst">Each review covers the same ground in the same order: what the product is, what is in it, what the company claims, what it costs, and what we could not verify.</p>
<div class="grid">
  <article class="card">
    <p class="kicker">Oral health</p>
    <h3><a href="/reviews/prodentim/">ProDentim: what's actually in it, and who it's for</a></h3>
    <p>Three named probiotic strains, 3.5 billion CFUs, a 60-day refund window, and no published trial on the formula itself.</p>
    <a class="more" href="/reviews/prodentim/">Read the review &rarr;</a>
  </article>
</div>
<p style="margin-top:28px;color:var(--ink-faint);font-size:16px">More reviews are in progress. We publish slowly because checking takes longer than copying.</p>
""", wide=True)

# ---------------------------------------------------------------- GUIDES INDEX
page("/guides/", "Guides — LabelFirst",
 "Plain explanations of the things supplement marketing relies on you not knowing: label conventions, claim wording, and what the research does and does not show.",
 """
<h1>Guides</h1>
<p class="standfirst">The background you need to judge a product yourself, rather than taking anyone's word for it. No products are sold in these articles.</p>
<div class="grid">
  <article class="card">
    <p class="kicker">Claims</p>
    <h3><a href="/guides/clinically-studied-claims/">"Clinically studied" does not mean what you think</a></h3>
    <p>The difference between a studied ingredient and a tested product, and why it matters more than any other sentence on a label.</p>
    <a class="more" href="/guides/clinically-studied-claims/">Read &rarr;</a>
  </article>
  <article class="card">
    <p class="kicker">Labels</p>
    <h3><a href="/guides/reading-supplement-labels/">How to read a supplement label in two minutes</a></h3>
    <p>Proprietary blends, CFU counts, potency dating, and the three checks worth doing before you spend anything.</p>
    <a class="more" href="/guides/reading-supplement-labels/">Read &rarr;</a>
  </article>
  <article class="card">
    <p class="kicker">Research</p>
    <h3><a href="/guides/oral-microbiome-basics/">The oral microbiome, without the marketing</a></h3>
    <p>An active research field, and a convenient story for anyone selling a lozenge. Where one ends and the other begins.</p>
    <a class="more" href="/guides/oral-microbiome-basics/">Read &rarr;</a>
  </article>
</div>
""", wide=True)

# ---------------------------------------------------------------- GUIDE 1
page("/guides/clinically-studied-claims/", '"Clinically studied" does not mean what you think — LabelFirst',
 "An ingredient can be studied while the product containing it has never been tested. Here is how to tell which one a label is claiming.",
 """
<h1>"Clinically studied" does not mean what you think</h1>
<p class="standfirst">An ingredient can be studied for thirty years while the product containing it has never been tested once. Almost all supplement marketing lives in the gap between those two sentences.</p>
<div class="byline"><span>By """ + EDITOR + """</span><span>October 2026</span><span>5 minute read</span></div>

<p>Pick up any supplement and you will find a phrase like <em>clinically studied ingredients</em>, <em>research-backed formula</em>, or <em>science-based blend</em>. Read it closely. Almost none of them claim the product was tested. They claim something was.</p>

<h2>The three levels, and why only one of them counts</h2>
<p>There are three quite different things a company can mean, and the wording rarely tells you which:</p>
<ul>
  <li><strong>The ingredient has been studied.</strong> Somewhere, at some dose, in some population, a compound with this name was examined. This is the weakest version and by far the most common.</li>
  <li><strong>The specific strain or extract has been studied.</strong> Stronger. A trademarked strain with a code after its name usually means a particular, identifiable material was used in research.</li>
  <li><strong>This finished product has been tested.</strong> Rare. It means this exact combination, at this exact dose, in this delivery format, was given to people and measured against a control.</li>
</ul>
<p>Only the third tells you anything about what is in your hand. The first two tell you about a literature that may have used ten times the dose, a different delivery method, and a population with nothing in common with you.</p>

<div class="flag">
  <p><b>A test you can run in ten seconds.</b> Read the claim and ask: <em>is the subject of this sentence the ingredient, or the product?</em> "Contains clinically studied strains" is about ingredients. "Our formula was tested in a randomised trial" is about the product. Companies that have the second almost always say so plainly, with a citation. Companies that only have the first phrase it so you will hear the second.</p>
</div>

<h2>Dose is where most of it falls apart</h2>
<p>A study showing an effect at 500&nbsp;mg says nothing useful about a product containing 50&nbsp;mg. This is not a technicality — it is the single most common gap between a cited study and the bottle citing it. When a label uses a proprietary blend, you often cannot check the dose at all, which is usually the point.</p>

<h2>Delivery matters as much as quantity</h2>
<p>A compound swallowed in a capsule, dissolved in the mouth, or applied to skin reaches different places in different amounts. Research on one route does not transfer to another. A probiotic studied for gut outcomes tells you comparatively little about what happens when the same strain is held in the mouth for ninety seconds — the environment, the contact time and the competing population are all different.</p>

<h2>What a good citation looks like</h2>
<p>If a company has real research on its product, you will usually see: the name of the journal, the year, the number of participants, the duration, and what was measured. If any of those are missing — particularly participant numbers — treat the claim as marketing until shown otherwise.</p>
<p>"Backed by science" with no further detail is not a citation. It is a sentence shaped like one.</p>

<h2>None of this means supplements never work</h2>
<p>Some do, for some people, for some outcomes. The point is narrower: the phrase <em>clinically studied</em> is not evidence that a particular product will do a particular thing for you, and it is routinely presented as though it were. Knowing the difference costs nothing and changes what you are willing to pay for.</p>
""")

# ---------------------------------------------------------------- GUIDE 2
page("/guides/reading-supplement-labels/", "How to read a supplement label in two minutes — LabelFirst",
 "Proprietary blends, CFU counts, potency dating and serving-size arithmetic — the checks worth doing before you spend anything.",
 """
<h1>How to read a supplement label in two minutes</h1>
<p class="standfirst">You do not need a biochemistry degree. You need to know where companies hide things, and there are only a few places.</p>
<div class="byline"><span>By """ + EDITOR + """</span><span>October 2026</span><span>6 minute read</span></div>

<p>The front of a supplement bottle is advertising. The back is closer to a legal document, and it is where the actual information lives. Here is the order worth reading it in.</p>

<h2>1. Check the serving size first, not the ingredients</h2>
<p>Every quantity on the panel refers to one serving. If the serving is three capsules and the bottle holds ninety, that is a thirty-day supply, not ninety. This quietly triples the real price of a product that looked cheaper than its competitor. Do this arithmetic before anything else, because it sometimes ends the decision on its own.</p>

<h2>2. Look for the words "proprietary blend"</h2>
<p>A proprietary blend lists several ingredients and one combined weight. You learn the total but not the split, which means a blend advertised at 500&nbsp;mg could be 480&nbsp;mg of the cheapest component and 20&nbsp;mg spread across the ones named in the marketing.</p>
<p>It is legal and it is sometimes genuinely about protecting a formula. It also makes the dose impossible to check, and you should price that uncertainty in.</p>

<div class="flag">
  <p><b>The useful question.</b> Not "is this a proprietary blend?" but "<em>can I tell how much of the ingredient they advertise is actually in here?</em>" If the answer is no, every claim resting on that ingredient is unverifiable by design.</p>
</div>

<h2>3. For probiotics, read the CFU count and then ignore it</h2>
<p>CFU means colony-forming units — roughly, how many live organisms are in a serving. Two things make the number less useful than it looks.</p>
<p>First, more is not better in any simple way. The relevant question is whether <em>these strains</em> do anything for <em>this outcome</em>, not how many of them there are. A large count of irrelevant strains is still irrelevant.</p>
<p>Second, and more important: look for <strong>when</strong> the count is guaranteed. "At time of manufacture" means the company counted on the day it was made and makes no promise about what survived shipping, shelf time and your kitchen cupboard. "At expiry" or "through end of shelf life" is a meaningfully stronger commitment. Many labels do not say, which is itself an answer.</p>

<h2>4. Named strains beat ingredient names</h2>
<p>"Lactobacillus reuteri" names a species containing many strains that behave differently. "L. reuteri DSM 17938" names one specific, identifiable organism that can be traced to specific research. The code after the name is the useful part. Its absence means you cannot connect the label to any particular study.</p>

<h2>5. Find the refund terms before you find the price</h2>
<p>For any product without published evidence, the guarantee <em>is</em> the evidence you are buying. A sixty-day window where you can return opened product changes the real cost of trying something from the price of the bottle to the cost of your time. A fourteen-day window on unopened product only is close to no guarantee at all for something you are meant to take daily.</p>
<p>Read who handles the refund, too. For products sold through a payment platform rather than the manufacturer directly, the platform usually processes returns — which is often easier, not harder.</p>

<h2>What is not on the label</h2>
<p>Third-party testing, the manufacturing facility, and whether anyone independent has verified the contents are usually absent. Their absence is not proof of a problem. It is simply unknown, and unknown is where most of this category sits.</p>
""")

# ---------------------------------------------------------------- GUIDE 3
page("/guides/oral-microbiome-basics/", "The oral microbiome, without the marketing — LabelFirst",
 "What researchers actually know about the bacteria in your mouth, and which parts get overstated when someone is selling a lozenge.",
 """
<h1>The oral microbiome, without the marketing</h1>
<p class="standfirst">It is a real and active research field. It is also a convenient story for anyone selling a probiotic candy. The two are worth separating.</p>
<div class="byline"><span>By """ + EDITOR + """</span><span>October 2026</span><span>5 minute read</span></div>

<p>Your mouth hosts a large and varied bacterial population — not a problem to be eliminated, but a community that exists in every healthy mouth. This has been understood for a long time, and interest in it has grown as tools for identifying bacteria have improved.</p>

<h2>What is reasonably well established</h2>
<ul>
  <li>The mouth contains hundreds of bacterial species, and the mix differs between people and between sites in the same mouth.</li>
  <li>Composition shifts with diet, smoking, medication, saliva flow and age.</li>
  <li>Certain species are associated with dental disease and others are not. Association is doing real work in that sentence — it is not the same as cause.</li>
  <li>Aggressive antimicrobial use affects the whole population, not only the species you were aiming at.</li>
</ul>

<h2>Where the marketing goes further than the research</h2>
<p>The leap usually happens in one of three places.</p>
<p><strong>From association to cause.</strong> Finding that certain bacteria are more common in people with gum problems does not establish that those bacteria caused the problem, or that adding different bacteria reverses it.</p>
<p><strong>From colonisation to benefit.</strong> Even where a supplemented strain can be detected in the mouth afterwards, that is a measurement of presence, not of benefit. Showing it is there is a much lower bar than showing it did something.</p>
<p><strong>From the gut to the mouth.</strong> A great deal of probiotic research concerns the gut. The mouth is a different environment with different pH, different oxygen, constant saliva flow and a resident population that is already established and not keen on visitors. Results do not transfer.</p>

<div class="flag">
  <p><b>The honest summary.</b> The oral microbiome is real, it matters, and manipulating it deliberately is a legitimate research direction. Whether any particular commercial product achieves anything measurable is, for most of them, simply untested. "Plausible mechanism" and "demonstrated effect" are different claims, and a lot of copy is written to blur them.</p>
</div>

<h2>What this means if you are considering an oral probiotic</h2>
<p>Treat it as an addition to brushing, flossing and professional cleaning, never a replacement. Those three have a far stronger evidence base than any supplement in this category, and no lozenge removes plaque.</p>
<p>If you have an active problem — pain, bleeding, loose teeth, persistent bad breath that does not respond to normal care — that is a reason to see a dentist, not a reason to try a supplement. Delay is the real cost there, and it can be considerable.</p>
<p>If you are simply curious and your mouth is healthy, the sensible question is what the trial costs you. That is why we pay close attention to refund terms: for a product category where most claims are untested, the guarantee is often the only concrete thing on offer.</p>
""")

# ---------------------------------------------------------------- REVIEW
page("/reviews/prodentim/", "ProDentim Review: What's Actually In It, and Who It's For — LabelFirst",
 "An independent, research-based review of ProDentim: the probiotic strains it contains, what the company claims, what we could and could not verify, and the refund terms.",
 """
<h1>ProDentim Review: What's Actually In It, and Who It's For</h1>
<p class="standfirst">A probiotic lozenge aimed at the mouth rather than the gut. We read the label, the claims, and the refund terms &mdash; and we are clear about what nobody can verify.</p>
<div class="byline"><span>By """ + EDITOR + """</span><span>Updated October 2026</span><span>6 minute read</span><span><a href="/how-we-review/">How we review</a></span></div>

<p>Most oral-care products are built around removing things &mdash; plaque, bacteria, stains. ProDentim is sold on the opposite idea: that the mouth hosts a microbial population much like the gut does, and that adding certain strains to it may be worth doing.</p>
<p>That premise is not fringe. <a href="/guides/oral-microbiome-basics/">Research into the oral microbiome</a> is an active field. Whether <em>this particular product</em> does anything useful for <em>you</em> is a separate question, and one this review cannot settle. What we can do is tell you precisely what is in the bottle, what the company says, what it costs to find out, and where the evidence runs out.</p>

<div class="verdict">
  <h2>Worth considering if</h2>
  <ul class="yes">
    <li>You already brush and floss consistently and are curious about the microbiome angle</li>
    <li>You want a low-commitment trial and value the 60-day refund window</li>
    <li>You prefer a chewable to another pill</li>
  </ul>
  <h2>Skip it if</h2>
  <ul class="no">
    <li>You have an active dental problem &mdash; pain, bleeding, loose teeth. That needs a dentist, not a supplement</li>
    <li>You expect it to replace brushing, flossing, or professional cleaning</li>
    <li>You are immunocompromised or pregnant, in which case probiotics warrant a conversation with your doctor first</li>
    <li>You want published clinical trials on this specific formula. They do not appear to exist</li>
  </ul>
</div>

<h2>What it actually is</h2>
<p>ProDentim is a chewable tablet taken once daily, sold in 30-day bottles. It is a dietary supplement, not a medicine, and it is not a replacement for anything your dentist tells you to do.</p>
<p>The format matters more than it sounds. A capsule swallowed whole delivers its contents to the stomach. A lozenge dissolved in the mouth keeps them in contact with the oral cavity, which is the entire logic of the product. Whether that contact time is enough to change anything is exactly the part nobody has published data on.</p>

<h2>What's in it</h2>
<p>Taken from the manufacturer's own label, as published on the official page in October 2026.</p>
<div class="tw">
<table>
  <thead><tr><th>Ingredient</th><th>What it is</th></tr></thead>
  <tbody>
    <tr><td>Lactobacillus Paracasei</td><td>A probiotic strain studied in various contexts, including oral and sinus health</td></tr>
    <tr><td>B. lactis BL-04&reg;</td><td>A trademarked strain of <em>Bifidobacterium lactis</em>, most studied for immune and gut outcomes</td></tr>
    <tr><td>Lactobacillus Reuteri</td><td>Among the better-documented strains in oral-health literature</td></tr>
    <tr><td>Inulin</td><td>A prebiotic fibre &mdash; food for the bacteria above, not a bacterium itself</td></tr>
    <tr><td>Malic acid</td><td>A fruit acid, commonly used for taste and sometimes associated with surface stain</td></tr>
    <tr><td>Tricalcium phosphate</td><td>A calcium compound used in dental products and as a tablet excipient</td></tr>
    <tr><td>Peppermint</td><td>Flavour</td></tr>
  </tbody>
</table>
</div>
<p>Total potency is stated as <strong>3.5 billion CFUs</strong> per serving, across the three probiotic strains.</p>

<div class="flag">
  <p><b>Worth knowing about that number.</b> CFU counts are a measure of quantity, not of effect. A high count of strains that do nothing for your situation is still nothing. 3.5 billion is modest next to gut probiotics advertising 50 billion or more &mdash; but those are formulated for a different environment and the comparison tells you little either way. Treat the figure as a specification, not a selling point. We explain the convention in our guide to <a href="/guides/reading-supplement-labels/">reading a supplement label</a>.</p>
</div>

<h2>What the company claims, and what we can check</h2>
<div class="tw">
<table>
  <thead><tr><th>The claim</th><th>Our read</th></tr></thead>
  <tbody>
    <tr><td>Supports healthy gums and teeth</td><td>A structure/function claim, which is what supplements are legally permitted to make. It is not a claim to treat anything, and should not be read as one.</td></tr>
    <tr><td>Doctor formulated / doctor endorsed</td><td>We could not independently verify which clinician, or what their involvement was. Absent a name and a disclosure of their relationship to the company, we give this no weight.</td></tr>
    <tr><td>Probiotics support the oral microbiome</td><td>Supported as a general research direction. Not evidence about this product.</td></tr>
    <tr><td>Named, trademarked strains</td><td>Verifiable, and a point in its favour. Naming specific strains is more transparent than "proprietary probiotic blend" with no detail.</td></tr>
  </tbody>
</table>
</div>
<p>On the second row, see our guide on why <a href="/guides/clinically-studied-claims/">"clinically studied" rarely means what it appears to mean</a>.</p>

<h2>Price and the refund window</h2>
<p>Three package tiers are sold: a single 30-day bottle, a three-bottle package, and a six-bottle package. The multi-bottle tiers include two digital bonuses &mdash; <em>Bad Breath Gone. One Day Detox</em> and <em>Hollywood White Teeth at Home</em>. Shipping is free within the United States; international orders are charged $15.95.</p>
<!-- EDITAR antes de publicar: confirmar os precos exactos na pagina oficial. Nao publicar valores nao verificados. -->
<p><strong>Current pricing: PRECOS_A_CONFIRMAR.</strong> Prices change; check the official page before ordering.</p>
<p>The guarantee is the part worth reading closely. The company states a <strong>60-day, 100% money-back guarantee</strong>, in its words: "If you are not impressed by the transformation of your gums and teeth&hellip; write to us and we'll refund every single cent."</p>
<p>Sixty days is long enough to actually try something daily and form a view. In practical terms it means the real cost of finding out is your time and the hassle of a return, rather than the price of the bottle &mdash; provided the refund process works as described. Purchases are processed by ClickBank, which handles refunds rather than the manufacturer.</p>

<h2>What we could not verify</h2>
<p>This is the section most reviews of this product leave out, so we'll be direct about it.</p>
<ul>
  <li><strong>No published clinical trial on this formula.</strong> There is research on individual probiotic strains. There is nothing we could find testing this specific combination, at this dose, in this delivery format.</li>
  <li><strong>The named clinician.</strong> "Doctor formulated" appears without a verifiable name or stated relationship to the company.</li>
  <li><strong>Manufacturing specifics.</strong> We could not confirm the facility, third-party testing, or whether potency is guaranteed through the expiry date rather than at the time of manufacture &mdash; a meaningful distinction for live cultures.</li>
  <li><strong>Customer reviews.</strong> A large share of ProDentim "reviews" online are affiliate pages recycling the same copy, several on hijacked domains. We did not treat any of them as evidence, and neither should you.</li>
</ul>

<div class="flag">
  <p><b>On the last point.</b> If you search this product you will find dozens of pages describing a dramatic personal transformation over 30, 60 or 90 days. Many are written by people who never opened a bottle. We have not used this product and are not going to pretend otherwise. What you have here is the label, the terms, and an honest account of where the evidence stops.</p>
</div>

<h2>The bottom line</h2>
<p>ProDentim is a transparently labelled probiotic lozenge with named strains, a modest CFU count, and an unusually long refund window. It is sold with marketing considerably more confident than the available evidence supports &mdash; which is true of most of this category.</p>
<p>If the oral-microbiome idea interests you and you treat it as an addition to brushing and flossing rather than a substitute, the 60-day guarantee makes trying it a low-stakes decision. If you are hoping it will fix a problem a dentist should be looking at, it will not, and the delay could cost you.</p>

<div class="cta">
  <p>Prices, current package options and the full refund terms are on the manufacturer's official page.</p>
  <a class="btn" href='""" + HOP + """' data-hop rel="nofollow sponsored noopener">View the official ProDentim page</a>
  <small>Affiliate link &mdash; we may earn a commission at no cost to you.</small>
</div>
""", track=True)

# ---------------------------------------------------------------- HOW WE REVIEW
page("/how-we-review/", "How we review — LabelFirst",
 "Our method, written down: what we check, what we refuse to publish, and how we handle the fact that we have not personally used most products we cover.",
 """
<h1>How we review</h1>
<p class="standfirst">Written down so you can hold us to it, and so you can tell quickly whether a page elsewhere was produced the same way.</p>
<div class="byline"><span>""" + SITE + """</span><span>Updated October 2026</span></div>

<h2>What we check, in order</h2>
<ol>
  <li><strong>The label.</strong> Ingredients as named by the manufacturer, doses where disclosed, serving size, and whether a proprietary blend hides the split.</li>
  <li><strong>The claims.</strong> Each marketing claim separated into what is a permitted structure/function statement, what is verifiable, and what rests on nothing we can find.</li>
  <li><strong>The evidence.</strong> Whether research exists on the ingredient, on the specific strain or extract, or on the finished product. These are three different things and we say which one applies.</li>
  <li><strong>The terms.</strong> Price tiers, shipping, who processes refunds, and how long the guarantee runs. For products without published evidence, the guarantee is usually the only concrete thing on offer.</li>
  <li><strong>What we could not verify.</strong> Every review carries this section. It is not a disclaimer, it is part of the finding.</li>
</ol>

<h2>We tell you when we have not used something</h2>
<p>We have not personally used most of the products we cover, and we say so in the review itself rather than implying otherwise. A research-based assessment of a label, a set of claims and a refund policy is a useful thing. A fabricated account of a personal transformation is not, and it is the single most common form this category takes.</p>
<p>Where we have used a product, the review says that too, and describes the conditions.</p>

<h2>What we will not publish</h2>
<ul>
  <li>Invented testimonials, invented reviewers, or stock photographs presented as customers</li>
  <li>Star ratings or review counts we did not collect</li>
  <li>Claims that a supplement treats, cures or prevents a disease</li>
  <li>Citations without a journal, a year and a participant count</li>
  <li>Pages designed to be mistaken for a manufacturer's own site</li>
  <li>Countdown timers, fake stock warnings or discounts that are not real</li>
</ul>
<p>Any one of these would make a page convert better in the short term. All of them would make this site worth less than nothing.</p>

<h2>How we are paid</h2>
<p>Some links on this site are affiliate links. If you buy through one, the seller pays us a commission at no additional cost to you. We are not paid by manufacturers to publish, we do not accept payment for a favourable assessment, and no company reviews our copy before it goes up.</p>
<p>The obvious conflict is that we earn more when you buy. Our answer is the "Skip it if" section that appears in every review, the "What we could not verify" section that appears in every review, and this page. Judge us on whether those sections contain anything that costs us money. If they ever stop doing so, stop trusting us.</p>
<p>Full detail on our <a href="/affiliate-disclosure/">affiliate disclosure page</a>.</p>

<h2>Corrections</h2>
<p>If something here is wrong, tell us and we will fix it and say what changed. <a href="/contact/">Contact</a>.</p>
""")

# ---------------------------------------------------------------- ABOUT
page("/about/", "About — LabelFirst",
 "Who publishes LabelFirst, why it exists, and what it is not.",
 """
<h1>About """ + SITE + """</h1>
<p class="standfirst">A small independent site reviewing supplements and sleep products for readers in the United States.</p>

<h2>Who publishes this</h2>
<p>""" + SITE + """ is published by """ + EDITOR + """, who writes and edits everything here. There is no team and no newsroom. It is one person reading labels carefully and writing down what is there.</p>
<p>We think that is worth saying plainly, because a great deal of health-product content online is published anonymously or under invented bylines. If you want to ask who wrote something or why we reached a conclusion, there is a real person to ask.</p>

<h2>Why it exists</h2>
<p>Search any supplement and the results fill with pages describing a dramatic personal transformation, usually by someone who never opened the box, frequently on domains that were hijacked for the purpose. The format has been so thoroughly abused that "review" has stopped meaning anything in this category.</p>
<p>We are trying to make it mean something again, by a simple method: publish what can be checked, be explicit about what cannot, and never pretend to experience we have not had. <a href="/how-we-review/">The method is written down.</a></p>

<h2>What this is not</h2>
<ul>
  <li><strong>Not medical advice.</strong> We are not clinicians. Nothing here replaces a conversation with your dentist, doctor or pharmacist.</li>
  <li><strong>Not a manufacturer.</strong> We do not make, sell or ship anything. Purchases happen on the seller's own site under their terms.</li>
  <li><strong>Not independent of commerce.</strong> We earn affiliate commissions. We would rather say that on every page than pretend to a purity we do not have.</li>
</ul>

<h2>Contact</h2>
<p>Corrections, questions and complaints: <a href="/contact/">get in touch</a>. We publish corrections rather than quietly editing.</p>
""")

# ---------------------------------------------------------------- CONTACT
page("/contact/", "Contact — LabelFirst",
 "How to reach LabelFirst with a correction, a question, or a complaint.",
 """
<h1>Contact</h1>
<p class="standfirst">A real address, read by the person who writes the site.</p>

<h2>Email</h2>
<!-- Criar esta caixa de correio no painel da Hostinger antes de publicar -->
<p><strong>hello@labelfirst.org</strong></p>
<p>We read everything. We reply to most things within a few days.</p>

<h2>What is useful to send</h2>
<ul>
  <li><strong>Corrections.</strong> If a fact here is wrong, tell us what and, if you can, where you saw better information. We publish corrections with a note saying what changed and when.</li>
  <li><strong>Questions about a review.</strong> If something in an assessment is unclear, ask. The answer may end up in the article.</li>
  <li><strong>Products to look at.</strong> We cannot promise to cover anything, and suggesting a product has no effect on how it is assessed.</li>
</ul>

<h2>What we do not do</h2>
<ul>
  <li>We do not accept payment for reviews or for favourable coverage.</li>
  <li>We do not publish guest posts or sponsored articles.</li>
  <li>We cannot give medical advice, including on whether a product is suitable for you. That is a question for a clinician who knows your history.</li>
  <li>We cannot process orders, refunds or shipping enquiries. Those go to the seller, whose details are on their own site.</li>
</ul>

<h2>Publisher</h2>
<!-- EDITAR: confirmar os dados da entidade antes de publicar -->
<p>""" + SITE + """ is published by """ + EDITOR + """, Luanda, Angola.</p>
""")

# ---------------------------------------------------------------- AFFILIATE DISCLOSURE
page("/affiliate-disclosure/", "Affiliate disclosure — LabelFirst",
 "How LabelFirst makes money, which links are affiliate links, and what that does and does not change.",
 """
<h1>Affiliate disclosure</h1>
<p class="standfirst">Plainly: we earn a commission when you buy through some of our links. Here is exactly how that works.</p>
<div class="byline"><span>""" + SITE + """</span><span>Updated October 2026</span></div>

<h2>The short version</h2>
<p>Some links on this site are affiliate links. If you click one and buy, the seller pays us a percentage of the sale. <strong>You pay the same price either way</strong> &mdash; the commission comes out of the seller's margin, not added to your bill.</p>

<h2>Which links</h2>
<p>Affiliate links appear in the call-to-action box at the end of a review, and are marked underneath with the words "Affiliate link". They also carry <code>rel="sponsored"</code> in the page code, which is the standard machine-readable signal for a paid link.</p>
<p>Links to our own guides and to third-party sources are ordinary links and earn us nothing.</p>

<h2>Who pays us</h2>
<p>We participate in affiliate programs operated by retailers and networks, including ClickBank, which acts as retailer for several of the products we cover. We are not employed by, owned by, or paid a fee by any manufacturer whose products appear here.</p>
<p>No company sees our copy before publication. No company has the right to request changes. We have never removed a critical finding at a seller's request, and if that ever happens we will say so on this page.</p>

<h2>The conflict, stated honestly</h2>
<p>We earn more when you buy than when you do not. That is a real incentive and we are not going to pretend it has no effect on anyone who works this way.</p>
<p>What we do about it is structural rather than promised. Every review contains a <strong>"Skip it if"</strong> section naming the people who should not buy, and a <strong>"What we could not verify"</strong> section listing the gaps in the evidence. Both cost us money on every page. They are the test &mdash; if those sections ever go soft, the site is no longer worth reading, and you should treat their disappearance as the signal.</p>

<h2>FTC</h2>
<p>This disclosure is provided in line with the United States Federal Trade Commission's guidance on endorsements and material connections in advertising. It appears at the top of every page as well as here.</p>

<h2>Questions</h2>
<p>If anything about how we are paid is unclear, <a href="/contact/">ask</a>.</p>
""")

# ---------------------------------------------------------------- PRIVACY
page("/privacy/", "Privacy policy — LabelFirst",
 "What data LabelFirst collects, what it does not, and how outbound links work.",
 """
<h1>Privacy policy</h1>
<div class="byline"><span>""" + SITE + """</span><span>Updated October 2026</span></div>

<h2>The short version</h2>
<p>We do not ask you for personal information, we do not run accounts, and we do not sell data. We do use analytics to understand which articles people read, and our outbound affiliate links pass tracking information to the seller so the sale can be attributed to us.</p>

<h2>What we collect</h2>
<p><strong>Analytics.</strong> We use a web analytics service to count visits and see which pages are read. This records technical information such as your approximate location by country, your browser and device type, the page you arrived from and the pages you view. We do not use it to identify individuals.</p>
<p><strong>Advertising parameters.</strong> If you arrived here from an advertisement, the link you clicked may carry parameters identifying the campaign and creative. We pass these through to the seller when you click an affiliate link, so that a purchase can be matched to the advertisement that led to it. These parameters describe the advertisement, not you.</p>
<p><strong>What we do not collect.</strong> We do not ask for your name, email address, postal address or payment details. There are no forms, no accounts and no newsletter on this site.</p>

<h2>Cookies</h2>
<p>Our analytics may set a cookie to avoid counting the same visitor twice. You can block or delete cookies in your browser settings; the site works without them.</p>

<h2>When you leave this site</h2>
<p>Clicking an affiliate link takes you to a seller's website or to a retail network such as ClickBank. <strong>Once you leave, this policy no longer applies.</strong> Anything you enter there &mdash; name, address, payment details &mdash; is collected by them under their own privacy policy and terms, which you should read. We never see your payment information at any point.</p>

<h2>Children</h2>
<p>This site is intended for adults and is not directed at children under 13. We do not knowingly collect information from children.</p>

<h2>Your rights</h2>
<p>Depending on where you live, you may have rights to access, correct or delete personal data held about you. Because we do not hold identifiable personal data, there is usually nothing to retrieve &mdash; but if you want to ask, <a href="/contact/">contact us</a>.</p>

<h2>Changes</h2>
<p>If this policy changes we will update the date at the top of this page.</p>
""")
