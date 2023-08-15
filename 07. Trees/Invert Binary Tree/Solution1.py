# Neetcode.io solution

# Time complexity: O(n)
# Space complexity: O(1)

# The only difference is that I go down the tree through the
# left router first, then flip the left with the right, and
# then go down the right route, and finally, flip the right
# with the previous left. Here, he firsts flips both sides
# and then goes down both paths.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
    	# If we reach a root that is None, it means we have
    	# arrived at the end of the tree
        if not root:
            return None

        # Swap the children
        tmp = root.left
        root.left = root.right
        root.right = tmp

        # Go down the tree through both ways
        self.invertTree(root.left)
        self.invertTree(root.right)

        # Return the root with the swapped children
        return root
