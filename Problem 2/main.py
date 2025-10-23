# Definition for singly-linked list node
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def addTwoNumbers(l1, l2):
    # Create a dummy head node to simplify result list creation
    dummy = ListNode()
    current = dummy
    carry = 0

    # Traverse both linked lists until both end and no carry remains
    while l1 or l2 or carry:
        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0

        total = val1 + val2 + carry
        carry = total // 10
        new_val = total % 10

        current.next = ListNode(new_val)
        current = current.next

        # Move forward in both lists
        if l1:
            l1 = l1.next
        if l2:
            l2 = l2.next

    return dummy.next


# -----------------------
# Example usage
# -----------------------

# Helper function to create a linked list from a list
def create_linked_list(nums):
    dummy = ListNode()
    current = dummy
    for n in nums:
        current.next = ListNode(n)
        current = current.next
    return dummy.next

# Helper function to print linked list as a list
def print_linked_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    print(result)


# Example:
l1 = create_linked_list([2, 4, 3])  # represents 342
l2 = create_linked_list([5, 6, 4])  # represents 465

result = addTwoNumbers(l1, l2)
print_linked_list(result)  # Output: [7, 0, 8]
