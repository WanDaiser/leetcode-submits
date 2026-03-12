# 326. Power Of Three

- Problem statement: [`326-power-of-three.md`](./326-power-of-three.md)
- Referenced submission: [`2025-10-17 14.36.17 - Accepted - runtime 4ms - memory 9.1MB.cpp`](./2025-10-17 14.36.17 - Accepted - runtime 4ms - memory 9.1MB.cpp)
- Language: **C++**

## Approach

- Iterative loop-based solution

## Step-by-Step Code Walkthrough

- Function signature: `bool isPowerOfThree(int n) {`
- Conditional check: `if(n<=0){return false;}`
- Loop step: `while(n%3==0){n=n/3;}`
- Return path: `return n==1;`

## Note

This file is auto-generated from your currently accepted submission code.
