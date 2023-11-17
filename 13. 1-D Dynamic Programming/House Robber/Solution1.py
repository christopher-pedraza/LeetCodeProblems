# Neetcode.io solution

# Time complexity: O(n) where n is the amount of houses
# Space complexity: O(1) because we only have to store the amount robbed of the two previous
#                   houses


class Solution:
    def rob(self, nums: list[int]) -> int:
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
            # ans2 is the amount robbed from the previous house, which for the next iteration
            # it will be the current house of this iteration
            ans2 = current
        # The max robbed will be the amount robbed until the previous house
        return ans2


sol = Solution()
print(sol.rob([1, 2, 3, 1]))  # 4
print(sol.rob([2, 7, 9, 3, 1]))  # 12
print(sol.rob([1, 2]))  # 2
