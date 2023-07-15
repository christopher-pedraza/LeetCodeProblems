# Time complexity: O(m*nlogn) - because of the sorting algorithm * m words in the input
# Space complexity: O(n^2)? - 2 dicts with all the words (first one, in the worst case
#                             that all words are diff, will also be of size n)


def groupAnagrams(strs):
    hMap = {} # sorted words : index
    resHMap = {} # word : index

    # Iterate over the words in the input list
    for i, word in enumerate(strs):
        # w will be the key for the hMap, which is the indexes dict
        # The word is sorted and then transformed into tupple as a list
        # can't be a key in a hMap
        # Sorting usually is in nlogn time.
        w = tuple(sorted(word))

        # Check if the word key isn't in the dict
        # Lookup in constant time
        if w not in hMap:
            # If not, add it as a key and as value, set the current index of the loop
            hMap[w] = i

        # Get the list stored in resHMap, which is a dict with indexes as a key and
        # a list of the words that are anagrams as values
        # If no lists exists, returns empty list
        lst = resHMap.get(hMap[w], list())
        # Append the word to the list. Append doesn't return anything, so can't 
        # do a one-liner
        # Append is in constant time
        lst.append(word)
        # Assign the new list as the value of the dictionary of results
        resHMap[hMap[w]] = lst

    # This already creates a list of the values
    return resHMap.values()

print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
print(groupAnagrams([""]))
print(groupAnagrams(["a"]))