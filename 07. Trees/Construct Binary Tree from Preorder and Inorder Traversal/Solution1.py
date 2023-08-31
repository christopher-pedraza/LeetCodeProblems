# Neetcode.io solution

# Time complexity: O(n^2) for every node we search in the inorder
#                  array for the value ('lst.index(val)' requires
#                  O(n))
# Space complexity: O(n^2) need to pass sublists for each call in
#                   in the stack

# Two important facts to consider:
# The first value of preorder is always the root.
# When adding a node as a parent in the preorder, we
# check where that value is in the inorder and count
# the number of nodes to the left and right of that
# value. With this count, we can partition the preorder
# array. For example:
# preorder: [3, 9, 20, 15, 7]
# inorder: [9, 3, 15, 20, 7]
# We take the 3 because it's the parent and look for it
# in the inorder
#      preorder: [/, 9, 20, 15, 7]
#      inorder: [9, 3, 15, 20, 7]
#   <- left subtree ^ right subtree ->
# With this we know that there's one node to the left of
# the 3, and three nodes to the right, so we partition the
# preorder as follows:
#  preorder: [parent: 3, left: 9, right: 20, 15, 7]
# As the 9 is alone in the left, we just create that node
# and add it to the left child of the parent
# For the right tree, we now take the first value in the
# preorder, as we already removed the 3 and 9, the next one
# is the 20. 

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # If we don't have any nodes to traverse, we don't create a tree
        if not preorder or not inorder:
            return None

        # Create a tree node with the first value of the preorder array
        # This first value will always be the parent node as we keep
        # removing the previous parents from the array.
        root = TreeNode(preorder[0])

        # Get the index of the value in the inorder array to get the mid
        # point. In this point, all the values to the left will go to the
        # left subtree, while all the values to the right will go the the
        # right subtree.
        mid = inorder.index(preorder[0])

        # Recursively build the trees
        # For preorder, we start at index 1 because we skip the index 0
        # which we already processed as the parent, and end at index mid
        # + 1 to include also the mid point.
        # For the inorder array, we take all the values from the beginning
        # up to the middle point
        root.left = self.buildTree(preorder[1 : mid + 1], inorder[:mid])
        # For preorder we take from the next position from the middle up
        # to the end. This because mid position is part of the left subtree
        # For the inorder we do the same because all values after the mid
        # are part of the right subtree 
        root.right = self.buildTree(preorder[mid + 1 :], inorder[mid + 1 :])

        # At the end of the recursion, we return the root of the built tree
        return root