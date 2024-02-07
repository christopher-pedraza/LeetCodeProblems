# Neetcode.io solution

# Time complexity: O(n) as we need to iterate to sum all the elements in the list
# Space complexity: O(1)

# The problem will give you a list of n numbers that are inside the range of [0, n]. Therefore, we have n+1
# possible numbers, but we only have in the list n numbers. We need to return that missing number.

# Possible solutions:
# 1. We can use the formula of the sum of the first n numbers, which is n*(n+1)/2. We can subtract the sum of the
#    list from the sum of the first n numbers, and we will get the missing number. (Solution2.py)
# 2. We can use the XOR operation to find the missing number. We can iterate through the list and XOR the index
#    with the value of the list. The result will be the missing number. A good property of the XOR is that you
#    can chain them and still be able to get the correct result. Also, what the XOR does is that whenever we have
# 	 the same number, it will return 0, and when we have a mismatched value (0 and 1) we will get 1. Therefore, we
# 	 can use this property to find the missing number:
#    5 ^ 5 = 0
#    101 ^ 101 = 0
#
#    5 ^ 5 ^ 3 = 3
#    101 ^ 101 ^ 011
#       000    ^ 011 = 011
#    This is useful as we can XOR the range 0 to n with the input list and all the duplicates will cancel each
#    other out, and we will be left with the missing number:
#    input = [3, 0, 1]   ^   [0, 1, 2, 3]
#            3 ^ 0 ^ 1       ^ 0 ^ 1 ^ 2 ^ 3
#    0 ^ 0 ^ 1 ^ 1 ^ 3 ^ 3 ^ 2 = 2
# 3. We can use the sum of the range from 0 to n and subtract the sum of the list. The result will be the missing
#    number. (Solution1.py)


class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        # Initialize it with the length of the list to include the last number as the loop is from 0 to n-1
        res = len(nums)

        # The loop will add the values from the complete range (ex. 1, 2, 3, 4, 5), while at the same time
        # subtract the values from the list. The result will be the missing number.
        for i in range(len(nums)):
            res += i - nums[i]
        return res


s = Solution()

print(s.missingNumber([3, 0, 1]))  # 2
print(s.missingNumber([0, 1]))  # 2
print(s.missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1]))  # 8
print(s.missingNumber([0]))  # 1
