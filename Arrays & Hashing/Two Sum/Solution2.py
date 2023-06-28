# Time complexity: O(n^2) - iterating n times the list of size n
# Space complexity: O(1) - nothing is stored

def twoSum(nums, target):
    # Iterate over all the elements in the list
    for i in range(len(nums)):
        # Iterate over the next elements of i in the list
        for j in range(i+1, len(nums)):
            # If the sum of the numbers in index i and j is target
            # return list with the indexes
            if nums[i]+nums[j] == target:
                return [i, j]

print(twoSum([2,7,11,15], 9))
print(twoSum([3,2,4], 6))
print(twoSum([3,3], 6))