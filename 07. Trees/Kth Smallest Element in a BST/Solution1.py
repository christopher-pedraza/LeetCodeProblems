# Neetcode.io solution

# The idea of this algorithm is the same as mine
# however, I solved it recursively, while he did
# it iteratively.

# Time complexity: O(n)
# Space complexity: O(1)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        stack = []
        curr = root

        # While neither the current node or the stack is
        # empty	
        while stack or curr:
        	# While current is not None, we will keep
        	# going to the left
            while curr:
            	# Append the current node to the stack
                stack.append(curr)
                # Go left
                curr = curr.left
            # Pop the top value so we can process it.
            # This should be the left most node that
            # hasn't still been processed.
            # We process after going to the left as
            # the current node is the parent of the
            # left children, so it should be bigger
            # than any left children by the definition
            # of a BST, but, smaller than any right
            # children, thus we go through the left,
            # then process the current node, and finally
            # go through the right
            curr = stack.pop()
            # Reduce k so we know when to stop popping
            # nodes from the stack
            k -= 1
            # If K is 0, it means we reached the kth
            # smallest element
            if k == 0:
            	# So we return the current value that
            	# was popped
                return curr.val
            # After going all the way to the left, and
            # processing the current node, we start
            # going to the right. 
            curr = curr.right