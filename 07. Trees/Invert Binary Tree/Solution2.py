# Time complexity: O(n) iterate over each node once
# Space complexity: O(1)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # If the received root is empty, it means we
        # have reached a node after a leaf (the end)
        if not root:
            return None

        # Invert the left child with the right one
        # Save the left child as a temporary variable
        # so we can later on update the right child with
        # it
        temp = root.left
        # Go down the tree always taking the left route
        self.invertTree(root.left)
        # After we have reached the end, we start returning
        # from the bottom to the top, updating the left
        # child with the right one
        root.left = root.right

        # Update the right child with the left one
        # Go down the tree taking the right route
        self.invertTree(root.right)
        # Update the right child with the previous left
        root.right = temp

        # Return the root node with the swapped children
        return root