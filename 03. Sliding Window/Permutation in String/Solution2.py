# IMPROVEMENTS:
# First check if s1 is longer than s2, in this case
# return False
# Limit the size of the sliding window to the length
# of s1

# Time complexity: O(m + n) where m is the len of
#                  s1, and n the len of s2
# Space complexity: O(n) - hashmaps needed

def checkInclusion(s1: str, s2: str) -> bool:
    # Hashmaps to store the frequency of the characters
    hMap1, hMap2 = {}, {}
    # Left pointer
    l = 0

    # Get the frequency of the characters in s1 (the chars
    # we are looking for in s2 in any order)
    for c in s1:
        hMap1[c] = 1 + hMap1.get(c, 0)

    # Iterate over the characters in s2 moving the right
    # pointer
    for r in range(len(s2)):
        # For convinience, we get the char in a variable
        c = s2[r]

        # If the char is not even in the chars we are looking
        # for, we move the left pointer to the right pointer
        # (we add one as in the next iteration the right
        # pointer will be there) and reset the hash map
        if c not in hMap1:
            # Move left pointer
            l = r+1
            # Reset the hashmap
            hMap2 = {}
        # If the char is in the hash map, and the quantity we
        # have found is lower than the needed, we add 1 to the
        # frequency of this char
        elif c in hMap1 and hMap2.get(c, 0) < hMap1[c]:
            # Add 1 to the frequency of char c
            hMap2[c] = 1 + hMap2.get(c, 0)
        # If it's in the hMap, but it already has the needed
        # quantity of that char, we move the left pointer 
        # until it's the same as the right pointer, or the
        # quantity is equals to the needed
        else:
            # We add the new char in the right pointer
            hMap2[c] = 1 + hMap2.get(c, 0)
            # Move the left pointer until it's in the same
            # position as the right one, or that the quantity
            # is already the needed one
            while l != r and hMap2.get(c, 0) > hMap1[c]:
                # Remove 1 from the quantity of the char in the
                # left pointer as it's not longer going to be
                # included in the sliding window
                hMap2[s2[l]] = hMap2.get(s2[l]) - 1
                # Move the left pointer 1 pos to the right
                l += 1

        # If both hashmaps are the same, it means we found the
        # correct permutation, meaning it's possible
        if hMap1 == hMap2:
            return True

    # If we finish without ever having the same values in the
    # hashmap, we return false
    return False

print(checkInclusion("ab", "eidbaooo")) # True
print(checkInclusion("ab", "eidboaoo")) # False
print(checkInclusion("adc", "dcda")) # True