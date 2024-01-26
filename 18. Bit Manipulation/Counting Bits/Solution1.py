# Neetcode.io solution

# Time complexity: O(n) using DP to prevent the need of reprocessign previous values when going from 0->n, being 0 the base case
# Space complexity: O(1) if we don't consider the answer array as extra memory, else O(n+1) as we will need an array to store from 0->n

"""
O(nlog₂n) approach
Basically, for every number from 0->n (thus the n in the time complexity, as we will iterate over all the numbers) we will check the number of 1s in
their binary representation. To check this, we will use the MOD operator to know if there's a 1 in the right most position, and then perfom an integer
division by 2 to chop the last value from the representation. As we are dividing, the time complexity is logn, and as it's by 2 log₂n. Example:
n = 3
DECIMAL: 3 -> BINARY: 11
res_n = 0
11 % 2 = 1 ; res_n++
11 // 2 = 1

res_n = 1
1 % 2 = 1 ; res_n++
1 // 2 = 0 ---END

res_n = 2
Therefore, 3 has two 1's, now let's check for n-1 until 0

n = 2
DECIMAL: 2 -> BINARY: 10
res_n = 0
10 % 2 = 0
10 // 2 = 1

res_n = 0
1 % 2 = 1
1 // 2 = 0 ---END

res_n = 1
Therefore, 2 has one 1's, now let's check for n-1 until 0

n = 0
DECIMAL: 0 -> BINARY: 0
res_n = 0
0 % 2 = 0
0 // 2 = 0 ---END

res_n = 0
Therefore, 0 has zero 1's, and we end it as we already arrived at 0

O(n) approach
In order to solve this problem linearly, we will be using Dynamic Programming. The number of 1s in a certain position will be equals to 1 plus a
value computed in a previous n. To know which previous n, we will be keeping track of an offset that will be taking values of 1, 2, 4, 8, 16...
So the formula to get the number of 1s for any given n will be "1 + dp[current_n - offset]"

n = 0
0 - 0000 - 0 (BASE CASE)

n = 1
offset: 1
1 | 0001 | 1 + dp[n - 1]
1 | 0001 | 1 + dp[1 - 1]
1 | 0001 | 1 + dp[0]
1 | 0001 | 1 + 0
1 | 0001 | 1

n = 2
offset: 1
off = off * 2 if off * 2 == n
off = 1 * 2 if 1 * 2 == 2
off = 2 if 2 == 2
offset: 2
2 | 0010 | 1 + dp[n - 2]
2 | 0010 | 1 + dp[0]
2 | 0010 | 1 + 0
2 | 0010 | 1

n = 3
offset: 2
off = off * 2 if off * 2 == n
off = 2 * 2 if 2 * 2 == 3
off = 4 if 4 == 3
offset: 2
3 | 0011 | 1 + dp[n - 2]
3 | 0011 | 1 + dp[1]
3 | 0011 | 1 + 1
3 | 0011 | 2

n = 4
offset: 2
off = off * 2 if off * 2 == n
off = 2 * 2 if 2 * 2 == 4
off = 4 if 4 == 4
offset: 4
4 | 0100 | 1 + dp[n - 4]
4 | 0100 | 1 + dp[0]
4 | 0100 | 1 + 0
4 | 0100 | 1

...

n = 8
offset: 4
off = off * 2 if off * 2 == n
off = 4 * 2 if 4 * 2 == 8
off = 8 if 8 == 8
offset: 8
8 | 1000 | 1 + dp[n - 8]
8 | 1000 | 1 + dp[0]
8 | 1000 | 1 + 0
8 | 1000 | 1
"""


class Solution:
    def countBits(self, n: int) -> list[int]:
        # Initialize it with the base case of 0.
        # Length of n+1 as we are considering from 0->n
        dp = [0] * (n + 1)
        # As we are going to ignore the first position, we start from an offset of 1
        offset = 1

        for i in range(1, n + 1):
            # Check if it's possible to double the offset (what we were doing with: "off = off * 2 if off * 2 == n")
            if offset * 2 == i:
                offset = i
            dp[i] = 1 + dp[i - offset]
        # dp already has the amount of 1s for every value from 0->n
        return dp


s = Solution()

print(s.countBits(2))  # [0, 1, 1]
print(s.countBits(5))  # [0, 1, 1, 2, 1, 2]
print(s.countBits(8))  # [0, 1, 1, 2, 1, 2, 2, 3, 1]
print(s.countBits(0))  # [0]
