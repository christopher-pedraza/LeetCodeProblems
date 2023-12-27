# Neetcode.io solution

# Time complexity: O(n) as we have to check all the numbers at least once to test the
#                  products
# Space complexity: O(1) we will just iterate over the numbers and not save anything

# We will keep track of both the positive and negative products that we have found up to
# a certain point. For example, consider these examples:
# Values: [1, 2, 3]
# Iteration 1 | Min: 1 = 1 | Max: 1 * 2 = 2
# Iteration 2 | Min: 1 = 1 | Max: 1 * 2 * 3 = 6
#
# Values: [-1, -2, -3]
# Iteration 1 | Min: -2 = -2 | Max: -1 * -2 = 2
# Iteration 2 | Min: -1 * -2 * -3 = -6 | Max: -2 * -3 = 6
# Notice that in the iteration 2, we are using for the min value the previous max value
# multiplied by the new number, while for the max value, we are multiplying the preivous
# min value by the new number. That's the use of keeping track of both the minimum and
# maximum product. In the same sense, we can see that we are reusing the previous products,
# thus, this calls for a dynamic programming approach:
# Iteration 1 | Min: -2 = -2 | Max: -1 * -2 = 2
# Iteration 2 | Min: -1 * -2 * -3 = -6 | Max: -2 * -3 = 6
# Iteration 2 | Min: 2 * -3 = -6 | Max: -2 * -3 = 6
# Iteration 2 | Min: it1_max * -3 = -6 | Max: it1_min * -3 = 6
#
#
# If we now add another value to the array:
# Values: [-1, -2, -3, -4]
# Iteration 1 | Min: -2 = -2 | Max: -1 * -2 = 2
# Iteration 2 | Min: it1_max * -3 = -6 | Max: it1_min * -3 = 6
# Iteration 3 | Min: it1_max * -4 = -24 | Max: it1_min * -4 = 24
#
# But in the case the new number is positive, it would be different:
# Values: [-1, -2, -3, 4]
# Iteration 1 | Min: -2 = -2 | Max: -1 * -2 = 2
# Iteration 2 | Min: it1_max * -3 = -6 | Max: it1_min * -3 = 6
# Iteration 3 | Min: it1_min * 4 = -24 | Max: it1_max * 4 = 24
#
# Notice that if we add a positive number, we now multiply by the maximum, while when
# adding a negative number, we were multiplying by the minimum product.
# So basically, if the new number is positive, we multiple by the maximum, else, we
# multiply by the minimum.


class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        # We cannot set it as 0 as we could only have for example 1 negative value, the
        # result would be a negative one, so we just begin it with the first value
        res = nums[0]
        # Initialize both to the neutral value of 1 (as any number multiplied by it would
        # be itselft)
        curMin, curMax = 1, 1

        for n in nums:
            # The current max/min can be multiplying the new number by the current min or
            # max or just the number by itself (for example, if we had [1, -8], just
            # keeping the 1 would be higher than multiplying it)
            # We are saving the current max so we can then calculate the current min with
            # the unmodified max
            prev_max = n * curMax
            # If we ever find a 0, it would make the product 0, however, as we are checking
            # for the max/min considering also the current number, we wouldn't have a
            # problem and wouldn't need to reset the values of curMin and curMax
            curMax = max(prev_max, n * curMin, n)
            curMin = min(prev_max, n * curMin, n)

            # The result is the max from itselft, or the current max (the current min
            # cannot be the result as it would be negative or lower than the current max)
            res = max(res, curMax)
        return res


s = Solution()

print(s.maxProduct([2, 3, -2, 4]))  # 6
print(s.maxProduct([-2, 0, -1]))  # 0
print(s.maxProduct([-2]))  # -2
print(s.maxProduct([0, 2]))  # 2
