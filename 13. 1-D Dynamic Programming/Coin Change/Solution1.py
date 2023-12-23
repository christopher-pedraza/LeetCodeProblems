# Neetcode.io solution

# Time complexity: O(amount*coins) as for every amount starting from 0...target_amount
#                  we have to check the combination with every coin
# Space complexity: O(amount) as we need to store all the combinations of the previous
#                   coin changes until we arrive at the coin change that the problem
#                   requires

# My first idea was to implement a Greedy algorithm in which I always take the greates
# valued coin, however, this not always produces the correct result. For example:
# Amount: 7
# Coins: [1, 3, 4, 5]
# In this case, following the greedy approach, we would grab the following coins:
# 3 coins used | 5 + 1 + 1 = 7
# However, we could actually use lower valued coins to use less coins, for example:
# 2 coins used | 4 + 3 = 7
# So in this case, the greedy approach is not possible.

# The brute force solution would be to compute all the possible paths for every used coin,
# for example (the values shown are the result after substracting from the amount the
# coin values in the order of the array):
# Amount: 7
# Coins: [1, 3, 4, 5]
#
#   _________|_________
#  /      /     \      \
# 6      4       3      2
#      __|__     |    __|__
#     / / \ \    |   / / \ \
#    3 1   0 -1  |  1 -1 -2 -3
#    |_|____As we have already computed the subtree of 3, the next time we won't need to
#      |    calculate it
#      |
#      |__The same with the 1
#
# As seen in this tree, some subproblems in which the bigger problem was divided (summing
# to 6, 4, 3, 2, 1, etc) are repeated, this calls for a Dynamic Programming approach.
# In this example it would be a top-bottom DP using memoization and recursive calls,
# however, it could also be solved using tabulation for a bottom-up solution.
#
# In these first examples, I'm only showing the solution using the correct coin, but all
# the possible coins should be tested and the combination with the lowest amount of coins
# should be kept.
#
# Amount of coins that are needed to sum up to 0:
# DP[0] = 0
#
# Amount of coins that are needed to sum up to 1:
# DP[1] = 1 + DP[0]
# DP[1] = 1 + 0
# DP[1] = 1
#
# Amount of coins that are needed to sum up to 2:
# DP[2] = 1 + DP[1]
# DP[2] = 1 + 1
# DP[2] = 2
#
# Amount of coins that are needed to sum up to 3, 4, 5, 6:
# DP[3] = 1
# DP[4] = 1
# DP[5] = 1
# DP[6] = 2
#
#
# Amount of coins that are needed to sum up to 7:
# In this last case, we will check with the four coins: [1, 3, 4, 5]
#
# With coin 1
# DP[7] = 1 + DP[7-1]
# DP[7] = 1 + DP[6]
# DP[7] = 1 + 2
# DP[7] = 3
#
# With coin 3
# DP[7] = 1 + DP[7-3]
# DP[7] = 1 + DP[4]
# DP[7] = 1 + 1
# DP[7] = 2
#
# With coin 4
# DP[7] = 1 + DP[7-4]
# DP[7] = 1 + DP[3]
# DP[7] = 1 + 1
# DP[7] = 2
#
# With coin 5
# DP[7] = 1 + DP[7-5]
# DP[7] = 1 + DP[2]
# DP[7] = 1 + 2
# DP[7] = 3
#
# The lowest amount of coins needed to give the coin change of 7 is: 2


class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        # From 0 to amount. We will store in every position a max value. In this case, as
        # a max value we will put the amount+1
        dp = [amount + 1] * (amount + 1)

        # Base case as for the amount of 0, it will only take 0 coins
        dp[0] = 0

        # For each amount: Bottom up
        for a in range(1, amount + 1):
            # We will go through every coin
            for c in coins:
                # If the coin still makes the amount valid, meaning we either have
                # a resulting amount of 0 or greater
                if a - c >= 0:
                    # We store in the current amount the min from itself or the sum of 1
                    # plus the count of coins for the amount substracted by the current
                    # coin. This last one sums 1 as it considers the current coin c that
                    # we are iterating. Basically there are 2 options, the first dp[a] is
                    # where we don't consider the current coin c, and the 1 + dp[a-c] is
                    # where we consider it, thus, adding 1 to the count of coins (because
                    # of c) to the count of coins of the remaining amount after
                    # substracting the value of the current coin. Basically it's like:
                    # coin c = 4
                    # amount a = 7
                    # dp[7] = min(dp[7], 1 + dp[7-4])
                    # dp[7] = min(dp[7], 1 + dp[3])
                    dp[a] = min(dp[a], 1 + dp[a - c])
        # As the answer, we return the coin count of the amount dp[amount], however, we
        # have to still consider an edge case: that the value store in it is not equal
        # to the default value we setup at the beginning, the maximum value of amount+1
        # If that's the case, it means we never found a combination of valid coins (even
        # if all the coins were 1s, the count would have been equals to amount, and when
        # taking the minimum value from "dp[a] = min(dp[a], 1 + dp[a - c])", we would
        # have replace the count), so we return -1
        return dp[amount] if dp[amount] != amount + 1 else -1


s = Solution()

print(s.coinChange([1, 2, 5], 11))  # 3
print(s.coinChange([2], 3))  # -1
print(s.coinChange([1], 0))  # 0
print(s.coinChange([1], 1))  # 1
