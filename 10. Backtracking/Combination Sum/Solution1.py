# Neetcode.io solution

# See video for a more detailed explanation:
# https://youtu.be/GBKI9VSKdGg
# The basic idea is to create a decision tree, in which we
# put the combinations with the numbers. If any branch breaks
# the restriction (being less than the target), we can stop
# developing that branch. Now, the problem with this, is that
# we can end up with duplicate solutions. To solve this, we
# are going to limit the numbers we can use when dividing
# the branches. For example, we have these numbers: [2, 3, 4]
# At first, we are going to make two paths, one in which we
# include 2s in all solutions, and one in which we include no
# 2s:
#     O
#   /   \
# [2]    []
# The left branch will continue including more of the number
# from the parent node, while the right branch will only
# include what was already in the parent + any other number
# different from the last number we added to the parent:
#           O
#         /   \
#      [2]    []
#      / \
# [2,2]   [2, 3]
# With this solution, we will still make all the available
# solutions, but without the problem of duplicate solutions

# The time complexiy will be O(2^t) where t is the target
# This is because we make 2 decisiones for each node and
# the biggest depth the tree can have is that of the target.
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # Defined global for the solution
        res = []
            # To go through all the nodes/options of the numbers
            # To keep track of the candidate numbers that are
            # still availabe, we are using the pointer i
            # cur is to keep track of the values that we have
            # added to the current combination
            # total is the totalsum from the cur combination
            # so we know if we have already reached the target
            # sum
        def dfs(i, cur, total):
            # If the totalSum is already equals to the
            # target, we know we found a solution
            if total == target:
                # As we are going to keep using cur in
                # the other recursions, we are going to
                # make a copy of what's in it at the
                # moment
                res.append(cur.copy())
                # Stop going through this branch
                return
            # If there are no more candidates or the total
            # sum is already bigger than the target, we
            # can stop going through this branch as we will
            # not find any combination from it
            if i >= len(candidates) or total > target:
                return

            ## Decision in which we include the current
            ## candidate
            # We will include the candidate in i
            cur.append(candidates[i])
            # Thus, i stays the same, cur already has the
            # new candidate, and total will now have the 
            # value of the candidate.
            dfs(i, cur, total + candidates[i])

            ## Decision in which we don't include the
            ## current candidate
            # As we don't want to include it, we remoev it
            # from cur
            cur.pop()
            # i moves as we will not include the value in i
            # cur doesn't include the candidate and total
            # stays the same
            dfs(i + 1, cur, total)

        # Start the dfs with 0 as beginning index, empty
        # array as the current combination, and 0 as total
        dfs(0, [], 0)

        # Res should contain all the combinations when the
        # dfs ends
        return res