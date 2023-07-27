# Neetcode.io recursive solution (the iterative
# solution is pretty much the same as mine, so
# I didn't include it)

# Time complexity: O(n)
# Space complexity: O(n)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # If the linked list is empty or the function was called
        # passing the next of the last node
        if not head:
            return None

        # newHead will keep the new head. At the beggining, it will
        # be the current head, but as we move recursively, we will
        # change it's value
        newHead = head

        # If there's still a node after the current one 
        if head.next:
            # Update newHead with the returned value
            newHead = self.reverseList(head.next)
            # We want to reverse the link of the `next` node. So
            # we change the `next` value of the `next` node to the
            # current node
            head.next.next = head

        # Set the next value of the current node to None. If
        # the current node is not the last one (or previously
        # the first one, this `next` value will get replaced
        # in the previous recursive call, however, if it's
        # the last one, then it will remain as None as there
        # shouldn't be any more nodes after it)
        head.next = None

        # After reversing the list, we return the new head of the list
        return newHead