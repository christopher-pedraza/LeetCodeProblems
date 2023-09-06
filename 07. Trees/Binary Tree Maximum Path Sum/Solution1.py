# Neetcode.io solution

# Things to consider:
# 1. There can be negative values inside a path so
#    we have to determine if adding the negative
#    value will later on in the path yield a bigger
#    output.
# 2. You can only split once from any node to form
#    a path, beause if we wanted to split twice, we
#    would be repeating the node.
# 3. When we use a node and its two children, we no
#    longer can use its parents.
# 4. When computing the max from going to the left
#    and going to the right without splitting, also
#    get the max from 0 (ex. max(L, R, 0)), in case
#    the maximum from the left and right are
#    negative, we wouldn't want to include them.

# Steps:
# 1. Select the root node as the top most
# 2. Start going doing the tree taking each child as
#    the top most and calculate the max sum if we
#    didn't from there (it's recursive, so we will
#    keep going down, and then use the answers for
#    the nodes higher in the tree). First we will
#    check what would be the max sum if we went only
#    left, then only right.
# 3. Then we check the max value if we were to split.
#    To do this, we just take the max value of going
#    to the left without ever splitting, and going to
#    the right withoute ever splitting and add it to
#    the value of the current node that is current the
#    top most node.
# 4. We update if needed the value of result if the
#    calculated sum is bigger than the previous
# 5. Return to the parent node the sum of the current
#    node + the max sum from going to the left and
#    right without splitting which will be for the 
#    parent node the max value from going right/left
#    from it without splitting.
# 5.1. Basically for each node, we will return the max
#      sum by going thru the left/right without spliting
#      beause if we split, we wouldn't be able to use
#      the parent node

# Time complexity: O(n)
# Space complexity: O(h) where h is the height of the tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
    	# Add the res to a list so we can edit it easier in the
    	# recursive function. We are only going to be using the
    	# first value
        # If we didn't want to use a global variable, we could
        # return two values from the dfs -> the max sum when
        # splitting, and the max sum without splitting
        # (currently only returning the later)
        res = [root.val]

        # Return max path sum without split
        def dfs(root):
        	# If the root is none, it means we have reached the
        	# end
            if not root:
                return 0

            # Get the max without splitting from the left and the
            # right
            leftMax = dfs(root.left)
            rightMax = dfs(root.right)

            # If the max is negative, we will make it 0 so we don't
            # reduce the value of the path
            leftMax = max(leftMax, 0)
            rightMax = max(rightMax, 0)

            # Compute max path sum WITH split
            # To do this, we get the max from the previous max path sum
            # and the current node's value+leftMax+rightMax (this maxs
            # are without splitting and if they were negative were
            # changed to 0). With this we update the new max path sum
            res[0] = max(res[0], root.val + leftMax + rightMax)

            # Return the path without splitting. So we add the current
            # node's value + the max from the left or right
            return root.val + max(leftMax, rightMax)

        # Start doing DFS with the root
        dfs(root)
        # Return the max path sum
        return res[0]