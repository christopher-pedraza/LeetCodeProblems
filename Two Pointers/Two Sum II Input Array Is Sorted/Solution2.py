# Time complexity: O(n) - 1 iteration over the list
# Space complexity: O(1) - no extra space needed

def twoSum(numbers, target):
    # Iterate over the numbers
    for i, n in enumerate(numbers):
        # Get the difference needed to get to the target using n
        diff = target - n
        # Check if diff is in the rest of the numbers
        if diff in numbers[i+1:]:
            # Add one to each of the indexes (required by the problem)
            # In the function index, I pass i+1 as the starting point
            # to look for the index of the number. This is done in case
            # there's a repeated number
            return [i+1, numbers.index(diff, i+1)+1]

print(twoSum([2,7,11,15], 9))
print(twoSum([2,3,4], 6))
print(twoSum([-1,0], -1))
print(twoSum([1, 2, 3, 9], 10))