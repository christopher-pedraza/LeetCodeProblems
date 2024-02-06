# Neetcode.io solution

# Time complexity: O(32) so it's constant time O(1)
# Space complexity: O(1)

# To know if a value is a 0 or a 1, we can AND it with a 1:
# 0 & 1 = 0
# 1 & 1 = 1
#
# We can also shift the bits to the right and left by one position using << and >>:
# Shifting 01 to the left by one position gives us 10 as we are moving the bits to the left and adding
# a 0 at the rightmost position
# 01 << 1 = 10
# Shifting 10 to the right by one position gives us 01 as we are moving the bits to the right and removing
# the rightmost bit
# 10 >> 1 = 01
#
# Combining these two operations, we can iterate through the 32 bits of the input number from right to
# left, and for each bit, we can add it to the result by shifting the result to the left by one position
# By shifting to the left the result, we are making space for the next bit to be added to the result at
# the rightmost position. Similarly, we can get the bit at the i-th position by shifting the input number
# to the right by i positions and then AND it with 1 to get the bit at the rightmost position

# Summary:
# Use the right shift in a loop to always get the rightmost bit
# AND the result with 1 to get a 0 or a 1 based on what's in the rightmost position
# Add the bit to the result by shifting the final result to the left by one position in order to give
# space for the next bit to be added at the rightmost position


class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        # The input number has 32 bits
        for i in range(32):
            # Get the bit at the i-th position. To do this, we shift the input number to the right by
            # i positions so at the last position we have the bit that we want to check with the AND
            bit = (n >> i) & 1
            # Add the bit to the result by shifting the result to the left by one position, thus leaving
            # space for the next bit to be added at the rightmost position. We shift by 31 - i positions
            # because we are iterating from right to left and we want to add the bits to the result from
            # left to right
            res += bit << (31 - i)
        return res


s = Solution()

print(s.reverseBits(43261596))  # 964176192
print(s.reverseBits(4294967293))  # 3221225471
print(s.reverseBits(0))  # 0
print(s.reverseBits(1))  # 2147483648
