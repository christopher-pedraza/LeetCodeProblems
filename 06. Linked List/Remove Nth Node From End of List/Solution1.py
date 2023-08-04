# Neetcode.io solution

# Time complexity: O(n)
# Space complexity: O(1)

# Basically we will first move a pointer n times to the right
# after that, we will keep moving it until it reaches the end
# but at the same time, we will move a left pointer that
# starts moving to the right each time the right pointer moves
# from the head. With this, once the right pointer reaches the
# end, we know that the left pointer is one position before
# the node we want to remove. With this, we can just update
# the `next` node of left with the `next` node of the `next`
# node (in other words, the next node will be the node that is
# after the node we want to remove).
# If we started the slow pointer in the `head` node, we would
# have the slow pointer end in the target node when the fast
# pointer reaches the `next` of the end node. As we want to
# change the `next` of the previous node of the target, we
# initialize the slow pointer in the dummy, which is before
# `head`, thus shifting it one position before the target

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
    	# Dummy node starting at the head
        dummy = ListNode(0, head)
        # Left pointer that starts before head and will start
        # moving to the right once the `right` pointer moves
        # n times. This pointer will be one position behind
        # the target node once the `right` pointer reaches
        # the end of the list 
        left = dummy
        # Right pointer
        right = head

        # Move the right pointer n times
        while n > 0:
        	# Move once
            right = right.next
            # Reduce n
            n -= 1

        # While the right pointer hasn't reached the end of
        # the list (that it hasn't become the `next` node of
        # the last node in the list)
        while right:
        	# Move the left pointer once to the right (which
        	# at the beginning, has `head` as `next`)
            left = left.next
            # Keep moving the right pointer
            right = right.next

        # In order to delete the node, update the `next` from
        # the node before the target node, with the node after
        # the target
        left.next = left.next.next

        # Return the next value from dummy, which is the head.
        # We cannot return head here because with this, we
        # are taking care of the edge case of having just 1
        # element in the list. 
        return dummy.next