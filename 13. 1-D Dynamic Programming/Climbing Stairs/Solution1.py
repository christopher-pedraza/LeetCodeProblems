# Neetcode.io solution

# Time complexity: O(n), where n is the step of which we want to get the number of unique
#                  solutions
# Space complexity: O(1), as we only keep track of the last 2 solutions
class Solution:
    def climbStairs(self, n: int) -> int:
         # Base cases
        # To reach to step 1, we only have 1 option (taking one step of size 1)
        # To reach to step 2, we have 2 options (take two steps of size 1, or one step of
        # size 2)
		# To reach to step 3, we have 3 options (take three steps of size 1, one of size
		# two followed by one of size 1, or viceversa)
        if n <= 3:
            return n
        
        # We will keep track of the 2 last solutions as each new solution is made with the
        # sum of the two previous ones
        n1, n2 = 2, 3

        # Iterate from the step 4 to the step n
        for i in range(4, n + 1):
            # The new solution is the sum of the previous 2 solutions
            temp = n1 + n2
            # Update the previous solutions
            n1 = n2
            n2 = temp

        # Last solution, which is the solution of the step n
        return n2

sol = Solution()
print(sol.climbStairs(2)) # 2
print(sol.climbStairs(3)) # 3
print(sol.climbStairs(5)) # 8