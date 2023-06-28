# Neetcode.io solution

# Time complexity: O(n) - iterate over len(s), dict operations are O(1)
# Space complexity: O(n) - 2 dicts of size n

def isAnagram(s, t):
    # Check if both strings are the same length. If not, they aren't anagrams
    if len(s) != len(t):
        return False

    # Declar hMaps (dicts)
    countS, countT = {}, {}

    # Iterate over the characters of boths strings adding +1 to the dicts
    # The key in the dicts are the chars, so for example, if a appears twice
    # you would add +1 two times.
    for i in range(len(s)):
        # hMap.get(charAsKey, defaultValIfKeyNotPresent) returns the val
        # The val is the frequency of the char
        countS[s[i]] = 1 + countS.get(s[i], 0)
        countT[t[i]] = 1 + countT.get(t[i], 0)

    # Check if both dicts are the same. If so, they are anagrams
    return countS == countT

print(isAnagram("anagram", "nagaram"))
print(isAnagram("rat", "car"))