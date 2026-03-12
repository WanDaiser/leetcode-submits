# Contributing

Thanks for your interest in improving this repository.

## Scope

This repository is an archive of accepted LeetCode submissions. Preferred contributions:

- Documentation improvements
- Indexing or tooling improvements
- Non-breaking cleanup of repository metadata

## Ground Rules

- Do not rewrite historical submission files unless there is a clear data corruption issue.
- Keep folder naming format unchanged: `<problem-id>-<problem-slug>`.
- Keep generated files reproducible using repository scripts.

## Local Workflow

1. Create a branch.
2. Make focused changes.
3. Run:
   - `python scripts/generate_index.py` (if index-related changes were made)
4. Open a pull request with a clear summary.

## Commit Style

Use concise commit messages, for example:

- `docs: improve README navigation`
- `chore: refresh generated solutions index`
- `tooling: update index generator`
