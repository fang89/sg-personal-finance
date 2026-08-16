# The Boring SG Money Stack

A single-page personal finance guide for Singapore residents, covering three decisions
and deliberately nothing else:

1. **Floor** — funding CPF MediSave and Special Account toward the Basic Retirement Sum,
   and what the cash top-up tax relief is actually worth at each marginal rate.
2. **Engine** — buying Ireland-domiciled accumulating ETFs (IWDA / EIMI / VWRA) through
   Interactive Brokers, and why domicile beats index choice for a Singapore resident.
3. **Leakage** — one uncapped flat-rate cashback card, with the fee-versus-rate maths.

Two interactive calculators are built in: a CPF top-up planner that projects your Special
Account against your own cohort's Basic Retirement Sum, and a card comparison that nets
cashback against the annual fee.

**This is not financial advice.** Every figure was checked against primary sources on
16 August 2026. See the disclaimer and source list in the page footer.

## Structure

```
index.html                 the entire site — no build step, no dependencies
artifact.html              generated preview body (Claude Artifact / embed use)
tools/build_artifact.py    regenerates artifact.html from index.html
.nojekyll                  tells GitHub Pages to serve the files as-is
```

`index.html` is the single source of truth. Everything — styles, scripts, content — is
inline in that one file, so it works from a local `file://` open, any static host, or
GitHub Pages with no toolchain.

## Running it locally

Open `index.html` in a browser. That is the whole procedure.

If you want a local server (for consistent relative-path behaviour):

```sh
python3 -m http.server 8000
# then visit http://localhost:8000
```

## Publishing to GitHub Pages

```sh
cd sg-personal-finance
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin git@github.com:<your-username>/<your-repo>.git
git push -u origin main
```

Then in the repository: **Settings → Pages → Build and deployment → Source:
Deploy from a branch**, branch `main`, folder `/ (root)`. The site appears at
`https://<your-username>.github.io/<your-repo>/` within a couple of minutes.

For a custom domain, add a `CNAME` file containing the bare domain and point a
`CNAME` DNS record at `<your-username>.github.io`.

## Regenerating the artifact preview

```sh
python3 tools/build_artifact.py
```

## Keeping it accurate

The page states a verification date in three places — the masthead stamp, the footer
disclaimer, and the colophon. Update all three whenever you refresh the figures. Things
that move, and when:

| What | Changes | Source |
|---|---|---|
| BRS / FRS / ERS | every 1 January | [CPF Board](https://www.cpf.gov.sg/service/article/what-are-the-retirement-sums-basic-retirement-sum-brs-full-retirement-sum-frs-and-enhanced-retirement-sum-ers) |
| Basic Healthcare Sum | every 1 January | [CPF Board](https://www.cpf.gov.sg/member/infohub/news/news-releases/cpf-interest-rates-from-1-january-to-31-march-2026-and-basic-healthcare-sum-for-2026) |
| CPF interest rate floors | reviewed quarterly | [CPF Board](https://www.cpf.gov.sg/member/growing-your-savings/earning-attractive-interest) |
| Income tax bands and reliefs | at each Budget | [IRAS](https://www.iras.gov.sg/taxes/individual-income-tax/basics-of-individual-income-tax/tax-reliefs-rebates-and-deductions/tax-reliefs) |
| ETF expense ratios | occasionally | [justETF](https://www.justetf.com/en/etf-profile.html?isin=IE00B4L5Y983) |
| IBKR commission schedule | occasionally | [IBKR Singapore](https://www.interactivebrokers.com.sg/en/pricing/commissions-home.php) |
| Card rates and annual fees | frequently, with little notice | each issuer |

Hard-coded numbers live in two places: the HTML tables, and the constants at the top of
each calculator in the `<script>` block (`BRS_2026`, `FRS_2026`, `BRS_GROWTH`, `CPF_RATE`,
and the `CARDS` array). Change both.

## Contributing

Corrections are welcome, especially on figures that have moved. Please cite the primary
source in the pull request.

## Licence

MIT — see [LICENSE](LICENSE).
