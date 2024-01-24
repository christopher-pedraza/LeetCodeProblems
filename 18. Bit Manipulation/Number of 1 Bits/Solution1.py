# Neetcode's solution

# SOLUTION2 IS EASIER TO UNDERSTAND AND COME UP WITH AND JUST MARGINALLY SLOWER THAN THIS SOLUTION (BOTH ARE STILL O(1))

# Time complexity: O(1) as we are guaranteed that the input will be a 32-bit integer, thus it won't grow with the input. Also, we will only be running
#                  the amount of 1s there is in the input integer because of the operation we are doing each iteration
# Space complexity: O(1)

# What we will be doing is removing each iteration the right most 1 from the input bit representation and adding 1 to the result count. To remove the
# right most 1 we will be performing the operation over the input AND with the input-1 "n = n & (n-1)". Everytime we do n-1, we are removing the right
# most 1 and adding 1s to all the positions to the right of that position. This is not a problem as we will be using the operator AND, so all those extra
# 1s will be removed. For example:
#
# n = 10000001   ->   n-1 = 10000000
# res = 1
#
#     10000001
# AND
#     10000000
#    ----------
#     10000000
#
#
# n = 10000000   ->   n-1 = 01111111
# res = 2
#
#     10000000
# AND
#     01111111
#    ----------
#     00000000
#
# We already arrived at all 0s by just performing the operation 2 times and arriving at the correct count of two 1s.


class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        # while n is equal to while n is not equal to 0 (or "while n>0")
        while n:
            # Remove the right most 1 by using "n = n & (n-1)"
            n &= n - 1
            # Increment the count
            res += 1
        return res


s = Solution()

print(s.hammingWeight(128))  # 1
print(s.hammingWeight(11))  # 3
print(s.hammingWeight(4294967293))  # 31
