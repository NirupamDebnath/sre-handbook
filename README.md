# SRE Handbook

A public, sanitized knowledge base for learning Site Reliability Engineering, platform engineering, and senior-level interview skills. It contains practical exercises, operational reasoning, and reusable examples—not production runbooks or confidential architecture.

**Website:** `https://YOUR-USERNAME.github.io/sre-handbook/` (replace `YOUR-USERNAME` in `mkdocs.yml` and this README before first deploy).

## What is here

- SRE foundations: service levels, error budgets, incidents, and reliability economics.
- Linux, networking, AWS/EKS, Kubernetes, delivery, GitOps, Terraform, and observability.
- Safe, local-first hands-on labs and scenario-based investigation guides.
- Senior interview prompts with model reasoning, not memorized one-line answers.

## Stack

Markdown + [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/), Python, Mermaid, and GitHub Actions/Pages. The sole Python dependency is pinned in `requirements.txt`.

## Local development

The Makefile provides the most common commands:

```bash
make install
make serve
make validate
```

Equivalent manual setup:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
mkdocs serve
```

Open `http://127.0.0.1:8000`. Validate the production build with `mkdocs build --strict`.

## Add a page

1. Add a Markdown file beneath `docs/` using descriptive headings and relative links.
2. Add it to `nav` in `mkdocs.yml`.
3. Run `mkdocs build --strict` before opening a pull request.

## Deployment

The deploy workflow publishes only pushes to `main` or a manual `workflow_dispatch`. In GitHub repository **Settings → Pages**, set **Source** to **GitHub Actions** once. Update the two `YOUR-USERNAME` values in `mkdocs.yml` first. The workflow uses the official Pages artifact/deployment actions and has no pull-request deployment path.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). Keep examples generic; never commit credentials, internal URLs, customer data, or proprietary incident details.

## Roadmap

- Extend topic pages with deeper vendor-specific, versioned guidance.
- Add runnable lab assets in isolated directories.
- Add accessibility and link checking in CI when the content set grows.

## License

MIT. See [LICENSE](LICENSE).
