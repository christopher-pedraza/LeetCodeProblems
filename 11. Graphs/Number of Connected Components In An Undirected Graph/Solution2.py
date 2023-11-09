# Neetcode.io's website solution

# Time complexity: O(v+e) where v are the vertices and e the edges
# Space complexity: O(v) for every node we are storing its parent
#                   and the rank (nodes connected to it)

# Solution:
# Basically we will have 2 data structures: parent and rank. This can
# be lists. parent will have the nodes represented in the list by the
# index of them, and the value in that position will tell us who is the
# parent. For example, in this parent list:
# parent = [0, 0, 2]
# We know that node 0 and 1 have both 0 as their parent. The node 0 will
# be the parent of itself. And node 2 has as its parent itself.
#
# The other list uses also the index as the identifier of the node, and
# as its value is the number of nodes to which it is parent. For example:
# rank = [2, 1, 1]
# In this case we know that node 0 is the parent of 2 nodes, while node
# 1 and 2 are just the parents of 1 node (themselves)
# This is useful to optimize the algorithm. If we want to connect a node
# to another one, but the other node is already connected to a parent
# node that has more connections, then it would be better to connect the
# new node to the "global" parent so it doesn't form like a stair, and
# instead we form a tree with a smaller height. For example:
# Instead of joining node C to B and forming this:
# A       rank: 2
#  \
#   B     rank: 1
#    \
#     C
# We can join it to A which already has as a rank 2 (B and itself), while
# B has as a rank 1 (just itself)
#    A    rank: 3
#   / \
#  C   B  rank: 1, 1
#
# Another thing we will keep track is the number of connections. We will
# start the counter with the number of nodes, as at the beginning, all
# the nodes will be the parents of themselves and will have no other nodes
# as their children. However, when making a union between nodes, we will
# decrease this value by 1, meaning we have one less section of connected
# components (as 2 individual nodes/sections are now one). It's important
# that we only decrease this value if the nodes in the edge we are
# exploring aren't already children of the same parent, if so, it means
# they are already connected and we wouldn't need to decrease the counter
# as we are not making any new union.

# Another way to solve the problem instead of UnionFind is using DFS
# We could do an adyacency list from the list of edges that we received
# and then run DFS from each node marking the nodes through which we
# pass as visited. After doing every dfs run, we increase a counter
# of connected components. Then we continue iterating through the nodes
# and running dfs from the node if it isn't in the visited set
# This solution would have a time complexity of O(v+e) where v are the
# vertices and e the edges.


class UnionFind:
    def __init__(self):
        self.f = {}

    def findParent(self, x):
        y = self.f.get(x, x)
        if x != y:
            y = self.f[x] = self.findParent(y)
        return y

    def union(self, x, y):
        self.f[self.findParent(x)] = self.findParent(y)


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        dsu = UnionFind()
        for a, b in edges:
            dsu.union(a, b)
        return len(set(dsu.findParent(x) for x in range(n)))


# Define a class called UnionFind
class UnionFind:
    # Initialize an empty dictionary to store the parent of each element
    def __init__(self):
        self.parent = {}

    # Find the parent of element x using path compression and return it
    def findParent(self, x):
        # Get the parent of x from the dictionary, or x if it is not in the dictionary
        y = self.parent.get(x, x) 
        # If x is not its own parent
        if x != y: 
            # Recursively find the parent of y and set it as the parent of x
            y = self.parent[x] = self.findParent(y) 
        # Return the parent of x
        return y 

    # Unite the sets containing elements x and y by making the parent of the root of one
    # node the root of the other one
    def union(self, x, y):
        # Set the parent of the root of the set containing x to the parent of the root of
        # the set containing y
        # Assign the parent of y to be the parent of x. In other words, it is merging the
        # two sets represented by x and y by making the parent of the representative of set
        # x be the representative of set y.
        self.parent[self.findParent(x)] = self.findParent(y) 

class Solution:
    # Count the number of connected components in an undirected graph represented by a list
    # of edges
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # Create an instance of the UnionFind class
        dsu = UnionFind()
        # Iterate over the edges, uniting the sets containing the endpoints of each edge
        for a, b in edges:
            dsu.union(a, b)
        # Return the number of unique parents in the UnionFind data structure, which corresponds
        # to the number of connected components in the graph
        return len(set(dsu.findParent(x) for x in range(n)))