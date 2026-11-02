# Psychology PhD Explorer

Find psychology, cognitive science and neuroscience faculty at the top 100 U.S. universities whose research matches yours. Describe what you want to study; matching runs entirely in your browser.

Live site: https://junyi-ch.github.io/psych_phd_finder/

A sibling of the [Linguistics PhD Explorer](https://github.com/Junyi-Ch/linguistics_phd_finder), and built from the same code. This repository is generated from that one with `pipeline/export_site.py --discipline psych`, so code changes are made there.

## What is included

- Universities: the top 100 national universities in the U.S. News 2027 ranking.
- Departments: psychology (and equivalents), cognitive science, and departments or programs named neuroscience. Medical schools, neurobiology and education schools are not included.
- Faculty: assistant, associate and full professors. In neuroscience programs, only people whose research is relevant to psychology.
- Each person: a one-sentence research summary, research labels, and links to their department profile. No photos, and no profile text is published.

## Building

```
npm ci
python pipeline/build.py --discipline psych      # data, search vectors, school logos (needs Python + sentence-transformers)
npm run build
```

Pushing to `main` deploys to GitHub Pages through `.github/workflows/deploy.yml`.

## Corrections

Faculty who want their information changed or removed can open an issue or email apc003@ucsd.edu.
