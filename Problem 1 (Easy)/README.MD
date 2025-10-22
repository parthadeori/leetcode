# Two Sum Problem

## Problem Description

Given an array of integers `nums` and an integer `target`, the task is to return the **indices of the two numbers** such that they add up to the target.

You may assume that:

- Each input would have **exactly one solution**.
- You **cannot use the same element twice**.
- You can return the answer in **any order**.

---

## Examples

### Example 1

**Input:** `nums = [2, 7, 11, 15]`, `target = 9`  
**Output:** `[0, 1]`  
**Explanation:** `nums[0] + nums[1] = 2 + 7 = 9`

### Example 2

**Input:** `nums = [3, 2, 4]`, `target = 6`  
**Output:** `[1, 2]`

### Example 3

**Input:** `nums = [3, 3]`, `target = 6`  
**Output:** `[0, 1]`

---

## Constraints

- `2 <= nums.length <= 10^4`
- `-10^9 <= nums[i] <= 10^9`
- `-10^9 <= target <= 10^9`
- Only **one valid answer** exists.

---

## Steps to Solve

1. **Understand the problem**  
   Identify that the goal is to find **two numbers whose sum equals the target** and return their indices.

2. **Think of a brute-force approach**

   - Check every possible pair of numbers to see if they sum to the target.
   - This works but is **slow** for large arrays (`O(n^2)` complexity).

3. **Optimize using a dictionary (hash map)**

   - Iterate through the array **once**.
   - For each number, calculate its **complement**:  
     `complement = target - current_number`
   - Check if the complement **already exists** in a dictionary that stores numbers and their indices.
   - If it exists, **return the indices**.
   - If it doesn’t exist, **add the current number and its index** to the dictionary.

4. **Return the answer**

   - Since there is only **one valid solution**, you can return the pair of indices immediately when found.

5. **Time and Space Complexity**
   - **Time Complexity:** O(n), because we traverse the list only once.
   - **Space Complexity:** O(n), for storing numbers in the dictionary.

---

## Key Points

- Use a dictionary to remember numbers already seen for **efficient lookups**.
- Ensure not to use the same element twice.
- The solution can be returned in **any order**.

---

This problem is commonly used in **interviews and coding tests** to assess problem-solving skills, understanding of **hash maps**, and ability to **optimize brute-force solutions**.
