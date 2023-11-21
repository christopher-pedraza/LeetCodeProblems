# Neetcode.io solution

# Time complexity: O(n) where n is the amount of houses (it will actually be O(2n) as we
#                  run House Robber I twice)
# Space complexity: O(1) because we only have to store the amount robbed of the two previous
#                   houses

"""
You will be able to do this only if you have solved HOUSE ROBBER I :

apply house robber I on nums(1,n-1) //left to right
apply house robber I on nums(n,2) //right to left
return max(answer obtained in step 1, answer obtained in step 2)

The basic idea is that if we rob the first house, we can't rob the last house, so we run
House Robber I twice, one not including the last house and the other not including the first
house. Then we return the max from those two calculations. With this we are converting the
problem into two House Robber I problems because we are not allowing to rob the first and
last house at the same time, thus breaking the circle and making the houses linear.
Example:
[2, 3, 2, 1]
Skipping the last house
[2, 3, 2] -> [2, 3] -> 3
Skipping the first house
[3, 2, 1] -> [2, 1] -> 2
max(3, 2) = 3

We would only be missing checking for an edge case in which we only have one house, in
which case we would return that house as the answer as it is the only house available to
rob. 
Example:
[1]
Skipping the last house
[1] -> [] -> 0
Skipping the first house
[1] -> [] -> 0
max(0, 0) = 0
So we add to the max the first house, which is the only house available to rob:
max(0, 0, 1) = 1
"""


class Solution:
    def rob(self, nums: list[int]) -> int:
        def rob_aux(nums: list[int]) -> int:
            # The previous two answers so we can check if its better to include the
            # current house or not. They start outside of the array of nums (with 0s)
            ans1, ans2 = 0, 0

            # Iterate over the houses checking which house should we rob
            for n in nums:
                # ans1 + n would be robbing the house before the previous (and any other
                # valid house that was robbed before it) and the current one.
                # ans2 would be not robbing the current house and just keeping whatever
                # was robbed until the previous house. As we are robbing the previous house,
                # we wouldn't be able to rob the current house, that is why we don't add n
                # to the value.
                # We get what is the maximum to know which decision is better
                current = max(ans1 + n, ans2)
                # ans1 is the amount robbed from the house before the previous (and any other
                # houses before it), so it will take the value of the previous house now
                ans1 = ans2
                # ans2 is the amount robbed from the previous house, which for the next
                # iteration it will be the current house of this iteration
                ans2 = current
            # The max robbed will be the amount robbed until the previous house
            return ans2

        # Run House Robber I twice, one not including the last house and the other not
        # including the first house
        # Skipping the last house
        not_last = rob_aux(nums[:-1])
        # Skipping the first house
        not_first = rob_aux(nums[1:])
        # We calculate the max from the previous calculations in which we skipped the first
        # and last houses. However, this leads to an edge case in which we only have one
        # house. In this case, the previous calculations will both be 0, as we are sending
        # and empty array to House Robber I because we are skipping the only house available.
        # So to the calculation of max we add the first house, which is the only house to solve
        # this edge case.
        return max(not_last, not_first, nums[0])


sol = Solution()
print(sol.rob([2, 3, 2]))  # 3
print(sol.rob([1, 2, 3, 1]))  # 4
print(sol.rob([1, 2, 3]))  # 3
print(sol.rob([1]))  # 1
print(sol.rob([0]))  # 0
