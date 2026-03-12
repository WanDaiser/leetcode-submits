# 20. Valid Parentheses

- Problem statement: [`20-valid-parentheses.md`](./20-valid-parentheses.md)
- Referenced submission: [`2025-11-05 22.03.08 - Accepted - runtime 0ms - memory 7.9MB.c`](./2025-11-05 22.03.08 - Accepted - runtime 0ms - memory 7.9MB.c)
- Language: **C**

![Time](https://img.shields.io/badge/Estimated%20Time-~O(n)-blue) ![Space](https://img.shields.io/badge/Estimated%20Space-~O(n)-teal)

## Complexity (Estimated)

- Time: **~O(n)**
- Space: **~O(n)**

> These values are auto-estimated from code structure and should be treated as approximations.

## Approach

- Stack usage
- Iterative loop-based solution

## Step-by-Step Code Walkthrough

- Function signature: `int top = -1;`
- Data-structure operation: `void push(char c) {`
- Conditional check: `if (top == MAX - 1) return;`
- Data-structure operation: `char pop() {`
- Conditional check: `if (top == -1) return '\0';`
- Return path: `return stack[top--];`
- Function signature: `bool isEmpty() {`
- Return path: `return top == -1;`

## Note

This file is auto-generated from your currently accepted submission code.
