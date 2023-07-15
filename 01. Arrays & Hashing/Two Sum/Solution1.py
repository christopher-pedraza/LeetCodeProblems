# Neetcode.io solution

# Time complexity: O(n) - iterating once over the list
# Space complexity: O(n) - as it's needed a new hashmap with worst case size n

def twoSum(nums, target):
    # Using a dictionary so I can access the indexes of the numbers
    # in constant time
    hMap = {}

    # Iterate over the numbers in list
    for i, n in enumerate(nums):
        # Check the number that is needed if you use n as one of the two
        diff = target - n

        # Check if the needed number is in the hMap, if so, the current number+diff = target
        if diff in hMap:
            return [hMap[diff], i]

        # If current+diff != target, add current to the hMap to continue checking
        hMap[n] = i

print(twoSum([2,7,11,15], 9))
print(twoSum([3,2,4], 6))
print(twoSum([3,3], 6))