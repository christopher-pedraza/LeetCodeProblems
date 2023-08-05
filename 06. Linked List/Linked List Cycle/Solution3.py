# Time complexity: O(n) - iterate one or more times the list until we find
#                         the end, or the `fast` pointer reaches the `slow`
#                         one
# Space complexity: O(1) - using the same list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# We are going to use 2 pointers: one fast and one slow. The slow
# pointer will start at `head`, while the faster one, will start
# at the next position of `head`. Then, we will move them each 
# iteration, `slow` by 1 position, while `fast` by 2. If at any
# point both of them are in the same node, it means we found a
# cycle. If, on the other hand, fast (or the `next` of fast) is
# None, it means we reached the end of the list (if we have a
# cycle, we would never reach a None). In the loop we'll test
# that neither `fast`, or the next of `fast` is None. We check
# that `fast` is not none in case the list only contains 1
# element. In this case, at the beginning, when we declare
# `fast` as the next node of head, it would be None. On the 
# other hand, if the next node of fast is None, it means we
# reached the end of the list, thus, we can exit the loop.

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # If the list has no elements, return False as it cannot have
        # a cycle
        if not head:
            return False

        # Slow and fast pointers
        slow, fast = head, head.next

        # While the fast hasn't reached the end, or the next element isn't
        # the end. We check for `fast` in case the list only contains 1
        # node, and from the beginning, `fast` is None
        while fast and fast.next:
            # If both pointers point to the same node, it means we found 
            # a cycle, as the fast pointer managed to reach the slow one
            if slow == fast:
                return True

            # Move the slow pointer 1 position, and the fast one 2
            slow = slow.next
            fast = fast.next.next

        # If we exit the loop, it means we never found a cycle, instead, we
        # found the end of the list
        return False