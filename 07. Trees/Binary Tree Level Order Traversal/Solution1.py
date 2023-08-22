# Same solution as Neetcode.io's one

# Time complexity: O(n) iterate over all the nodes
# Space complexity: O(n) need a deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Queue so we can do BFS. We add the nodes in the
        # current level, then we iterate over them adding
        # to the queue their children, but only popping them
        # and adding them to a list of the current level.
        # This list is added to the complete list of the
        # tree. Next iteration, we go through the children
        # and add their children to the queue without popping
        # them.
        queue = collections.deque()
        # Matrix to store the lists of values in each level
        res = []

        # If the root is not empty, then we append it to the
        # queue
        if root:
            # Append to the queue the root
            queue.append(root)

        # While the queue still has elements
        while queue:
            # Lists of the current level
            currentLevel = []
            # Iterate only over the nodes in the current level
            for i in range(len(queue)):
                # Get a node in the level from the left
                current = queue.popleft()
                # Add that node to the current level list
                currentLevel.append(current.val)
                # If the children are not empty, add them
                # to the queue to the right
                if current.left: 
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)

            # Append to the matrix the list of the current
            # level nodes
            res.append(currentLevel)

        # Return the matrix
        return res