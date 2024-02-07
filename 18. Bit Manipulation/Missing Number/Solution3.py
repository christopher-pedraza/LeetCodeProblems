# Time complexity: O(n)
# Space complexity: O(1)

# Possible solutions:
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


class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        res = len(nums)
        for i in range(len(nums)):
            res ^= i ^ nums[i]
        return res


s = Solution()

print(s.missingNumber([3, 0, 1]))  # 2
print(s.missingNumber([0, 1]))  # 2
print(s.missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1]))  # 8
print(s.missingNumber([0]))  # 1
