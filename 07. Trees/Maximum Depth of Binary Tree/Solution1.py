# Time complexity: O(n) we have to go through the whole tree
# to find the deepest node
# Space complexity: O(1) no need of additional data structure

# This solution is using recursive DFS

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # If we reached an empty node, it means the child
        # that was received doen't exist, thus we don't
        # consider this height, and return 0
        if not root:
            return 0

        # We add 1 (current height) to the maximum height
        # returned from going through the tree by the left
        # and right path
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))