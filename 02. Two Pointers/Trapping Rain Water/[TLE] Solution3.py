# Neetcode.io idea (not the code shown)
# Time limit exceeded

# Time complexity: O(n)
# Space complexity: O(1)?

def trap(height):
	water = 0
	maxLeft, maxRight = 0, 0

	# Get the maximum right and left height for each index
	for i in range(len(height)):
		# If we are in the first and last position, we dont calculate
		# the left/right maximum as there's not other number at the
		# left/right
		if i > 0:
			# Get the maximum height from the left values
			maxLeft = max(height[0:i])
		if i < len(height)-1:
			# Get the maximum height from the right values
			maxRight = max(height[i+1:len(height)])

		# Get the minimum from the left and right heights
		minHeight = min(maxLeft, maxRight)
		# To calculate the amount of water that can be trapped in any given
		# position, we do the minHeight-currentHeightInIndex. We only want
		# positive values, so any negative ones are replaced by a 0
		water += (minHeight-height[i] if minHeight-height[i] >= 0 else 0)

	return water

print(trap([0,1,0,2,1,0,1,3,2,1,2,1])) # 6
print(trap([4,2,0,3,2,5])) # 9
print(trap([5,2,1,2,1,5])) # 14