# Time complexity: O(nlogn) because of the sorting
# Space complexity: O(n)

def topKFrequent(nums, k):
    # Dictionary to store the frequencies
    freq = {}

    # Iterate over the numbers in the input list to get the frequency
    for n in nums:
        # Get the frequency stored in the dictionary (if not present, get 0), and add 1
        freq[n] = 1 + freq.get(n, 0)

    # Sort the frequency dict using the second value of the tuple and reversing the order
    # (greater->smaller)
    freqList = sorted(freq.items(), key=lambda x: x[1], reverse=True)

    # Append into the result list the k numbers with greater frequency and return it
    res = []
    for i in range(k):
        res.append(freqList[i][0])
    return res

print(topKFrequent([1,1,1,2,2,3], 2))
print(topKFrequent([1], 1))