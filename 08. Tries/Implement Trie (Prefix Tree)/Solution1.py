# This is a very efficient data structure specifically to check for prefixes
# If we want to know if a word in a list starts with B, we have to iterate
# over the n words checking if there is one, but with a trie tree, we just
# need to check the first level. In this first level, the worst case scenario
# would be that there will be 26 lowercase letters (+26 if we consider upper
# case), thus giving us a time complexity to know if something starts with a 
# certain letter of O(26) => O(1). Also, it can be efficiente in terms of space
# as we have the potential to reuse some nodes when inserting another word

class TrieNode:
    def __init__(self):
        # Stores the children of the node. The key of the hashmap contains the
        # value of the child node, thus, we don't have to store the value in
        # this node as the parent will know it
        self.children = {}
        # If the node is the end of a word or not
        self.isEnd = False

class Trie:
    def __init__(self):
        # The trie tree starts empty and with no children
        self.root = TrieNode()

    # Time complexity: O(n) as we have to iterate over the n characters of
    # the word
    # Space complexity: O(n) as we have to store in the worst case, the n
    # characters of the word (but sometimes we may reuse nodes)
    def insert(self, word: str) -> None:
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

    # Time complexity: O(n) as we have to iterate over the n characters of
    # the word
    def search(self, word: str) -> bool:
        # Start at the root of the tree
        cur = self.root
        # Iterate over the word
        for c in word:
            # If the character is not one of the children we return False
            if c not in cur.children:
                return False
            # Update cur to the child node of the character
            cur = cur.children[c]
        # If at the end cur is in the end of a word, we will return True, but
        # if it isn't at the end, it will return False
        return cur.isEnd

    # Time complexity: O(n) as we have to iterate over the n characters of
    # the word
    def startsWith(self, prefix: str) -> bool:
        # Start at the root of the tree
        cur = self.root
        # Iterate over the word
        for c in prefix:
            # If the character is not one of the children we return as no word
            # starts with the prefix
            if c not in cur.children:
                return False
            # Update cur to the child node of the character
            cur = cur.children[c]
        # If we never returned False, a word starts with that prefix
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)