# Time complexity: O(n) - iterate over list of chars in s
# Space complexity: O(n) - 2 lists of size n


def isAnagram(s, t):
    # Check that both words are of the same length
    if len(s) != len(t):
        return False
    
    # Transform the words into lists so I can remove elements
    sL = list(s)
    tL = list(t)

    # Iterate over the elements of sL
    for c in sL:
        # If the character is in tL, I remove it
        if c in tL:
            tL.remove(c)
        # If it's not in tL, not a valida Anagram
        else:
            return False
    
    # If I iterate over all the elements, and never return True
    # it's a valida Anagram
    return True

print(isAnagram("anagram", "nagaram"))
print(isAnagram("rat", "car"))