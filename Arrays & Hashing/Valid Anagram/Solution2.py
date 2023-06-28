# Time complexity: O(nlogn) - counter most common complexity
# Space complexity: O(n) - the strings return as new dicts?

# Not needed in leetcode:
from collections import Counter 

def isAnagram(s, t):
    # Counter counts the frequency of the chars in a string.
    return Counter(s) == Counter(t)

print(isAnagram("anagram", "nagaram"))
print(isAnagram("rat", "car"))