# 20. Valid Parentheses

- Problem statement: [`20-valid-parentheses.md`](./20-valid-parentheses.md)
- Referenced submission: [`2025-11-05 22.03.08 - Accepted - runtime 0ms - memory 7.9MB.c`](./2025-11-05 22.03.08 - Accepted - runtime 0ms - memory 7.9MB.c)
- Language: **C**

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
