# Neetcode.io solution

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    ## Function to create a tree from a list of strings
    # Time complexity: O(n)
    # Space complexity: O(n)
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        res = []

        def dfs(node):
            # Base case. When we reach a null node, we append
            # an N simbolizing that there's no child
            if not node:
                res.append("N")
                return 
            # If it isn't null, we can append the integer
            # value as a string
            res.append(str(node.val))
            # We go all the way to the the left until we find
            # a None value, and then return and start going
            # to the right, each time appending the current
            # node's value to the list before going to its
            # children
            dfs(node.left)
            dfs(node.right)
        # We begin the DFS with the root
        dfs(root)
        # We added all the nodes (and Nones) to a list so
        # we don't have to keep passing and returning it
        # with each call, but now we have to join each
        # element by a delimiter (in this case we chose a
        # comma)
        return ",".join(res)

    ## Function to create a tree from a list of strings
    # Time complexity: O(n)
    # Space complexity: O(n)
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        # Our data is comma delimited as that is the
        # delimiter we used in the serialize function.
        # So we split it into a list to manipulate it easier
        vals = data.split(",")
        # Pointer that will be a member variable in this
        # class so it's global and we don't have to pass it
        # to the functions
        self.i = 0

        def dfs():
            # If the curren val is None, it's represented
            # by an N
            if vals[self.i] == "N":
                # Update the index
                self.i += 1
                # So we return the base case
                return None
            # However, if it isn't None, we add the value as
            # a TreeNode. It's important that we saved it as
            # a string, so we have to convert it to an int
            node = TreeNode(int(vals[self.i]))
            # Update the index
            self.i += 1
            # Do DFS to get the left and then the right
            # subtree
            node.left = dfs()
            node.right = dfs()
            # Return the root node we created
            return node
        # After we create the whole tree, we return the root
        # node that is returned from the dfs()
        return dfs()
        
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))