# Neetcode.io solution 2

# Time complexity: O(n) we have to go through the whole tree
# to find the deepest node
# Space complexity: O(1) no need of additional data structure

# This solution is using iterative BFS

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # If we reached an empty node, it means the child
        # that was received doen't exist, thus we don't
        # consider this height, and return 0
        if not root:
            return 0

        # Intial level of the root node (as we already checked
        # 'if not root' we know that it has at least 1 level)
        # We are starting it at 0 as we add the root to the queue
        # and add 1 to the level each time we take out the nodes
        # of the current level
        level = 0
        # Add the root to a queue
        q = deque([root])

        # While the queue has elements
        while q:
            # We are going to iterate only over the nodes of the current
            # level. This is done by taking the nodes from the left and
            # appending the children to the right
            for i in range(len(q)):
                # Take the node from the left side of the queue
                node = q.popleft()

                # Append the children of the node to the queue
                # If there's a left child, we append it to the right
                # of the queue
                if node.left:
                    q.append(node.left)
                # If there's a right child, we append it to the right
                # of the queue
                if node.right:
                    q.append(node.right)

            # After taking out the nodes of the current level and
            # adding their children to the queue, we update the value
            # of level
            level += 1

        # Return the last level that was found
        return level