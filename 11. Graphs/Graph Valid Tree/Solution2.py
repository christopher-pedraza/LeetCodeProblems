# Neetcode.io's alternative solution

# WASN'T EXPLAINED IN THE VIDEO, THE COMMENTS WERE ADDED BY CHATGPT AS I DIDN'T
# UNDERSTAND IT

# Time complexity: O(ElogV) where E is the number of edges and V is the number of vertices
# Space complexity: O(V) for the parents and heights dictionaries


# alternative solution via DSU (Disjoint Set Union) O(ElogV) time complexity and
# save some space as we don't recreate the graph\tree into an adjacency list prior to DFS
# and loop over the edge list directly
class Solution:
    """
    @param n: An integer
    @param edges: a list of undirected edges
    @return: true if it's a valid tree, or false
    """

    # Find the root of the set to which 'n' belongs
    def __find(self, n: int) -> int:
        # Traverse the path to the root
        while n != self.parents.get(n, n):
            n = self.parents.get(n, n)
        return n

    # Connect two sets represented by 'n' and 'm'
    def __connect(self, n: int, m: int) -> None:
        # Find the root of the set containing 'n'
        pn = self.__find(n)
        # Find the root of the set containing 'm'
        pm = self.__find(m)
        # If already in the same set, do nothing (redundant edge)
        if pn == pm:
            return
        # Union by rank
        if self.heights.get(pn, 1) > self.heights.get(pm, 1):
            # Attach smaller tree under the root of the larger tree
            self.parents[pn] = pm
        else:
            # Attach smaller tree under the root of the larger tree
            self.parents[pm] = pn
            # Update height if necessary
            self.heights[pm] = self.heights.get(pn, 1) + 1
        # Decrement the number of connected components (trees)
        self.components -= 1

    # Check if it's a valid tree
    def valid_tree(self, n: int, edges: List[List[int]]) -> bool:
        # Initialize data structures
        # Dictionary to store the parent of each node
        self.parents = {}
        # Dictionary to store the height of each set (tree)
        self.heights = {}
        # Initially, each node is its own connected component (tree)
        self.components = n

        # Iterate over the edges
        for e1, e2 in edges:
            # Check for a 'redundant' edge
            if self.__find(e1) == self.__find(e2):
                return False
            # Connect the sets represented by 'e1' and 'e2'
            self.__connect(e1, e2)
        # Check if the forest contains one tree
        return self.components == 1
