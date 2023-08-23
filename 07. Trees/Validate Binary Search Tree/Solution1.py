# Neetcode.io solution

# Time complexity: O(n)
# Space complexity: O(1)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        # Helper function to go through the tree keeping track
        # of the min and max values already visited
        def valid(node, left, right):
            # If the node is None, then we have reached the
            # end of the tree
            if not node:
                return True
            # If the value of the node is bigger than the min
            # value, or smaller than the max value already
            # visited, then it's not a valid BST
            if not (left < node.val < right):
                return False

            # Check the left and right side of the tree
            # Pass the child, the min value, and the max value
            # For the left, we pass the left child, the min
            # value, and the now biggest which is the current
            # node's value
            # For the right, we pass the right child, the max
            # value, and the now smallest which is the current
            # node's value
            return (valid(node.left, left, node.val) and
                    valid(node.right, node.val, right))

        # The first time we pass the root and the smallest
        # and biggest value possible, which are the negative
        # and positive infinite
        return valid(root, float("-inf"), float("inf"))