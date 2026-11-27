# lhparker1.github.io

Personal website of Liam H. Parker, built with [Jekyll](https://jekyllrb.com/) and the
[al-folio](https://github.com/alshedivat/al-folio) theme, and hosted on GitHub Pages.

## Where things live

| To change…                      | Edit…                                           |
| ------------------------------- | ----------------------------------------------- |
| Home page bio, subtitle, photo  | `_pages/about.md`, `assets/img/prof_pic.jpg`    |
| Research sections               | `_pages/research.md`                            |
| Publications                    | `_bibliography/papers.bib`                      |
| Code cards                      | `_data/code.yml`                                |
| CV (PDF shown on the CV page)   | `cv/CV.tex`, `cv/pubs.tex`, `cv/talks.tex`      |
| Contact icons on the home page  | `_data/socials.yml`                             |
| Name, site URL, global settings | `_config.yml`                                   |
| Background image and its fade   | `_sass/_site_custom.scss`, `assets/img/bg_*.webp` (made by `scripts/make_background.py`) |

A paper appears on the home page when its entry in `papers.bib` has `selected = {true}`.

## How it publishes

Every push to `master` runs the **Deploy site** workflow (`.github/workflows/deploy.yml`), which builds
the site and pushes the result to the `gh-pages` branch. GitHub Pages serves that branch
(Settings → Pages → Deploy from a branch → `gh-pages`).

## Updating the CV

The CV is LaTeX, in `cv/` (the `resume.cls` class is the LaTeXTemplates.com "Medium Length Professional CV"
class by Trey Hunner). Compile with `pdflatex CV.tex` (or upload the folder to Overleaf), then copy the result to
`assets/pdf/CV.pdf`.

## Preview locally

With Docker installed: `docker compose up`, then open <http://localhost:8080>.

## License

Theme code is from al-folio, under the MIT license (see `LICENSE`).

## Citation counts

The badges next to each publication show Google Scholar counts from `_data/citations.yml`. A paper gets a badge when its
entry in `_bibliography/papers.bib` has a `google_scholar_id`. Once a day the deploy workflow runs
`scripts/fetch_scholar_citations.py`, which reads the counts through [SerpApi](https://serpapi.com) (Google Scholar
blocks GitHub's servers directly) and commits the file if anything changed. It needs a repository secret named
`SERPAPI_KEY`; without it the counts simply stay as last committed.
