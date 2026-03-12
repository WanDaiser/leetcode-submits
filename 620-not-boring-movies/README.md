# 620. Not Boring Movies

- Problem statement: [`620-not-boring-movies.md`](./620-not-boring-movies.md)
- Referenced submission: [`2025-11-17 09.30.48 - Accepted - runtime 262ms - memory 0.0B.sql`](./2025-11-17 09.30.48 - Accepted - runtime 262ms - memory 0.0B.sql)
- Language: **SQL**

![Time](https://img.shields.io/badge/Estimated%20Time-~O(n%20log%20n)-blue) ![Space](https://img.shields.io/badge/Estimated%20Space-~O(n)-teal)

## Complexity (Estimated)

- Time: **~O(n log n)**
- Space: **~O(n)**

> These values are auto-estimated from code structure and should be treated as approximations.

## Approach

- Conditional filtering (`WHERE`)
- Ordering result set (`ORDER BY`)

## Step-by-Step Code Walkthrough

- Query clause: `SELECT *`
- Query clause: `FROM Cinema`
- Query clause: `WHERE id % 2 = 1`
- Query clause: `ORDER BY rating DESC;`

## Note

This file is auto-generated from your currently accepted submission code.
