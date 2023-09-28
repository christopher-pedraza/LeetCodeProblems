class TrieNode:
    def __init__(self):
        # Stores the children of the node. The key of the hashmap contains the
        # value of the child node, thus, we don't have to store the value in
        # this node as the parent will know it
        self.children = {}
        # If the node is the end of a word or not
        self.isEnd = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()
        # We store the max lenght so if we later on receive a word to search
        # that is longer than it, we know right away that we won't find it
        # This is just an optimization, it's not needed for the algorithm to
        # work
        self.max_word_length = 0

    # Time complexity: O(n) as we have to iterate over the n characters of
    # the word
    # Space complexity: O(n) as we have to store in the worst case, the n
    # characters of the word (but sometimes we may reuse nodes)
    def addWord(self, word: str) -> None:
        # Update the max length if the length of the new word is longer than
        # the previous max
        self.max_word_length = max(self.max_word_length, len(word))

        # In order to iterate over the tree
        cur = self.root
        # Iterate over the characters of the word
        for c in word:
            # Check if the character already exists in the children of the
            # current node. If it exists, we just move to the children and
            # continue iterating over the word. When/If we find a character
            # that doesn't exist in the Trie tree, we create a new child
            # TrieNode to represent it
            # If the char is not in the children, we create the node
            if c not in cur.children:
                # Create in the children of the current node, a new node with
                # the key of the current character
                cur.children[c] = TrieNode()
            # Either we go to the already existing child or the child we just
            # created
            cur = cur.children[c]
        # At the end of adding the word, cur is in the end of the word, so we
        # set it as True
        cur.isEnd = True

    # Time complexity: O(n) in the worst case scenario in which we receive
    # just dots, we would have to iterate over every child node in every node
    def search(self, word: str) -> bool:
        # If the length of the word we are searching for is longer than the
        # max length stored, we know we won't find it
        if len(word) > self.max_word_length:
            return False

        def dfs(j: int, root: TrieNode):
            cur = root
            # Iterate over all the characters in the word starting from the
            # position j that we received
            for i in range(j, len(word)):
                c = word[i]
                # If the character is a wildcard
                if c == ".":
                    # As the wildcard can be any character, we will iterate
                    # over all the children of the current node to see if any
                    # of the paths manages to find the word
                    for child in cur.children.values():
                        # We pass the index of the character we are looking for
                        # In this case, we were on the character in position i
                        # so we pass the next character (i+1)
                        # As the dfs is a boolean function, if we ever find a
                        # path that returns true, we return right away true, if
                        # not, we continue until there's no more children and
                        # then return False
                        if dfs(i+1, child):
                            return True
                    return False
                else:
                    # If the character is not in the children, then it doesn't
                    # exist, thus we return false as we couldn't find the word
                    if c not in cur.children:
                        return False
                    # Update the current node to continue searching for the word
                    cur = cur.children[c]
            # After iterating over the word, if the current node is the end of
            # a word, we return true, else, we return false
            return cur.isEnd
        # Call the dfs, at the beginning, the index of the word will be 0, and
        # the current node the root
        return dfs(0, self.root)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)