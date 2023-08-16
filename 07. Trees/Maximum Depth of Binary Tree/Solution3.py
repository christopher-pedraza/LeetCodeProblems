# Neetcode.io solution 3

# Time complexity: O(n) we have to go through the whole tree
# to find the deepest node
# Space complexity: O(1) no need of additional data structure

# This solution is using iterative DFS
# We are going to add every node and its children to a stack
# process the current node height and then take it from the
# stack and process its children

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        # Add current node to the stack
        stack = [[root, 1]]
        # Variable where we are going to store the max depth
        res = 0

        # While the stack still has elements
        while stack:
            # Pop a node with it's height
            node, depth = stack.pop()

            # If it's a node and not None
            if node:
                # Calculate if the depth is deeper than the current res
                res = max(res, depth)
                # Append to the stack the children of the node and a depth
                # 1 level deeper than the current
                stack.append([node.left, depth + 1])
                stack.append([node.right, depth + 1])
        # Return the deepest depth calculated
        return res