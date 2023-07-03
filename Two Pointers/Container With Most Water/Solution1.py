# Neetcode.io solution

# Time complexity: O(n) - getting min and max is on O(n)
#                         also iterating over the list
# Space complexity: O(1) - no extra space needed

def maxArea(height):
	# Left and right pointers
	l, r = 0, len(height) - 1
	# Store the max water capacity
	res = 0
	# Get the maximum height possible in the list
	maxH = max(height)

	while l < r:
		# To calculate the water, you get the difference between the
		# left and right pointer and multiply it by the minimum height
		# between the two heights in the positions l and r
		res = max(res, min(height[l], height[r]) * (r - l))

		# Move the pointer where the height is the least
		if height[l] < height[r]:
			l += 1
		# Here also checks if both are equal. In this case, you
		# can shift whatever of the two pointers
		elif height[r] <= height[l]:
			r -= 1
		
		# If the current water is already the maximum that is possible
		# it breaks the loop
		if (r-l) * maxH <= res:
			break 
	return res


print(maxArea([1,8,6,2,5,4,8,3,7])) # 49
print(maxArea([1,1])) # 1
print(maxArea([0,2])) # 0
print(maxArea([2,3,4,5,18,17,6])) # 17
print(maxArea([1,3,2,5,25,24,5])) # 24