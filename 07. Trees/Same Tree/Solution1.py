# Time complexity: O(n)
# Space complexity: O(1)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # If both of the nodes are None, it means they are the same
        # and we have reached the end
        if not p and not q:
            return True

        # If they are not None, and the values are the same
        elif p and q and p.val == q.val:
            # Check both sides to see if they are the same
        	# Both sides need to return True, for the tree to be the same
        	return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
            
       	# If they are both not None, but the values differ
        else:
        	return False