# Time complexity: O(n)
# Space complexity: O(1)

# Go through the left path
# When Node==None, return to parent node
# Add current node to list
# Go through the right side
# Repeat

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # Stack where we are going to be placing the nodes
        # from smallest to greates
        stack = []
        
        # Auxiliary function to go through the tree first
        # through the left, and then through the right
        def getSmallest(root, k, stack):
            # If the root is empty, means we have reached
            # a end of the tree, so we return the current
            # stack
            if not root:
                return stack

            # If we already have k smalles elements, we
            # stop going through the tree, and return the
            # current stack
            if len(stack) > k:
                return stack
            
            # If it has a left child, we go first through the
            # left path
            if root.left:
                getSmallest(root.left, k, stack)
            # Append the current node as it is smaller than 
            # the right child, but bigger than the left one
            # That's why, it's after going through the left
            # but before going to the right. If there's no
            # left child, we will append it as it is the
            # smallest
            stack.append(root)
            # Go through the right side
            if root.right:
                getSmallest(root.right, k, stack)
            # After adding the current node and going
            # through both sides, we return the current
            # stack
            return stack
        
        # Return the kth element's value from the stack
        # of smallest nodes
        return getSmallest(root, k, stack)[k-1].val