# Neetcode.io ITERATIVE (TABULATION) DP SOLUTION

# Time complexity: O(n)
# Space complexity: O(n) as we are going to store all the previous answers. As
#                   an optimization, we could just store the last 2 answers which
#                   would give us a space complexity of O(1) and is the solution
#                   in Solution1.py

# To solve the problem, we will keep track of how combinations can be made up to
# a certain point, and use dynamic programming to calculate the final count.
# For the combinations, it's something like this:
# 121
#        / \
#       1   12
#      / \   \
#     2   21  1
#    /
#   1
# So with this, we only have 3 possible combinations
# Now, the problem with this is that as we can have 2 decisions for node, it would
# have a time complexity of O(2^n). To optimize it, we can do DP so we can divide
# the problem in subproblems. We will check how many times we can decode a certain
# portion without considering another one and so on and with that, we will
# eventually know the total count. With this, we can have a time complexity of O(n)
# as well as a memory complexity of O(n) (considering we use a list where we store
# all the previous answers). We could further optimize the memory by not storing
# all the answers but just the last 2 so we have a memory complexity of O(1). This
# is because to know the current answer dp[i], we just need to take the sum of the
# previous (in the index the next ones) answers dp[i] = dp[i+1] + dp[i+2], thus we
# only need 2 positions and not a full array.


class Solution:
    def numDecodings(self, s: str) -> int:
        # We will store 1 in case we get empty string, we return 1 as the base case
        dp = {len(s): 1}

        # Loop backwards through the string
        for i in range(len(s) - 1, -1, -1):
            # If the current character is "0", set the current index in the
            # dictionary to 0
            if s[i] == "0":
                dp[i] = 0
            else:
                # Otherwise, set the current index in the dictionary to the value
                # of the next index (as we are looping backwards, the next index
                # would be the previous answer)
                dp[i] = dp[i + 1]

            # Check for 2 digit combinations
            # The Solution2.py file has alternative ways of making this check
            if i + 1 < len(s) and (
                s[i] == "1" or s[i] == "2" and s[i + 1] in "0123456"
            ):
                # Add the value of the index two steps ahead to the current index in
                # the dictionary
                dp[i] += dp[i + 2]

        # Return the value of the first index in the dictionary (as we are looping
        # backwards and we are storing the answers in the dictionary, the first index
        # would be the final answer)
        return dp[0]


s = Solution()

print(s.numDecodings("12"))  # 2
print(s.numDecodings("226"))  # 3
print(s.numDecodings("0"))  # 0
print(s.numDecodings("06"))  # 0
