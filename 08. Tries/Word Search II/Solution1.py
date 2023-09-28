# Neetcode.io solution

# One brute force solution would be to do a BFS over the entire
# matrix searching for each one of the words. For each and every
# cell in the matrix, we would run a dfs going to all four
# directions to see if we can find the word. Obviously we cannot
# repeat the same cell, so we wouldn't go in cycles, but still,
# it would have a time complexit for each cell of O(4^mn) as for
# each cell we go in the four directions and it grows
# exponentially. Now, for the entire matrix, as there are m*n
# cells, it would be O(mn*4^mn), and for the w words we have to
# check O(wmn*4^mn). This wouldn't be that efficient, thus we
# will use a Trie tree. To optimize this, we can check all the
# words that can be built starting at every cell, thus we remove
# the constant w from the complexity. Based on the prefix of 
# the words, we can ignore the check for certain words starting
# at certain cells. For example, if the cell has an 'A', we
# will only run a DFS for the words that also start with 'A',
# and ignore any other words (e.g. 'BAT')

# 1. Add all the words to the prefix tree
# 2. Use DFS from each cell while going through the Trie Tree
# to see if we have a word with the prefix we are forming by
# doing dfs through the matrix.
# 3. If we reach an end of a word in the Trie Tree, we know we
# can form a word from the input with the matrix, thus we add
# it to the results.
# 4. If at any point the prefix formed by doing dfs over the
# matrix isn't in the Trie Tree (meaning it wasn't in the input
# words), we can return from that path of the matrix to check
# the other 3 directions (left, right, top, bot).

# Note: This data structure is great for this solution because
# if for example, we are in a cell in the matrix with the value
# 'C' and no word in the input starts with 'C', with the Trie
# Tree we will know right away in O(1) as the root node won't
# have a child with the value 'C'. This is the same for when
# we are going through the matrix with dfs. When we create a
# prefix that doesn't appear as a child of the current node of
# the tree, we know we can return as no word will be found from
# that path.

class TrieNode:
    def __init__(self):
        self.children = {}
        # If the node is the end of the word
        self.isWord = False
        # Counts the times the character that is described
        # by the node appears. This is useful so we can remove
        # the node when removing words if the word we are
        # removing is the only one that still uses the node
        # We are not actually going to remove the node, but
        # rather, if the counter of the node is less than 1
        # the code knows that the node is not used by any
        # word that is in the Trie Node, practically removing
        # it
        self.refs = 0

    def addWord(self, word):
        # Current will be in the root node
        cur = self
        # As the current node is used for the word, we add
        # one to its counter
        cur.refs += 1
        # Iterate over the chars in the word
        for c in word:
            # If the char is not in the children
            if c not in cur.children:
                # Create a TrieNode with the value of the char
                cur.children[c] = TrieNode()
            # Move the current node to the child
            cur = cur.children[c]
            # Add 1 to the counter of the current node
            cur.refs += 1
        # Mark the last node as the end of the word
        cur.isWord = True

    # Function to prune the tree from the words that have
    # already been found
    def removeWord(self, word):
        # Start at the root node
        cur = self
        # Reduce the references of this node as it will no
        # longer be used by the word we are removing
        cur.refs -= 1
        # For every character in the word
        for c in word:
            # If the character is in the children
            if c in cur.children:
                # We move the current node to the child as
                # we already reduced the counter of the
                # current node
                cur = cur.children[c]
                # And reduce the counter of the node
                cur.refs -= 1


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        # For every word in the input, we add it to the Trie
        # Tree
        for w in words:
            root.addWord(w)
        # Get the dimensions of the board
        ROWS, COLS = len(board), len(board[0])
        # Result is a set of words we find so we don't
        # repeat them and have duplicates
        # Visited helps so we don't repeat the same character
        # twice and remain in a loop
        res, visit = set(), set()

        # DFS receives the current coordinates (r, c), the
        # current node in the Trie which we are comparing
        # with the char in the matrix, and the word we have
        # formed by the moment we call DFS (the path we have
        # taken at the moment)
        def dfs(r, c, node, word):
            if (
                # If rows or columns are out of bounds
                r not in range(ROWS) 
                or c not in range(COLS)
                # If the character in the current cell is
                # not in the children of the Trie Node
                or board[r][c] not in node.children
                # If the node has a refs less than 1, it means
                # the node isn't used by any word that is still
                # in the Trie Tree. It could have been used by
                # a word, but when removed, the node is no
                # longer needed. This way we are prunning the
                # Tree
                or node.children[board[r][c]].refs < 1
                # If the current position has already been
                # visited
                or (r, c) in visit
            ):
                return

            # Mark the position as visited temporarilly
            # We will later remove it from visited, but
            # this prevents returning to this cell when we
            # started from here
            visit.add((r, c))
            # We update the node with the one we are visiting
            node = node.children[board[r][c]]
            # Update the word by adding the character in the
            # cell
            word += board[r][c]
            # If the node is the end of a word, we know we
            # found a word in the path (doesn't mean we can't
            # find more words, so we will after this continue
            # with the dfs)
            if node.isWord:
                # Update the current node so it's no longer
                # detected as the end of a word and added to
                # the answer set
                node.isWord = False
                # Add to the result 
                res.add(word)
                # Remove the word from the Trie Tree so we
                # don't find it again and can optimize our
                # search (as we already found the word, we
                # can stop going through the tree from the
                # beginning because it will not be found in
                # the tree and the first if-condition will
                # return)
                root.removeWord(word)

            # Recursive case of dfs going to the 4 directions
            dfs(r + 1, c, node, word)
            dfs(r - 1, c, node, word)
            dfs(r, c + 1, node, word)
            dfs(r, c - 1, node, word)

            # Once we are done with this position, we remove
            # it from visited so we can use it again in the
            # path from another cell.
            visit.remove((r, c))

        # Call DFS from each cell as its starting position
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, root, "")

        # Convert the result set into a list
        return list(res)