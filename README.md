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
| Talks                           | `_data/talks.yml`                               |
| Press                           | `_data/media.yml`                               |
| CV page                         | `_pages/cv.html` (talks, code, media are shared) |
| Contact icons on the home page  | `_data/socials.yml`                             |
| Name, site URL, global settings | `_config.yml`                                   |

A paper appears on the home page when its entry in `papers.bib` has `selected = {true}`.

## How it publishes

Every push to `master` runs the **Deploy site** workflow (`.github/workflows/deploy.yml`), which builds
the site and pushes the result to the `gh-pages` branch. GitHub Pages serves that branch
(Settings → Pages → Deploy from a branch → `gh-pages`).

## Preview locally

With Docker installed: `docker compose up`, then open <http://localhost:8080>.

## License

Theme code is from al-folio, under the MIT license (see `LICENSE`).
