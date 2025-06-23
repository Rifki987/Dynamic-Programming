# 509. Fibonacci Number

This repository contains the solution to the LeetCode problem **509. Fibonacci Number**.

## Problem Description

The Fibonacci numbers, commonly denoted `F(n)`, form a sequence such that each number is the sum of the two preceding ones, starting from `0` and `1`. That is:

F(0) = 0
F(1) = 1
F(n) = F(n - 1) + F(n - 2), for n > 1

markdown
Copy
Edit

Given an integer `n`, the task is to compute `F(n)`.

## Examples

### Example 1
Input: n = 2
Output: 1
Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1

shell
Copy
Edit

### Example 2
Input: n = 3
Output: 2
Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2

shell
Copy
Edit

### Example 3
Input: n = 4
Output: 3
Explanation: F(4) = F(3) + F(2) = 2 + 1 = 3

markdown
Copy
Edit

## Constraints

- `0 <= n <= 30`

## Solution Approaches

Solutions can be implemented in multiple ways, such as:

- **Recursive** (naive, with exponential time)
- **Memoization** (top-down dynamic programming)
- **Bottom-up Dynamic Programming**
- **Iterative with constant space** (optimal for this constraint)

You can find the implementation in the `solution.py` (or equivalent file in the repo).

## License

This project is licensed under the MIT License.