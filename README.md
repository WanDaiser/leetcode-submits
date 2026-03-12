# LeetCode Submits

Curated archive of accepted LeetCode submissions exported from my account.

## Highlights

- 100+ problems solved
- Multiple languages (`Python`, `C`, `C++`, `C#`, `SQL`)
- Problem-first folder structure for fast lookup
- Auto-generated index at [`docs/SOLUTIONS.md`](docs/SOLUTIONS.md)

## Repository Structure

Each problem is stored in a dedicated folder:

```text
<problem-id>-<problem-slug>/
  <problem-id>-<problem-slug>.md
  <timestamp> - Accepted - runtime ... - memory ....<ext>
```

- `.md` file: exported problem statement
- source files: accepted submissions over time

## Quick Start

### Browse solutions

1. Open [`docs/SOLUTIONS.md`](docs/SOLUTIONS.md) for a full index.
2. Jump to a problem folder and inspect the latest accepted submission.

### Refresh the index

```bash
python scripts/generate_index.py
```

## Exporting New Submissions

This repo is fed by [`leetcode-export`](https://pypi.org/project/leetcode-export/):

```bash
python -m pip install leetcode-export
leetcode-export --only-accepted --folder . --cookies "LEETCODE_SESSION=...; csrftoken=..."
python scripts/generate_index.py
```

## Contributing

Contributions are welcome. Please read [`CONTRIBUTING.md`](CONTRIBUTING.md) before opening a PR.

## License

Distributed under the MIT License. See [`LICENSE`](LICENSE).
