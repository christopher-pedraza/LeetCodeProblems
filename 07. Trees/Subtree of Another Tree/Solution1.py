# Neetcode.io solution

# Time complexity: O(s*t) where s is the size of the 'root'
#                  tree and t the size of the 'subRoot' tree
# Memory complexoty: O(1)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: TreeNode, subRoot: TreeNode) -> bool:
        # If the subtree is empty, then it will obviously be a subtree
        # of the other tree, regardless of the values the other tree
        # has
        if not subRoot:
            return True
        # However, if the subtree is not empty, but the tree is, then
        # the subtree cannot be a subtree of the tree as a tree
        # with values cannot be the subtree of an empty tree
        if not root:
            return False

        # Compare both trees from the current node
        # If both of the trees are the same, we return true, if not
        # we will check for the children of the tree
        if self.isSameTree(root, subRoot):
            return True
        # Check for the right and left children of root. If any of them
        # returns true, then it means the subRoot was found in the root
        # tree in one side of the tree
        return (self.isSubtree(root.left, subRoot) or 
                self.isSubtree(root.right, subRoot))

    # Helper function to check if from the given nodes, the trees are the same
    def isSameTree(self, s: TreeNode, t: TreeNode) -> bool:
        # If both of the nodes are None, it means they are the same
        # and we have reached the end
        if not s and not t:
            return True

        # If they are not None, and the values are the same
        elif s and t and s.val == t.val:
            # Check both sides to see if they are the same
            # Both sides need to return True, for the tree to be the same
            return (self.isSameTree(s.left, t.left) and
                    self.isSameTree(s.right, t.right))
            
        # If they are both not None, but the values differ
        else:
            return False