# Add Two Numbers

## Problem Description

You are given two **non-empty linked lists** representing two non-negative integers.  
The digits are stored in **reverse order**, and **each node** contains a single digit.

You need to **add the two numbers** and return the **sum as a linked list**.

You may assume:

- The two numbers **do not contain any leading zeros**, except when the number itself is `0`.

---

## Examples

### Example 1

**Input:**  
`l1 = [2,4,3]`, `l2 = [5,6,4]`  
**Output:**  
`[7,0,8]`  
**Explanation:**  
The numbers represent `342` and `465`.  
Adding them gives `342 + 465 = 807`.  
Since digits are stored in reverse, the result is `[7,0,8]`.

---

### Example 2

**Input:**  
`l1 = [0]`, `l2 = [0]`  
**Output:**  
`[0]`

---

### Example 3

**Input:**  
`l1 = [9,9,9,9,9,9,9]`, `l2 = [9,9,9,9]`  
**Output:**  
`[8,9,9,9,0,0,0,1]`

---

## Constraints

- The number of nodes in each linked list is in the range **[1, 100]**.
- Each node’s value: **0 <= Node.val <= 9**
- The linked list represents a number **without leading zeros** (except for 0 itself).

---

## Steps to Solve

1. **Understand the representation**

   - Each linked list represents a number in **reverse order**.
   - Example: `[2,4,3]` means the number `342` (not `243`).

2. **Set up pointers**

   - Use two pointers to **traverse both linked lists** at the same time.
   - Maintain a variable `carry` to handle sums greater than 9.

3. **Add corresponding digits**

   - For each pair of digits, calculate:
     ```
     total = l1.val + l2.val + carry
     new_digit = total % 10
     carry = total // 10
     ```
   - Create a new node with `new_digit` and move both pointers forward.

4. **Handle different lengths**

   - If one list is shorter, treat missing nodes as `0`.

5. **Handle final carry**

   - If there’s a remaining carry after the last addition, create a new node for it.

6. **Return the new linked list**
   - The resulting linked list should also be **in reverse order**.

---

## Example Walkthrough

Let’s take `l1 = [2,4,3]` and `l2 = [5,6,4]`.

| Step | l1.val | l2.val | carry | Sum | New Digit | New List  |
| ---- | ------ | ------ | ----- | --- | --------- | --------- |
| 1    | 2      | 5      | 0     | 7   | 7         | [7]       |
| 2    | 4      | 6      | 0     | 10  | 0         | [7, 0]    |
| 3    | 3      | 4      | 1     | 8   | 8         | [7, 0, 8] |

Final carry = 0 → Done!  
**Result = [7, 0, 8]**

---

## Key Concepts

- **Linked List Traversal**
- **Digit-by-digit addition**
- **Carry propagation**
- **Modular arithmetic (% and //)**

---

## Complexity Analysis

- **Time Complexity:** O(max(n, m))  
  You traverse each list once.
- **Space Complexity:** O(max(n, m))  
  The result list can be as long as the longest input (plus one extra node for carry).

---
