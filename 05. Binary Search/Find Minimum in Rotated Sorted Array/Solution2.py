# Time complexity: O(logn) - binary search
# Space complexity: O(1)

# Considering the required time complexity by
# the problem, we need to implement a binary
# search in order to find the minimum value
# in the list.
# As the numbers in the list are already sorted
# in ascending order, just rotated n times, we
# can just check the right pointer when we are
# doing the binary search, as if the value in
# right is bigger than the one in the middle, it
# means the right side is in the correct order
# (as it is ascending). In the previous case, we
# know that the minimum number needs to be on the
# left side as all the numbers to the right are
# bigger. However, we cannot ignore the value in
# the middle, as it could already be the minimum.
# Based on this, if the number in the middle is
# smaller than the one in the right, we are going
# to move the right pointer up to the middle
# pointer (still considering it in case it's
# already the minimum) and continue searching. If
# on the other hand, the value in the middle is
# bigger than the value to the right, it means
# that somewhere inside the right side should be
# the minimum value as the array is rotated.
# Additionally, we know that the value in the
# middle cannot be the minimum value in the list
# as the value in the right is already smaller,
# so we move the left pointer up to the middle + 1
# so we dont include it again. We are going to
# keep doing binary search until the left and right
# pointers cross each other, meaning we didn't find
# the minimum, or when we find the minimum and
# return it. As the minimum length of the array is
# 1, there should always be a minimum, so we could
# also iterate `while True`

def findMin(nums: list[int]) -> int:
	# Left and right pointers
	l, r = 0, len(nums)-1

	# Do binary search until the pointers cross
	# each other (we can be sure there will
	# be a solution, so the loop will never
	# exit without returning first the minimum)
	while l <= r:
		# Get the middle pointer
		mid = (l+r)//2

		# If the value in the middle pointer is
		# greater than the value in the right
		# pointer, then we need to search for the
		# minimum in the right side, thus, we
		# move the left pointer one position to
		# the right of the middle pointer
		if nums[mid] > nums[r]:
			l = mid + 1
		# If the value in the middle is instead
		# smaller than the right one, we move the
		# right pointer up to the middle (without
		# substracting 1 as the number in the
		# middle could already be the minimum)
		elif nums[mid] < nums[r]:
			r = mid
		# If it isn't smaller or greater, it means
		# we already found the minimum value and
		# return it
		else:
			return nums[mid]

print(findMin([3,4,5,1,2])) # 1
print(findMin([4,5,6,7,0,1,2])) # 0
print(findMin([11,13,15,17])) # 11
print(findMin([-500])) # -500
print(findMin([-500, 500])) # -500