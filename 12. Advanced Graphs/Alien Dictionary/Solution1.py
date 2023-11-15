# Neetcode.io solution

# In general we will be performing a Topological Sort, which involves a Directed
# Acyclical Graph (has directed edges but no cycles)
#
# We will first start going through the words that were given to know the
# order of the letters. The words that were given are already ordered by
# the significant characters. For example, if we have 'gef' before 'tef', it
# means the g is before the t in the alien dictionary. The same goes for
# multiple characters like 'gef' and 'get', in this case, the f goes before
# the t. So we will be going in pairs of words checking until we find a
# character that differs, and that way we will know which character goes first.
#
# For example, lets say we have this list of words:
# wrt
# wrf
# er
# ett
# rftt
#
# We will first compare the two first words and notice that the t and f differ
# so we would know that the t goes before the f:
# wrt
# wrf
#   ^ difference
# So we would be able to create a node in the graph of t going to f:
# t -> f
#
# Now we check the next two words:
# wrf
# er
# ^ diff
# With this we know the w is before the e:
# w -> e
#
# er
# ett
#  ^ diff
# r -> t
# As we already had t in the graph, we can already connect the r to the existing t
# r -> t -> f
#
# ett
# rftt
# ^ diff
# e -> r
#
# And we are able to connect the nodes to create a :
# w -> e -> r -> t -> f
#
# We would then only need to run a traversal (dfs/bfs) to know the order of the
# nodes.

# Edge cases:
# What would happen if we constructed a graph like this:
# w -> e -> r -> t -> f -
# ^---------------------|
# In this case, we have a contradiction so it's not valid (we have a cycle
# meaning a letter is before, but at the same time after another letter)
# We would return an empty string
#
# Another case would be that we have multiple connected components. For example
# if we didn't have the last word of the example, we would have two separate
# connected components:
# r -> t -> f
# w -> e
# This means we have multiple valid orders, it could either be:
# rtfwe
#        or
# wertf
#        or (with bfs)
# wretf
# However, we cannot just run dfs from the beggining and that's it, for example
# A -> B -> C
# |---------^
# If we start from A, we could directly go to C and have AC. Then return to A
# to continue going through the neighbors and go to B and now have ACB, which is
# not valid. Notice that this graph is valid as it doesn't have any cycle,
# however, the order may be ambigous.
# To solve this, we will do a postorder dfs: Go to all the neighbors before
# processing the current node:
# From A, we will go to C without adding A for the moment. For C, as it doesn't
# have neighbors, we will add it to the solution: "C". Then we will return to A
# but still we will not add it, we will now go to B. From B we will go to its
# neighbors, but as C is already processed, we return and now we can add B to the
# solution: "CB". Finally, we can return to A and process it as it doesn't have
# any more neighbors: "CBA". We first process the leaves, and then the roots.
# This solution is reversed, so we will have to reverse it at the end.

# To prevent cycles, we will keep track of the visited nodes in the current path
# as we have done in previous solutions.

# Time complexity: O(n) where n is the number of characters we are given as an
#                  input, we will create a graph of n elements and then traverse
#                  it.
# Space complexity: O(n) where n is the number of characters we are given as an
#                  input as we will have to create a graph with them.


class Solution:
    def alienOrder(self, words: List[str]) -> str:
        # Adjacency list to match all the characters in all the words we received
        # to a set (to ensure we don't have duplicates)
        adj = {char: set() for word in words for char in word}

        # Go through each pair of words (1-2, 2-3, 3-4, etc.)
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            # Get the minimum length from both words
            minLen = min(len(w1), len(w2))
            # If both words have the same prefix, but their lengths differ, it
            # means they are invalid as they are in an invalid order
            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                return ""
            # Go through every single character in the words
            for j in range(minLen):
                # Find the first different charcter between the two words
                if w1[j] != w2[j]:
                    # We will say that the character in word 2 comes after the
                    # character in word 1
                    adj[w1[j]].add(w2[j])
                    # We can break as we only needed the first different character
                    # because we cannot be sure the following characters are in
                    # the correct order (the words we ordered based on the first
                    # different character, so we can only be sure of the order of
                    # that one)
                    break

        # After we built the order, we can start going through it with a dfs
        # postorder traversal
        # {char: bool} False: visited, True: visited & current path. If it doesn't
        # even exist in the dictionary, it means it has never been visited in any
        # path
        visited = {}
        # List to reverse it later
        res = []

        # Pass the current character or node we are visiting
        def dfs(char):
            # If the character has already been visited, we will return whatever
            # is in the visited dictionary for that character. It can either be
            # a False, meaning that it has been visited in another path, or True
            # that it has been visited in this path. This means that if the dfs
            # ever returns true, it means we have detected a loop as we visited
            # the same node in the same path more than once.
            if char in visited:
                return visited[char]

            # Mark the character as visited for the current path
            visited[char] = True

            # Go to every charcter that is a neighbor of the current character
            # We are going to the neighbors BEFORE processing the current node as
            # its a postorder dfs
            for neighChar in adj[char]:
                # If the dfs ever returns True, it means we detected a loop in
                # this dfs calls, so we can return True
                if dfs(neighChar):
                    return True

            # Mark the charcter as if it has been once visited, but not the
            # current path
            visited[char] = False

            # Append to the result AFTER we have gone to all its neighbors the
            # current character. It's important that it's after as its a postorder
            # dfs. This means the result will be in reverse order as we are
            # processing the subsequent characters before the character that
            # should be before them, meaning we would have to reverse the answer
            # at the end to have the correct order
            res.append(char)

        # We can start at any single character in the adjacency list. We will
        # build the res list when calling dfs to all the characters
        for char in adj:
            # If the dfs ever returns a True, it means we detected a loop
            if dfs(char):
                return ""

        # Reverse the list and convert it to a string by joininig the characters
        # in the list
        res.reverse()
        return "".join(res)
