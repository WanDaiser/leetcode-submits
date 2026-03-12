# 181. Employees Earning More Than Their Managers

- Problem statement: [`181-employees-earning-more-than-their-managers.md`](./181-employees-earning-more-than-their-managers.md)
- Referenced submission: [`2025-11-17 14.35.41 - Accepted - runtime 559ms - memory 0.0B.sql`](./2025-11-17 14.35.41 - Accepted - runtime 559ms - memory 0.0B.sql)
- Language: **SQL**

![Time](https://img.shields.io/badge/Estimated%20Time-~O(n)-blue) ![Space](https://img.shields.io/badge/Estimated%20Space-~O(1)-teal)

## Complexity (Estimated)

- Time: **~O(n)**
- Space: **~O(1)**

> These values are auto-estimated from code structure and should be treated as approximations.

## Approach

- Joining tables with `JOIN`
- Conditional filtering (`WHERE`)

## Step-by-Step Code Walkthrough

- Query clause: `SELECT`
- Query clause: `FROM Employee E`
- Query clause: `JOIN Employee M`
- Query clause: `WHERE E.salary > M.salary;`

## Note

This file is auto-generated from your currently accepted submission code.
