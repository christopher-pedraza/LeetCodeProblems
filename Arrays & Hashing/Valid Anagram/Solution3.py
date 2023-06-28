# Time complexity: O(nlogn) - sorting
# Space complexity: O(n) - the sorted strings return as new lists?

def isAnagram(s, t):
    # Gets a sorted array of each of the strings
    # If they are equal, they are anagrams
    # Ex. car -> acr
    #     arc -> acr
    # Valid anagrams!

    # Cannot do s.sort as the strings don't have that method
    return sorted(s) == sorted(t)

print(isAnagram("anagram", "nagaram"))
print(isAnagram("rat", "car"))