# Time limit exceeded

# Time complexity: O(m) where m is the value of the max 
#				   number in height
# Space complexity: O(1)

def trap(height):
	# Left and right pointers
    l, r = 0, len(height)-1
    # Stores the trapped water
    water = 0
    # In order to 
    nums = set(height)
    # current height. Starts in 1 as 0 in the edges won't store
    # any water
    currentH = 1
    maxHeight = max(nums)

    # While the pointers don't cross or are the same
    while l < r and l != r and nums:
        # Move the pointers if the height is less than the current
        while height[l] < currentH and l < r:
            l += 1
        while height[r] < currentH and l < r:
            r -= 1

        # Sum 1 for each level that is empty and is less than
        # the current height
        water += sum(1 for i in height[l+1:r] if i < currentH)

        # If the curren height is in nums, you remove it
        if currentH in nums:
            nums.remove(currentH)

        # Increase the current height to check for empty spaces
        # in the next level
        currentH += 1

    return water

print(trap([0,1,0,2,1,0,1,3,2,1,2,1])) # 6
print(trap([4,2,0,3,2,5])) # 9
print(trap([5,2,1,2,1,5])) # 14