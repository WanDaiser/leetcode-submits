# LeetCode Submits

[![Problems](https://img.shields.io/badge/problems-109-blue)](docs/SOLUTIONS.md)
[![Languages](https://img.shields.io/badge/languages-5-0A7EA4)](docs/SOLUTIONS.md)
[![Index Check](https://github.com/WanDaiser/leetcode-submits/actions/workflows/index-check.yml/badge.svg)](https://github.com/WanDaiser/leetcode-submits/actions/workflows/index-check.yml)
[![Last Commit](https://img.shields.io/github/last-commit/WanDaiser/leetcode-submits)](https://github.com/WanDaiser/leetcode-submits/commits/main)
[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

Accepted LeetCode submissions archive, organized by problem and kept up to date with an auto-generated index.

## Why this repository

- Fast problem lookup with folder-per-problem structure
- Historical accepted submissions (different attempts over time)
- Multi-language coverage (`Python`, `C`, `C++`, `C#`, `SQL`)
- Reproducible index generation via script + CI check

## Quick Navigation

- Full index: [`docs/SOLUTIONS.md`](docs/SOLUTIONS.md)
- Contribution guide: [`CONTRIBUTING.md`](CONTRIBUTING.md)
- Index generator: [`scripts/generate_index.py`](scripts/generate_index.py)

## Repository Structure

```text
<problem-id>-<problem-slug>/
  <problem-id>-<problem-slug>.md
  <timestamp> - Accepted - runtime ... - memory ....<ext>
docs/
  SOLUTIONS.md
scripts/
  generate_index.py
```

Notes:
- `*.md` inside problem folders are exported statements.
- Source files are accepted submissions and may include multiple versions.

## Local Workflow

### 1) Export latest accepted submissions

```bash
python -m pip install leetcode-export
leetcode-export --only-accepted --folder . --cookies "LEETCODE_SESSION=...; csrftoken=..."
```

### 2) Refresh index

```bash
python scripts/generate_index.py
```

### 3) Commit and push

```bash
git add .
git commit -m "chore: refresh leetcode submissions"
git push
```

## Automation

GitHub Actions workflow [`index-check.yml`](.github/workflows/index-check.yml) regenerates the index and fails if `docs/SOLUTIONS.md` is stale.

## Contributing

Please read [`CONTRIBUTING.md`](CONTRIBUTING.md) before opening a PR.

## License

This repository is licensed under the MIT License. See [`LICENSE`](LICENSE).
