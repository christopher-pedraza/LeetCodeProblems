# Neetcode.io solution

# It is the same solution as mine, the only difference is that this
# was made as an iterative function, while I did it recursively.

# Time complexity: O(logn) becase in the worst case we will only search
#                  half of the tree
# Memory complexity: O(1)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def lowestCommonAncestor(self, root: "TreeNode", p: "TreeNode", q: "TreeNode") -> "TreeNode":
        # Start at the root
        current = root

        # We are guaranteed that there will be an answer, so current will never
        # be None as we will find the answer before
        while current:
        	# If both are greater than the root, check the right side as the
        	# LCA is somewhere in that side
            if p.val > current.val and q.val > current.val:
                current = current.right
            # If both are smaller than root, check the left side as the LCA
        	# is somewhere in that side
            elif p.val < current.val and q.val < current.val:
                current = current.left
            # If we have a node smaller than root and one bigger than it
	        # it means it's a split and the current node is the LCA as
	        # each node is in a different side of the tree. Another case
	        # that enters here is if the current node is equal to one of
	        # the nodes q or p. In both cases, this is the LCA
            else:
                return current
