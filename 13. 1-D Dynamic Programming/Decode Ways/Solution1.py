# Neetcode.io RECURSIVE (MEMOIZATION) DP SOLUTION

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

        # i is the current position we are checking
        def dfs(i):
            # Good Base Case
            # If i is in the dp, we have already calculated the answer for that position
            # or it's the last position, so we return the answer
            if i in dp:
                return dp[i]

            # Bad Base Case
            # If the current position is 0, we can't decode it as it's not a valid
            # number, so we return 0
            if s[i] == "0":
                return 0

            # If it's not 0, then it means the value is 1-9 and we can decode it as a
            # single digit number, so we call the function again with the next position
            res = dfs(i + 1)

            # Check for 2 digit combinations
            # Another way to check if it's a valid combination of 2 digits would be to
            # check if the current position is less than the length of the string and
            # if the char in the current position is either 1 or 2. 1 because with 1 we
            # can only have numbers up to 19 (considering the second digit is 9) and with
            # 2, we could have up to 29, so we also have to check if the second digit is
            # less than 7, otherwise it's not a valid combination. Or we can slice it and
            # check if it's less than 26. What i'm describing would be:
            """
            if (i + 1 < len(s) and (s[i] == "1" or (s[i] == "2" and s[i+1] < "7"))):
            """
            # Or it could also be:
            """
            if (i + 1 < len(s) and
                (s[i] == "1" or (s[i] == "2" and s[i+1] in "0123456"))):
            """
            if i + 1 < len(s) and s[i : i + 2] <= "26":
                # Subproblem from the next position
                res += dfs(i + 2)

            # Cache the answer of the current position
            dp[i] = res
            # And return it
            return res

        # Start the recursion from the first position and return what is returned as it
        # will be the combination of all the counts of the subproblems. The answer will
        # be in the last position, while on the Solution3.py, as it's iterating backwards,
        # the answer will be in the first position
        return dfs(0)


s = Solution()

print(s.numDecodings("12"))  # 2
print(s.numDecodings("226"))  # 3
print(s.numDecodings("0"))  # 0
print(s.numDecodings("06"))  # 0
