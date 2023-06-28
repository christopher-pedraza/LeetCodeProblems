# Time complexity: O(n)
# Space complexity: O(n)

def topKFrequent(nums, k):
    # Dictionary to store the frequencies
        freq = {}
        # List that stores a list of numbers using the frequency as index
        freqList = [None] * (len(nums)+1)
        # List to store the result
        res = []

        # Iterate over the numbers in the input list to get the frequency
        for n in nums:
            # Get the frequency stored in the dictionary (if not present, get 0), and add 1
            freq[n] = 1 + freq.get(n, 0)

        # Iterate over the numbers and their frequency
        for key, v in freq.items():
            # If the frequency-index is None, it means no number has been added
            if freqList[v] is None:
                # Add the number as a new list
                freqList[v] = [key]
            # Else, append the number to the other numbers in the same index (frequency)
            else:
                freqList[v].append(key)

        # Iterate from the last index (highest freq) to the least
        for i in range(len(freqList)-1, 0, -1):
            # If k still requires a number and the index is not None
            if k > 0 and freqList[i] is not None:
                # For each number in the index (needed in case the numbers in the index
                # exceed the k numbers required)
                for n in freqList[i]:
                    # If k still requieres number
                    if k > 0:
                        # Append to the result list the number and decrease k val
                        res.append(n)
                        k -= 1

        return res

print(topKFrequent([1,1,1,2,2,3], 2))
print(topKFrequent([1], 1))