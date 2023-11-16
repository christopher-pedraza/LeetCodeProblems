# Time complexity: O(n), where n is the step of which we want to get the number of unique
#                  solutions
# Space complexity: O(n), because for every step, we are storing its solution to be used
#                   to create the next solutions using backtracking

# One optimization present in neetcode's solution is that we don't have to store all the
# previous solutions in a list. As each new solution is just the sum of the 2 previous
# solutions, we just have to keep track of those two, reducing the memory complexity to
# O(1)

class Solution:
    def climbStairs(self, n: int) -> int:
        # Base cases
        # To reach to step 1, we only have 1 option (taking one step of size 1)
        # To reach to step 2, we have 2 options (take two steps of size 1, or one step of
        # size 2)
		# To reach to step 3, we have 3 options (take three steps of size 1, one of size
		# two followed by one of size 1, or viceversa)
        if n in [1, 2, 3]:
            return n
        
        # Add the base case solutions to the list to use backtracking
        solutions = [0 for _ in range(n)]
        solutions[1] = 2
        solutions[2] = 3

        # Iterate from the index 2 (as the first and second steps are already covered)
        for i in range(3, n):
            # The solution in the step i will be the sum of the solution in the previous and
            # before the previous solution
            solutions[i] = solutions[i-1] + solutions[i-2]

        # Return the last solution
        return solutions[-1]
    
sol = Solution()
print(sol.climbStairs(2)) # 2
print(sol.climbStairs(3)) # 3
print(sol.climbStairs(5)) # 8