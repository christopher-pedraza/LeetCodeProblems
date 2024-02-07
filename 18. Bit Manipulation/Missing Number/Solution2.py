# Time complexity: O(n)
# Space complexity: O(1)

# The problem will give you a list of n numbers that are inside the range of [0, n]. Therefore, we have n+1
# possible numbers, but we only have in the list n numbers. We need to return that missing number.

# Possible solutions:
# 1. We can use the formula of the sum of the first n numbers, which is n*(n+1)/2. We can subtract the sum of the
#    list from the sum of the first n numbers, and we will get the missing number.


class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        # Solution 1
        # Getting the length of the list is O(1)
        n = len(nums)
        # Getting the sum of the list is O(n)
        # The formula n * (n + 1) / 2 gives us the sum of the first n numbers, so by then substracting the
        # actual sum of the list, we can know what is the missing value as it will be the difference from the
        # actual sum and what we have.
        return int(n * (n + 1) / 2 - sum(nums))


s = Solution()

print(s.missingNumber([3, 0, 1]))  # 2
print(s.missingNumber([0, 1]))  # 2
print(s.missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1]))  # 8
print(s.missingNumber([0]))  # 1
