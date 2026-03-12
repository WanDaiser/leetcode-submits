from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
FOLDER_PATTERN = re.compile(r"^(?P<id>\d+)-(?P<slug>[a-z0-9-]+)$")


def to_title(slug: str) -> str:
    return slug.replace("-", " ").title()


def language_from_suffix(suffix: str) -> str:
    mapping = {
        ".py": "Python",
        ".sql": "SQL",
        ".c": "C",
        ".cpp": "C++",
        ".cs": "C#",
        ".js": "JavaScript",
        ".java": "Java",
        ".ts": "TypeScript",
        ".kt": "Kotlin",
        ".go": "Go",
        ".rb": "Ruby",
        ".rs": "Rust",
        ".swift": "Swift",
        ".php": "PHP",
        ".scala": "Scala",
        ".sh": "Bash",
    }
    return mapping.get(suffix.lower(), suffix.lower().lstrip(".").upper())


def detect_techniques(code: str, suffix: str) -> list[str]:
    low = code.lower()
    techniques: list[str] = []

    if suffix == ".sql":
        if "join" in low:
            techniques.append("Joining tables with `JOIN`")
        if "group by" in low:
            techniques.append("Grouping records (`GROUP BY`)")
        if "where" in low:
            techniques.append("Conditional filtering (`WHERE`)")
        if "order by" in low:
            techniques.append("Ordering result set (`ORDER BY`)")
        if "select" in low and not techniques:
            techniques.append("Direct selection query (`SELECT`)")
        return techniques

    if any(token in low for token in ["dict(", "{}", "unordered_map", "hashmap", " in ", ".get("]):
        techniques.append("Hash-table based lookup")
    if any(token in low for token in ["sort(", "sorted(", "order", "qsort", "std::sort"]):
        techniques.append("Sorting-based approach")
    if any(token in low for token in ["stack", "push(", "pop("]):
        techniques.append("Stack usage")
    if any(token in low for token in ["dp", "memo", "cache", "@lru_cache"]):
        techniques.append("Dynamic programming / memoization")
    if any(token in low for token in [" left", " right", "pointer", "two-pointer", "two pointer"]):
        techniques.append("Two-pointer style traversal")
    if any(token in low for token in ["for ", "while", "for(", "while("]):
        techniques.append("Iterative loop-based solution")
    if not techniques:
        techniques.append("Direct conditional / arithmetic implementation")
    return techniques


def normalize_line(line: str) -> str:
    line = line.strip()
    line = re.sub(r"\s+", " ", line)
    return line


def extract_steps(code: str, suffix: str, limit: int = 8) -> list[str]:
    steps: list[str] = []
    lines = [normalize_line(line) for line in code.splitlines() if normalize_line(line)]

    for line in lines:
        low = line.lower()
        if low.startswith(("def ", "function ", "bool ", "int ", "public ", "private ", "static ")):
            steps.append(f"Function signature: `{line}`")
        elif low.startswith(("if ", "if(", "elif ", "else if", "else {", "else:")):
            steps.append(f"Conditional check: `{line}`")
        elif low.startswith(("for ", "for(", "for (")):
            steps.append(f"Loop step: `{line}`")
        elif low.startswith(("while ", "while(", "while (")):
            steps.append(f"Loop step: `{line}`")
        elif "return " in low or low.startswith("return"):
            steps.append(f"Return path: `{line}`")
        elif suffix == ".sql" and any(k in low for k in ["select", "from", "join", "where", "group by", "order by"]):
            steps.append(f"Query clause: `{line}`")
        elif any(token in low for token in ["append(", ".add(", "push(", "pop(", "insert", "erase", "dict", "map", "set"]):
            steps.append(f"Data-structure operation: `{line}`")

        if len(steps) >= limit:
            break

    if not steps:
        fallback = lines[: min(3, len(lines))]
        if fallback:
            steps = [f"Code line: `{line}`" for line in fallback]
        else:
            steps = ["Code content appears to be empty."]
    return steps


def build_readme(problem_id: int, slug: str, statement_file: Path | None, submission_file: Path | None) -> str:
    title = to_title(slug)
    lines: list[str] = [f"# {problem_id}. {title}", ""]

    if statement_file:
        lines.append(f"- Problem statement: [`{statement_file.name}`](./{statement_file.name})")
    if submission_file:
        lines.append(f"- Referenced submission: [`{submission_file.name}`](./{submission_file.name})")
        lines.append(f"- Language: **{language_from_suffix(submission_file.suffix)}**")
    lines.append("")

    if not submission_file:
        lines.append("## Code Summary")
        lines.append("")
        lines.append("No submission file was found to explain in this folder.")
        lines.append("")
        return "\n".join(lines)

    code = submission_file.read_text(encoding="utf-8", errors="ignore")
    techniques = detect_techniques(code, submission_file.suffix)
    steps = extract_steps(code, submission_file.suffix)

    lines.append("## Approach")
    lines.append("")
    for item in techniques:
        lines.append(f"- {item}")
    lines.append("")
    lines.append("## Step-by-Step Code Walkthrough")
    lines.append("")
    for step in steps:
        lines.append(f"- {step}")
    lines.append("")
    lines.append("## Note")
    lines.append("")
    lines.append("This file is auto-generated from your currently accepted submission code.")
    lines.append("")
    return "\n".join(lines)


def main() -> None:
    folder_count = 0
    for folder in sorted(ROOT.iterdir(), key=lambda p: p.name):
        if not folder.is_dir():
            continue
        match = FOLDER_PATTERN.match(folder.name)
        if not match:
            continue

        problem_id = int(match.group("id"))
        slug = match.group("slug")
        statement_file = folder / f"{folder.name}.md"
        if not statement_file.exists():
            md_candidates = sorted(folder.glob("*.md"))
            statement_file = md_candidates[0] if md_candidates else None

        submissions = sorted(
            file
            for file in folder.iterdir()
            if file.is_file() and file.suffix.lower() != ".md" and file.name != "README.md"
        )
        latest_submission = submissions[-1] if submissions else None

        readme_text = build_readme(problem_id, slug, statement_file, latest_submission)
        (folder / "README.md").write_text(readme_text, encoding="utf-8")
        folder_count += 1

    print(f"Generated README.md files for {folder_count} problem folders.")


if __name__ == "__main__":
    main()
