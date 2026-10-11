# labelfirst.org

Static site for LabelFirst — independent reviews of supplements and sleep
products for readers in the United States.

Twelve pages, no framework, no build dependencies beyond Python 3.

## Structure

```
index.html                              home
reviews/                                review index
reviews/prodentim/                      ← ad destination
guides/                                 guide index
guides/clinically-studied-claims/
guides/reading-supplement-labels/
guides/oral-microbiome-basics/
how-we-review/                          editorial method
about/  contact/  privacy/  affiliate-disclosure/
assets/style.css
build.py                                regenerates every page
```

## Build

Every page is generated from `build.py`. Edit the content there, not the HTML —
regenerating overwrites the HTML files.

```sh
python3 build.py
```

Four variables at the top control the whole site:

```python
SITE   = "LabelFirst"
DOMAIN = "labelfirst.org"
EDITOR = "Ernesto Luciano"
HOP    = "https://...hop.clickbank.net"
```

## Deploy

Static files. Document root is the repository root. No server-side code,
no database, no environment variables.

Target: Hostinger shared hosting, with auto-deploy from this repository.

## Non-negotiables

These are not style preferences. Removing any of them breaks either platform
policy or the merchant agreement:

- Affiliate disclosure stays at the top of every page and in the footer
- The FDA disclaimer stays in the footer of every page
- Affiliate links keep `rel="nofollow sponsored"` and `data-hop`
- The tracking script stays on pages carrying an affiliate link — without it,
  sales arrive at the network with no known source
- No invented testimonials, no star ratings we did not collect, no claims that
  a supplement treats or prevents disease
- No merchant logos, no merchant brand name in header or footer, nothing that
  could make a page read as a manufacturer's own site
