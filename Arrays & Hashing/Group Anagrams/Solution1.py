# Neetcode.io solution

# Time complexity: O(m * n * 26) -> O(m*n) where m is the quantity of words and n the average
#                                           size of each word
# Space complexity: O(n) as a new dictionary is needed to store the words grouped by anagrams

# Not needed in leetcode:
from collections import defaultdict 

def groupAnagrams(strs):
    # Creating a defaultdict so I can declare an empty list as the default value
    ans = defaultdict(list)

    # Iterating over the words in the input
    for s in strs:
        # List of 26 zeros representing the 26 chars from a to z
        # This will serve as the key for the anagrams. Any word with the
        # same combination and quantity of chars will be an anagram
        count = [0] * 26
        # Iterating over the chars in the word
        for c in s:
            # Adding 1 to the position of the char
            # Substracting the value of a so a can be index 0.
            #   Ex. a is 97, so 97-97 = 0
            #       b is 98, so 98-97 = 1 ...
            # ord transforms a char into an int value
            count[ord(c) - ord("a")] += 1
        # Converting the list into a tuple so it works as a list and appending
        # the word into that key
        ans[tuple(count)].append(s)

    # Values already created a list of the elements in the dictionary
    # In this case, a list of lists
    return ans.values()

print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
print(groupAnagrams([""]))
print(groupAnagrams(["a"]))