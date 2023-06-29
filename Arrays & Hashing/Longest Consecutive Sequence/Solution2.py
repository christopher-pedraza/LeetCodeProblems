# Time complexity: O(nlogn) - sorting
# Space complexity: O(1)

def longestConsecutive(nums):
	# Stores the current length of the sequence
    currentSeq = 1
    # Stores the max length that has been found
    maxSeq = 0

    # If the list is empty, return 0 without doign anything else
    if not nums:
        return 0

    # In-place sorting so space complexity is O(1)
    # This gives the time complexity of O(nlogn)
    nums.sort()

    # Iterate over the numbers - 1 as on each iteration I'm looking
    # at the next number 
    for i in range(len(nums)-1):
        # If the current number is equal to the next number - 1, it
        # means it's consecutive and you add 1 to the current length
        if nums[i] == nums[i+1]-1:
            currentSeq += 1
        # if the current numbers is the same as the next one
        # (repetition), just continue iterating
        elif nums[i] == nums[i+1]:
            continue
        # If it isn't consecutive, you get the max from the previous max
        # and the current length and reset the value of current length
        else:
            maxSeq = max(maxSeq, currentSeq)
            currentSeq = 1

    # In case all numbers are consecutive and you never arrive at the
    # else, get once again the max and return it
    return max(maxSeq, currentSeq)

print(longestConsecutive([100,4,200,1,3,2]))
print(longestConsecutive([0,3,7,2,5,8,4,6,0,1]))