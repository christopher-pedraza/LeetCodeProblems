# Neetcode.io solution

# Time complexity: O(n)
# Space complexity: O(1)

def trap(height):
	# If the list of heights is empty, return 0
	# as no water can be trapped
	if not height:
		return 0

	# Left and right pointers. The left starts at
	# the beginning of the array, the right at the
	# end
	l, r = 0, len(height) - 1

	# Store the current max from the left and right
	# Each time we move a pointer we will update 
	# these in case the new height is bigger.
	# We will always move the pointer of the position
	# with the lowest max height. In case they are the
	# same, we are moving the right one, but could also
	# be the left one.
	leftMax, rightMax = height[l], height[r]

	# Stores how much water has been trapped
	water = 0
	
	# Loop while the pointers don't cross each other
	while l < r:
		# As I said, move the one that is lower. This
		# removes the need to know the max value from the
		# other side as you know the bottleneck is the min
		# value, thus the height of the pointer you will be
		# shifting. By bottleneck I mean that the trapped
		# water is limited by the lowest height, as any more
		# water would escape. This means that using the
		# lowest value (the one you shift), you already know
		# that is the max height of the water that can be
		# trapped
		if leftMax < rightMax:
			# Move the left pointer 1 position to the right
			l += 1
			# Update the max before calculating the water
			# helps remove the negative values. If the new
			# height is bigger than the previous max height
			# and we calculate the water first, we would get
			# a negative result, meanwhile if we get the new
			# max, we would be substracting the number by 
			# itself and get 0. Obviously, if the new height
			# is smaller, the maxHeight won't update and the
			# result of water would be a positive value
			leftMax = max(leftMax, height[l])
			# Once you get the new (or same) height, you can
			# calculate if any water was trapped. This is done
			# by substracting the max by the current height.
			# If for example the left max height is 2 and the
			# current height is 0, that means that in the
			# current position 2 units of water can be stored.
			# If on the other hand, the current height is also
			# 2, it means that the current position can trap no
			# water
			water += leftMax - height[l]
		# Do the same as the left side but to the right side
		# in case the maximum right height is greater or equal
		# than the height of the left
		else:
			r -= 1
			rightMax = max(rightMax, height[r])
			water += rightMax - height[r]

	# After the left and right pointers cross each other
	# it means that you have calculated the total water
	# that can be trapped in all of the positions of the
	# array, so you may return the sum
	return water

print(trap([0,1,0,2,1,0,1,3,2,1,2,1])) # 6
print(trap([4,2,0,3,2,5])) # 9
print(trap([5,2,1,2,1,5])) # 14