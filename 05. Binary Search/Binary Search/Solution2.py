# Time complexity: O(logn)
# Space complexity: O(1)

def search(nums: list[int], target: int) -> int:
	# Left and right pointers
	l, r = 0, len(nums)-1

	# If the value is outside of the lowest and
	# highest numbers, return -1 without
	# iterating over all the list
	if nums[l] > target or nums[r] < target:
		return -1

	# While the left and right pointers don't cross
	# Notice they can be the same, for example, if
	# we have a list of just one element
	while r >= l:
		# Get the middle pointer by dividing the sum
		# of the left and right pointers
		mid = (l+r)//2
		# If the target is on the middle we return
		# the index
		if nums[mid] == target:
			return mid
		# If the target is less than the value in the
		# middle, we move the left pointer one position
		# to the left of the middle pointer
		elif target < nums[mid]:
			r = mid-1
		# If the target is more than the value in the
		# middle, we move the right pointer one position
		# to the right of the middle pointer
		elif target > nums[mid]:
			l = mid+1
		# If no condition is met, we return -1
		else:
			return -1
	# If no condition is met, we return -1
	return -1


print(search([-1,0,3,5,9,12], 9)) # 4
print(search([-1,0,3,5,9,12], 2)) # -1
print(search([5], 5)) # 0
print(search([2, 5], 2)) # 0
print(search([-1,0,3,5,9,12], 13)) # -1