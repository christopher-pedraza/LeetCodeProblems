# Neetcode.io solution

# Time complexity: O(n^2) as for every value in the input array we will check all the
#                  other values
# Space complexity: O(n) as we are keeping track of the longest subsequent chain for
#                   every index

# The bruteforce solution would be for every element of the input array, check whether
# to include or not the value, thus, for every element, you have two options:
# include it, or not. This leads to a time complexity of O(2^n)
#
# A more efficient solution would be to do a DFS with cache, this would end up with a
# time complexity of O(n^2). Basically, we start from every position of the input
# array, and keep adding from the rest of the input array to the path if the new value
# is bigger than the last value we added, and at the end, we check what's the longest
# path and that would be the longest increasing subsequence
# Example:
# Input: [1, 2, 4, 3]
#
# |
# |- [1]
#     \- [1, 2]
#           \- [1, 2, 4]
#                  \- [1, 2, 4, 3] X <-- This solution is not valid as we are adding
#                                        a number with a lower value
#           \- [1, 2, 3] <-- This is the longest increasing subsequece (as well
#                            as the subsequence [1, 2, 4])
#     \- [1, 4]
#           \- [1, 4, 3] X
#     \- [1, 3]
# \- [2] <-- Eventhough we may find a subsequence, its length may at most be of the
#            size of the longest we have already found as we have only 3 numbers
#            remaining and the longest we have found is of length 3
# \- [4] <-- Any of this solutions would be smaller as we already found a subsequence
#            of length 3 and we only have 2 remaining numbers
# \- [3]
#
# With this we may also include DP so we don't have to process the same indexes again
# for example, we know that from index 3 (the last index) we may just add 1 more
# number (itself) as there's no other number after it, thus we know that DP[3] = 1
# Similarly, after running the path from the first index: "0->1->" and the numbers
# being "1, 2, ", we know that from index 2 we can just add 1 more number, either 4 or
# 3, therefore, DP[2] = 1. This helps us the next time we are at either index 3 or 2.
# For example, the path that starts with the number 4 (index 2), we know that we can
# just add it without any other number, making the subsequence of just 1. Following
# the path of "0->1" we also know that we could only have added 2 values, so DP[1] = 2
# and DP[0] = 3. The biggest DP would be the answer as it would be the longest
# subsequence. Bare in mind that, even if in this example the longest one is in index
# 0, that will not always be the case. In this case we followed a down-top DP approach
# starting from the end of the input array, and working our way to the beginning.
#
# The DP approach would be like this:
# We start at our base case that is the last value in the input array:
# DP[3] = 1
# Then for DP[2] it can either be just taking itself "1" or itself+next DP:
# DP[2] = max(1, 1+DP[3])
# However, in order to do "1+DP[3]" a certain condition needs to be fulfilled:
# nums[2] < nums[3], meaning that in order to take the next number as part of the
# subsequence, the next number needs to be bigger than the current one, if not, we
# cannot consider it as part of the subsequence.
# In this case, the condition doesn't apply, so DP[2] can only be 1
# For DP[1] as nums[1] < nums[2] and at the same time nums[1] < nums[3], the value
# can be: max(1, 1+DP[2], 1+DP[3]) -> max(1, 1+1, 1+1) -> max(1, 2, 2)
# DP[1] = 2
# And finally:
# DP[0] = max(1, 1+DP[1], 1+DP[2], 1+DP[3]) -> max(1, 1+2, 1+1, , 1+1)
#                                                                -> max(1, 3, 2, 2)
# DP[0] = 3
#
# This approach is O(n^2) as we only iterate one time the input array, and for every
# position of it, we go through all the other values.


class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        # The base case is 1, as even if all the numbers aren't in increasing order
        # at least the subsequence can be of length 1
        LIS = [1] * len(nums)

        # Iterate from the back all the numbers
        for i in range(len(nums) - 1, -1, -1):
            # For every element, iterate over the numbers that are after it,
            # which are the ones we have already processed
            for j in range(i + 1, len(nums)):
                # If the condition that the next number is bigger than the current
                # one applies
                if nums[i] < nums[j]:
                    # Update the longest subsequent value with the max of itself or
                    # the combination of itself plus the next LIS
                    LIS[i] = max(LIS[i], 1 + LIS[j])
        # Return the maximum LIS we have found
        return max(LIS)


s = Solution()

print(s.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]))  # 4
print(s.lengthOfLIS([0, 1, 0, 3, 2, 3]))  # 4
print(s.lengthOfLIS([7, 7, 7, 7, 7, 7, 7]))  # 1
print(s.lengthOfLIS([4, 10, 4, 3, 8, 9]))  # 3
