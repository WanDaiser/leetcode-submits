from __future__ import annotations

import re


def _count_python_loop_nesting(code: str) -> int:
    max_depth = 0
    stack: list[int] = []

    for raw in code.splitlines():
        line = raw.rstrip()
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue

        indent = len(line) - len(line.lstrip(" "))
        while stack and stack[-1] >= indent:
            stack.pop()

        if re.match(r"^(for|while)\b", stripped):
            stack.append(indent)
            max_depth = max(max_depth, len(stack))

    return max_depth


def estimate_complexity(code: str, suffix: str) -> tuple[str, str]:
    low = code.lower()
    suffix = suffix.lower()

    if suffix == ".sql":
        if "group by" in low or "order by" in low or " join " in f" {low} ":
            return "O(n log n)", "O(n)"
        return "O(n)", "O(1)"

    has_sort = any(token in low for token in ["sort(", "sorted(", "std::sort", "qsort("])
    has_binary_search = all(token in low for token in ["mid", "left", "right"]) and "while" in low
    has_hash = any(token in low for token in ["dict(", "unordered_map", "hashmap", ".get(", " set(", "map["])
    has_aux_ds = any(token in low for token in ["append(", "push(", "stack", "queue", "vector<", "list("])
    has_loop = any(token in low for token in ["for ", "for(", "while ", "while("])

    if suffix == ".py":
        nesting = _count_python_loop_nesting(code)
    else:
        loop_tokens = len(re.findall(r"\bfor\b|\bwhile\b", low))
        nesting = 2 if loop_tokens >= 2 else (1 if loop_tokens == 1 else 0)

    if has_sort:
        time_complexity = "O(n log n)"
    elif has_binary_search:
        time_complexity = "O(log n)"
    elif nesting >= 2:
        time_complexity = "O(n^2)"
    elif has_loop:
        time_complexity = "O(n)"
    else:
        time_complexity = "O(1)"

    if has_hash or has_aux_ds:
        space_complexity = "O(n)"
    else:
        space_complexity = "O(1)"

    return time_complexity, space_complexity
