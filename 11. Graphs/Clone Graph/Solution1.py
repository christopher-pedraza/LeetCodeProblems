# Neetcode.io solution

# Time complexity: O(V+E) where V is the number of vertices and E the
#                  number of edges. In general, it's O(n)
# Space complexity: O(V+E) as we are creating an exact deep copy of
# the graph

# Basically we are going to use a Hashmap to keep track of the nodes we
# have already created a copy, where we map the original nodes to the
# created ones. When we arrive at a node, we create a copy if it doesn't
# exist in the hashmap and using DFS, we go to its neighbors. If the
# neighbor is already in the hashmap, we only create the connection from
# the node we came, to it. This is done by returning the already copied
# node and in the function call of DFS appending to the node's neighbors
# the returned node. However, if it isn't in the hashmap, we first create
# the copy, add it to the hashmap so we know it has already been copied,
# and return the node to the function call to create the connection as
# the neighbor of the node that called it. As it's recursive, we will
# at the end return to the already created nodes to explore all the
# neighbors in case we haven't explored some, and create the connections
# to the copied neighbors.

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

# Import added by leetcode
from typing import Optional


class Solution:
    def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:
        # Hashmap to map the old nodes to the new nodes
        oldToNew = {}

        # DFS to go to the neighbors from the current node.
        # We pass the node we are visiting
        def dfs(node):
            # If the node is already in the hashmap, it means we already
            # made a clone, so we only return it (the clone)
            if node in oldToNew:
                return oldToNew[node]

            # If we haven't created it, we create a new node using the
            # Node constructor, and passing the original value to it
            node_copy = Node(node.val)
            # We add to the hashmap the copy so we later know we already
            # created the copy. We map the original node (key) to the
            # copied node (value)
            oldToNew[node] = node_copy

            # We go through all the neighbors of the original node (the
            # copied node still doesn't have any neighbors as we just
            # created it with the value, so we are going to create the
            # connections here)
            for nei in node.neighbors:
                # dfs(neighbor) will return the copy of the neighbor
                # We append to the neighbors of the current copied node
                # the copy of the neighbor returned from the dfs call
                # (remember the call can either return a node that was
                # already in the hashmap as it was already copied, or a
                # newly copied node)
                node_copy.neighbors.append(dfs(nei))
            # Return the copied node with the original value and the
            # neighbors mapped to the copied original neighbors
            return node_copy

        # Return the node returned from performing a dfs from the original
        # node if it isn't None from the beginning
        return dfs(node) if node else None
