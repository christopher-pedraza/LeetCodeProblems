# Neetcode.io solution

# Time complexity: O(n) - actually O(2n)
# Space complexity: O(1) - no need of any data structure,
#                          just modified the pointers of
#                          the nodes

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Basically what we are going to do is first divide the list
# in two. To do this we find the middle using two pointers:
# a fast and a slow one. After that, we are going to reverse
# the second half by reversing the `next` pointers of its
# nodes. After reversing the second half, we can build the
# new list by having two pointers at the beginning of the 
# two lists (the pointer of the second list will be at the
# end of the previous complete list, and as we have reversed
# the pointers, we are going to be able to use `next` to
# traverse it in reverse [from end to the middle])

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # Find the middle of the list.
        # We are going to use 2 pointers to find the middle,
        # one fast and the other one slower. The fast one
        # starts 1 position after the slow one and will move
        # 2 positions each time, while the slow one only moves
        # 1 position each time and starts at the beggining.
        # When the next value of fast is None (meaning the list
        # has an even number of nodes and we have reached the
        # end of it) or it's None itself (meaning the list has
        # an odd number of nodes and we have passed the end by
        # 1 node), we say we have found the start of the second
        # half of the list in the next position of slow
        # Slow starts in first position, fast in second.
        # We are assured that the list has at least 1 node, so
        # we won't get an error for using next over the first
        # node in case it's None
        slow, fast = head, head.next
        while fast and fast.next:
        	# Move slow once
            slow = slow.next
            # Move fast twice
            fast = fast.next.next
        # The second list is from the next node of the slow
        # pointer
        second = slow.next

        # Reverse second half
        # We are going to keep track of the previous node of the
        # current node as it's going to become the new `next` of
        # it. For the first node in the second half, the prev 
        # will be None as its now the last element of the
        # reversed list. Thus, we also change the next value of
        # the current node to None 
        prev = slow.next = None
        # While the second half of the list still has nodes
        while second:
        	# temporarily store the next node as we are going to
        	# break the `next` link
            tmp = second.next
            # Change the `next` pointer to the previous node
            second.next = prev
            # Update the previous node with the current one
            prev = second
            # Update the current node with the previous `next`
            second = tmp

        # Merge two halfs
        # Two pointers to traverse from the beginning and end of
        # the list
        # The `first` pointer will be the head, the `second` one
        # will start from the end of the second half, which is now
        # the beginning of it. As `second` became None in the last
        # iteration of reversing the second half, we are using prev
        # as the starting node of it
        first, second = head, prev
        # While the second half still has nodes
        while second:
        	# Temporarily store the next node from both pointers
            tmp1, tmp2 = first.next, second.next
            # The next node of first will be second (last node)
            first.next = second
            # The next node of second (which is now after first)
            # will be the next node of first
            second.next = tmp1
            # Update first and second with the stored `next` nodes
            first, second = tmp1, tmp2