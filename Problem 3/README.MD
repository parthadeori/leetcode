# Longest Substring Without Repeating Characters

## Problem Description

Given a string `s`, find the **length of the longest substring** that contains **no duplicate characters**.

A **substring** is a contiguous sequence of characters within a string (unlike a subsequence, where characters can be non-contiguous).

---

## Examples

### Example 1

**Input:**  
`s = "abcabcbb"`  
**Output:**  
`3`  
**Explanation:**  
The longest substring without repeating characters is `"abc"`.  
(Note: `"bca"` and `"cab"` are also valid substrings of length 3.)

---

### Example 2

**Input:**  
`s = "bbbbb"`  
**Output:**  
`1`  
**Explanation:**  
All characters are the same, so the longest substring without duplicates is `"b"`.

---

### Example 3

**Input:**  
`s = "pwwkew"`  
**Output:**  
`3`  
**Explanation:**  
The longest substring is `"wke"`, with length 3.  
(`"pwke"` is not valid because it’s not contiguous — it’s a subsequence, not a substring.)

---

## Constraints

- `0 <= s.length <= 5 * 10^4`
- `s` consists of English letters, digits, symbols, and spaces.

---

## Steps to Solve

1. **Understand what the problem is asking**

   - You must find the **maximum length of a substring** with **unique characters**.

2. **Brute-force approach (inefficient)**

   - Generate all substrings and check each for duplicates.
   - Time complexity: O(n³).
   - This approach is too slow for large strings.

3. **Optimized approach — Sliding Window Technique**

   - Use two pointers (`start` and `end`) to create a **moving window**.
   - Use a **set** or **dictionary** to track characters in the current window.
   - Move the `end` pointer forward, adding characters until a duplicate appears.
   - When a duplicate is found, move the `start` pointer to remove the duplicate.
   - Keep updating the maximum window size.

4. **Key idea:**
   - You’re essentially maintaining a **window of unique characters** that grows and shrinks as you traverse the string.

---

## Example Walkthrough

### Example: `s = "abcabcbb"`

| Step | Window | Unique Chars                          | Length |
| ---- | ------ | ------------------------------------- | ------ |
| 1    | "a"    | ✅                                    | 1      |
| 2    | "ab"   | ✅                                    | 2      |
| 3    | "abc"  | ✅                                    | 3      |
| 4    | "abca" | ❌ duplicate `a` → move start forward |
| 5    | "bca"  | ✅                                    | 3      |

✅ The longest substring without repeating characters is `"abc"` (length 3).

---

## Complexity Analysis

- **Time Complexity:** O(n)  
  Each character is visited at most twice (once by `start`, once by `end`).
- **Space Complexity:** O(min(n, m))  
  Where `m` is the character set size (for example, 128 for ASCII).

---

## Key Concepts

- **Sliding Window Technique**
- **Hash Set / Dictionary for Fast Lookups**
- **Dynamic Window Adjustment**

---

## Summary

This problem is a classic example of the **Sliding Window** technique.  
It’s widely used in interviews to test:

- Efficient use of data structures (sets or maps)
- Handling variable window sizes
- Avoiding brute-force approaches

---

### 🧠 Takeaway

Mastering this problem helps you tackle many related ones like:

- “Longest Substring with At Most K Distinct Characters”
- “Minimum Window Substring”
- “Permutation in String”

---
