# Neetcode.io solution

# IT'S BETTER MY SOLUTION (Solution2.py)

# Time complexity: O(logn)
# Space complexity: O(1)

# If the middle value is greater or equals
# (equals in order to consider edge case in
# which there's only one or two elements in
# the array) than the value in the left
# pointer, we need to search the right side.
# This is because we know that when we
# rotate an array, the greater values are
# the ones that are going to go to the left
#
# For example:
# [1, 2, 3] -> [3, 1, 2] -> [2, 3, 1]
#           1R           1R
#
# In this case, if 3 is the middle, and
# is greater than the value in the left
# pointer which is 2, then it means it
# belongs to the left side the 3 (as they
# are ordered in ascending order), therefore
# we need to search for the minimum at the
# right side. If on the other hand, it's
# smaller, then we know that the minimum
# should be at the left.
# 
# For example:
# [1, 2, 3, 4, 5] -> [1, 2, 3, 4, 5]
#                 5R
#
# Here, after 5 rotations, the middle will
# be in the 3, which you would have to update
# the minimum with the left side and break
# out of the loop

def findMin(nums: list[int]) -> int:
    # Stores one value as the minimum temporarily
    res = nums[0]

    # Left and right pointers
    l, r = 0, len(nums)-1

    # Binary search until the pointers cross each
    # other
    while l <= r:
        # If the number at the left is smaller than
        # the one at the right, we update our min
        if nums[l] < nums[r]:
            res = min(res, nums[l])
            break

        # Middle pointer
        m = (l + r) // 2
        # Update the minimum if the middle value is
        # smaller
        res = min(res, nums[m])

        # If the value in the middle is greater than
        # the value at the left, then we search the
        # right side
        if nums[m] >= nums[l]:
            # Move the left pointer to search the
            # right side
            l = m + 1
        # Middle value is part of the right sorted
        # portion, so we search the left side
        else:
            # Move the right pointer to search the
            # left side
            r = m - 1

    # Return the minimum value
    return res


print(findMin([3,4,5,1,2])) # 1
print(findMin([4,5,6,7,0,1,2])) # 0
print(findMin([11,13,15,17])) # 11
print(findMin([-500])) # -500
print(findMin([-500, 500])) # -500