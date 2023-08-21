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
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # If both are bigger than the root, check the right side as the
        # LCA is somewhere in that side
        if p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        # If both are smaller than root, check the left side as the LCA
        # is somewhere in that side
        elif p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        # If we have a node smaller than root and one bigger than it
        # it means it's a split and the current node is the LCA as
        # each node is in a different side of the tree. Another case
        # that enters here is if the current node is equal to one of
        # the nodes q or p. In both cases, this is the LCA
        else:
            return root
            