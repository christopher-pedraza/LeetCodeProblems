# Neetcode.io solution

# Time complexity: O(n) - iterate n times to create frequency dict, n times in frequency list
#                         and n times for each index in frequency list, so O(3n)
# Space complexity: O(n) - freq list and dict of size n, so O(2n)

def topKFrequent(nums, k):
    # Dictionary to store the frequencies
    freq = {}
    # List that stores a list of numbers using the frequency as index
    freqList = [[] for i in range(len(nums)+1)]
    # List to store the result
    res = []

    # Iterate over the numbers in the input list to get the frequency
    for n in nums:
        # Get the frequency stored in the dictionary (if not present, get 0), and add 1
        freq[n] = 1 + freq.get(n, 0)

    # Iterate over the numbers and their frequency
    for key, v in freq.items():
        # Append the key in the frequency index
        freqList[v].append(key)

    # Iterate from the last index (highest freq) to the least
    for i in range(len(freqList)-1, 0, -1):
        # For each number in the index (needed in case the numbers in the index
        # exceed the k numbers required)
        for n in freqList[i]:
            # Append to the result list the number and decrease k val
            res.append(n)
            # if res already has the k numbers needed, it returns it
            if len(res) == k:
                return res

print(topKFrequent([1,1,1,2,2,3], 2))
print(topKFrequent([1], 1))