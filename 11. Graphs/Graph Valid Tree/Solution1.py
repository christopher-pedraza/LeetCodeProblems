# Neetcode.io solution

# Time complexity: O(v+e) because we need to create the adyacency
# list and then run dfs through all the nodes
# Space complexity: O(v+e) we need to create an adyacency list
# representation of the graph

# The basic idea is to find if the tree we were given has loops AND
# all of its nodes are connected. If any loop exists, or there are
# nodes that are not connected, then it means it's not a valid
# tree. One way to solve this is to first construct the graph using
# an adyacency list, and then run dfs from one of its nodes marking
# the nodes we are visiting in a visited set. We should be able to
# start from any node as they should all be connected, if any node
# wasn't added to the visited set after running dfs, it means it's
# not a valid tree as not all the nodes are connected. In the other
# hand, if while going through the tree, we arrive at a node that was
# already marked as visited, then it also means it's not a valid tree
# as we found a loop and arrived at an already processed node


class Solution:
    """
    @param n: An integer
    @param edges: a list of undirected edges
    @return: true if it's a valid tree, or false
    """

    def validTree(self, n, edges):
        # If we weren't given any node, then it means the graph is empty
        # But this still counts as a valid tree
        if not n:
            return True

        # We will create our adyacency list
        adj = {i: [] for i in range(n)}
        # Each edge is formed from 2 nodes
        for n1, n2 in edges:
            # As it's an indirect graph, we add both nodes to the adyacency
            # list and the other node as the neighbor
            adj[n1].append(n2)
            adj[n2].append(n1)

        # Visited set to keep track of the nodes we have visited
        visit = set()

        # DFS where we will pass the node to be visited, as well as the previous
        # node so we don't return from the node we just came and return false
        # thinking it's a cycle
        def dfs(i, prev):
            # If the current node has already been visited, we found a loop
            if i in visit:
                return False

            # If it hasn't been visited, we can add it to the visited set
            visit.add(i)

            # Go through the neighbors of the current node
            for j in adj[i]:
                # Except for the node from which we came
                if j == prev:
                    continue
                # Run dfs and if at any time we get a False as a returned value
                # we return False as we detected a loop
                # We pass the neighbor as the new node and i as the previous node
                # as it's the node from which we are comming
                if not dfs(j, i):
                    return False
            # If no loop was found in this dfs traversal, we can return True
            return True

        # If the dfs from the parent node returned True (no loops were found),
        # and we visited all the nodes that existed, we can return True. If
        # any of these conditions doesn't happen, then we return False.
        return dfs(0, -1) and n == len(visit)
