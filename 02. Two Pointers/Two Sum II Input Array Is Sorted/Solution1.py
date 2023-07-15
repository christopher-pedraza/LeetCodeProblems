# Neetcode.io solution

# Time complexity: O(n) - 1 iteration over the list
# Space complexity: O(1) - no extra space needed

def twoSum(numbers, target):
    # Left and right pointers
    left = 0
    right = len(numbers)-1

    # Guaranteed a solution, so could be while True
    while left < right:
        # Get the current sum of the numbers in the
        # left and right indexes
        currentSum = numbers[left] + numbers[right]

        # If the sum is greater than the target, and
        # considering the list is sorted, you need to
        # decrease the pointer in the right to get a
        # smaller number
        if currentSum > target:
            right -= 1
        # If on the other hand, it's smaller than the
        # targer, we need to increase the left pointer
        # to get a bigger number
        elif currentSum < target:
            left += 1
        # If none of the previous conditions are met, it
        # means we have found our solution, so add 1 to
        # each index (required by the problem) and return
        # a list with them
        else:
            return [left+1, right+1]
    
print(twoSum([2,7,11,15], 9))
print(twoSum([2,3,4], 6))
print(twoSum([-1,0], -1))
print(twoSum([1, 2, 3, 9], 10))