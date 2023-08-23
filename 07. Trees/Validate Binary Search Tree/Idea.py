# Problem:
# The algorithm checks if the current subtree is valid
# however, it doesn't keep track of the previous nodes,
# so you could have a valid subtree of for example:
#     10
#    /  \
#   8   12
# But that subtree be inside a tree that makes one of
# its nodes not valid, for example:
#     9
#      \
#      10
#     /  \
#    8   12
# In this case, even if the 8 is smaller than the 10,
# making the subtree a valid BST, the 8 is also smaller
# than the 9, so it should be in the left side of the
# tree, making the tree an invalid BST

# Time complexity: O(n) go through all the nodes
# Space complexity: O(1) no extra data structure

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        left, right = True, True
        if root.left:
            left = self.isValidHelper(root.left, root.val)
        if root.right:
            right = self.isValidHelper(root.right, root.val)

        return (left and right)
        
    def isValidHelper(self, root, previous):
        # If the current node is empty, return True
        # because it's the end of the tree
        if not root:
            return True

        if root.val == previous:
            return False

        # Variables to store if the right and left
        # children are valid for a BST
        isLeftCorrect, isRightCorrect = True, True

        # If there's a left child, we check if its
        # value is lower than the root's value. If
        # There's no child, we keep the True
        if root.left:
            isLeftCorrect = (root.left.val < root.val and
                            root.left.val > previous)
        
        # If there's a right child, we check if its
        # value is lower than the root's value. If
        # There's no child, we keep the True
        if root.right:
            isRightCorrect = (root.right.val > root.val and
                            root.right.val < previous)

        # Return True if the left and right children are
        # valid for a BST, and the children of them are
        # also valid
        return (isLeftCorrect and
                isRightCorrect and
                self.isValidHelper(root.left, min(root.val, previous)) and
                self.isValidHelper(root.right, max(root.val, previous)))
