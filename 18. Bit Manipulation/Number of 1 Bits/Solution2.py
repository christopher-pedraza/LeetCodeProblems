# Neetcode's solution

# Time complexity: O(1) because, even if we need to traverse the entire bit representation of the integer, we are guaranteed that it will be a 32-bit
#                  bit, thus it will be O(32)
# Space complexity: O(1) as we don't need any extra space

# For this solution what we are going to be doing is checking whether the last bit is a 0 or a 1 using either modulus operation (%) or AND operation (&)
# After checking, if it's a 1, we will increase the count of 1's we have found, and then shift the bits to the right by 1 position.
#
#
# AND operation:
# For the and operation, we will use the bit representation and apply an AND with a bit representation of 1, so for example, if we had 10001101:
#     10001101
# AND
#     00000001
#    ----------
#     00000001
# In this case we add 1 to the count as we got 1 in the result, then we shift the bits:
#
#     1000110
# AND
#     0000001
#    ----------
#     0000000
# Here we got a 0, so we don't add anything to the count and just shift again. We will keep repeating this process until we only have 0s
#
#
# MOD operation:
# The mod operation would follow the same process, with the difference that we will be using the Modulus operator. This will yield 0 if we have a 0 and
# 1 if we have a 1 in the last position when using %2. This is because we will be dividing by 2 and if we have a 1 in the last position, we will have
# a remainder of 1, and in the case of 0, of 0.


class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n > 0:
            # If the MOD operator yields a 1, we will be adding to the result, otherwise, we will be adding 0 (nothing)
            res += n % 2
            n = n >> 1
        return res


s = Solution()

print(s.hammingWeight(128))  # 1
print(s.hammingWeight(11))  # 3
print(s.hammingWeight(4294967293))  # 31
