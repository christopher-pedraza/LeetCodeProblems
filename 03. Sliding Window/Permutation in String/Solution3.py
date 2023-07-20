# From a comment in NeetCode's video

# Time complexity: O(n) ?? for iterating over s2 and
#                          the Counter (I think it's
#                          more than O(n))
# Space complexity: O(n) ?? need the dictionaries (
#                           counters)

# Less efficient than the previous two which are almost
# the same in terms of efficiency

import collections

def checkInclusion(s1: str, s2: str) -> bool:
    # Left and right pointers
    l = 0
    r = len(s1)
    # Counts the frequency of the characters in the string
    s1Count = collections.Counter(s1)
    
    # While the r pointer is less than or equals than the
    # length of s2. If s1 is greater than s2, then we would
    # never enter the loop and return False
    while r <= len(s2):
        # If the required frequency of the characters in s1
        # is found in the slice of the string of s2 from the
        # left to the right pointer, we return True
        if s1Count == collections.Counter(s2[l:r]):
            return True
        # Each iteration move the left and right pointer once
        # As the right pointer starts at the length of s1, the
        # sliding window always remains of the necessary size
        # to find the permutation, if it exists.
        l += 1
        r += 1
    # If the permutation was not found, we return False
    return False

print(checkInclusion("ab", "eidbaooo")) # True
print(checkInclusion("ab", "eidboaoo")) # False
print(checkInclusion("adc", "dcda")) # True