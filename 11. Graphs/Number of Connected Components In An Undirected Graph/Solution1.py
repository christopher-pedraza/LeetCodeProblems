# Neetcode.io's video solution

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

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # Parent and rank lists for every node
        par = [i for i in range(n)]
        rank = [1] * n
        
        # Function to find the parent of a node
        def find(n1):
            res = n1
            # If we found a node that it's the parent of itself we
            # cannot go any higher as it's already the parent
            while res != par[res]:
                # This is an optimization to make the linked list shorter
                # Basically we are updating the parent of the current node
                # to be the grandparent. If there's no grandparent, this line
                # will do nothing (why??)
                par[res] = par[par[res]]
                # Update the current node to its parent to go up the chain
                res = par[res]    
            return res
    
        # Function to unified two parent nodes
        def union(n1, n2):
            # Find the root parents of both nodes
            p1, p2 = find(n1), find(n2)

            # It's possible for both nodes to have the same parent, in this
            # case, we return 0 as we didn't perform any union
            if p1 == p2:
                return 0

            # We make the union considering the parent that has a higher rank
            # to make the tree have an smaller height
            if rank[p2] > rank[p1]:
                # The parent of p1 us now going to be p2
                par[p1] = p2
                # Therefore, we increase the rank of p2 with whatever was in
                # p1 (we just don't add 1 because p1 may already have some nodes
                # as its children)
                rank[p2] += rank[p1]
            else:
                # If the rank of p1 is higher or equals, we make the parent of
                # p2 the node p1, and update the rank of p1
                par[p2] = p1
                rank[p1] += rank[p2]

            # Return 1 simbolizing we did perform a union
            return 1

        # At the begginning, every node is the parent of itself, thus there are
        # n connected components. This value will decrease every time we
        # succesfully perform a union
        connected_components = n
        # Iterate over the edges we were given
        for n1, n2 in edges:
            # Try and joing the nodes of the edge. If both nodes have the same
            # parent, then union() will return 0 as no union will be made and
            # therefore, we will not decrease connected_components. In the other
            # hand, if we do perform a union, the function will return 1,
            # decreasing the count of connected components as now the nodes 
            # are not by themselves, but are united
            connected_components -= union(n1, n2)
        return connected_components