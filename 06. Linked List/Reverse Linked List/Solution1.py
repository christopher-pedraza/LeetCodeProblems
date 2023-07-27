# Time complexity: O(n)
# Space complexity: O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Current node 
        current = head
        # Previous node. As the head doesn't have a previous node, we 
        # declare it with None
        previous = None

        # While the current node is not None. If the linked list is
        # empty from the beginning, then we will skip this loop.
        # At the end of the loop, current will take the next position
        # of the last previous node (which after being reversed is the
        # new head). As it was the previous last, current will take the
        # value of None, ending the loop
        while current:
            # Get the next node of the current node before we reverse
            # the atribute `next` of it
            prevNext = current.next
            # Reverse the atribut `next` by changing its value to the
            # previous node in the list
            current.next = previous
            # Set the previous node as the current node for the next
            # iteration
            previous = current
            # Set the current node as the previous `next` of the current
            # node for the next iteration
            current = prevNext

        # After the loop ends (or never enters) we return the `previous`
        # node. We return this instead of `current` as current took the
        # `next` node of previous in the last iteration, meaning that
        # it's now None. If we never enter the loop, it means the list
        # is empty and we return None as it's the default value of
        # previous
        return previous