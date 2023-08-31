# Solution from a comment in Neetcode's video proposing a time and
# space complexity optimization using a hashset to reduce the time
# (just check the indexes in the inorder once at the beginning 
# instead of every recursion) and reversing the postorder list to
# reduce the space (instead of slicing as we take the first element
# of the list, we first reverse it once, and then just have to pop
# the last element, not creating copies of the list and reducing
# also the time)

# Time complexity: O(n) we go through the nodes once
# Space complexity: O(n) need a hashset to keep track of the indexes
#                   in the inorder list

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # Hashset where the keys are the values in the inorder
        # array and the value the indexes. This way we don't
        # have to use lst.index(value) each recursion, and we
        # just create the hashset once. It's important to
        # consider that this can be done because the values in
        # the Binary Tree are Unique.
        inorderHash = {}
        # Add to the hashset the value of the node as a key and
        # its index as the value
        for i in range(len(inorder)):
            inorderHash[inorder[i]] = i

        # We are going to reverse the preorder so we don't have to
        # slice the lists every recursion, and instead we pop the
        # last value. Before, we took the parent node from the first
        # position of the preorder and then sliced the preorder list
        # so we don't include that node anymore, however, slicing
        # takes O(n) time complexity and creates a copy of the list
        # taking also O(n) space complexity. With this, because we are
        # reversing the list, we can now take the first element, which
        # is now at the end, using pop() without creating more copies
        # and with a time complexity of O(1)
        preorder.reverse()

        # We will use a helper function so we can keep track of the
        # hashset. We pass the preorder list, the hashset with the
        # indexes of the values in the inorder list, and the range
        # of the partition (as it's the first time, it takes the
        # whole length)
        return self.build(preorder, inorderHash, 0, len(inorder) - 1)

    # Helper function that will be called recursively to build the
    # tree.
    def build(self, postorder, inorderHash, start, end):
        # If the left and right pointers haven't crossed each other
        # it means it's a valid partition. However, if the start
        # index is greater than the end, it means it's not and we
        # return nothing
        if start > end:
            return None

        # Get the parent node from the last position of the postorder
        # list (remember that previously we took the first element
        # of this list, but as we reversed it, we now take the last)
        parent = postorder.pop()

        # Get the index of the parent node in the inorder hashset. With
        # this we know the middle of the inorder, and know how many nodes
        # are to the left and right from the parent node
        midIndex = inorderHash[parent]

        # Create a root node with the parent. By default the children are
        # initialized with None
        root = TreeNode(parent)

        # Try to get the left and right children. If the partition that is
        # sent is not valid, it will return None, meaning there's no child
        # in that side. An invalid partition can happen if when getting the
        # mid index, there are no nodes to the left or right of the parent
        # node, in this case, the range that is sent won't cover any nodes
        # and it will return None.
        # Get the left child by sending the postorder list (which doesn't
        # have the parent node anymore), the hashset, and the range from 
        # the left pointer, up to the mid-1. We substract 1 from the index
        # as the index points to the parent node and we shouldn't consider
        # it as part of the left subtree.
        root.left = self.build(postorder, inorderHash, start, midIndex - 1)
        # Get the right child by sending the postorder list (which doesn't
        # have the parent node anymore), the hashset, and the range from 
        # the mid+1 pointer, up to the end. We add 1 to the middle index
        # as the index points to the parent node and we shouldn't consider
        # it as part of the right subtree.
        root.right = self.build(postorder, inorderHash, midIndex + 1, end)

        # Return the root node that already has the subtrees as its children
        return root