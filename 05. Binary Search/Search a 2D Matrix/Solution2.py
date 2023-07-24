# Time complexity: O(logm) + O(logn) = O(log(m*n))
#                  This because we first did a binary search for
#                  the row that could contain the target, and then
#                  a binary search for the target in the row
# Space complexity: O(1)

def searchMatrix(matrix: list[list[int]], target: int) -> bool:
    # Binary search using the first and last value in each row.
    # When you define a middle, check if target is not inside the
    # row (check if target is smaller or equals than last value
    # in the row and greater or equals than first value).
    # If it isn't in the row, keep with the binary search through
    # the rows and each time check if it isn't in the middle row
    # When you find that the target could be in the row (between
    # the first and last value), you now do a binary search in the
    # row

    # Upper and lower pointers (point to the rows)
	up, low = 0, len(matrix)-1

	# While the pointer don't cross each other
	while low >= up:
		# Get the horizontal mid index
		# Could also be done with `(low+up)//2`, however this is better
		# for other languages. See Binary Search for a better explanation 
		h_mid = up + ((low - up) // 2)

		# If the target is inside the middle row
		# Start doing binary search in the row
		if target >= matrix[h_mid][0] and target <= matrix[h_mid][-1]:
			# Left and right pointers of the row
			l, r = 0, len(matrix[h_mid])-1
			# While the pointers don't cross each other
			while r >= l:
				# Get the vertical middle index
				v_mid = l + ((r - l) // 2)
				# If the target is smaller than the one in the middle
				# Move the right pointer 1 position to the left of the
				# middle
				if target < matrix[h_mid][v_mid]:
					r = v_mid - 1
				# If the target is greater than the one in the middle
				# move the left pointer 1 position to the right of the
				# middle
				elif target > matrix[h_mid][v_mid]:
					l = v_mid + 1
				# If the target is equals to the middle value
				else:
					return True
			# If the value was never found
			return False
		# If the target is smaller than the first value in the middle
		# row, we move the lower index as the value could be in the
		# upper rows
		elif target < matrix[h_mid][0]:
			# Move lower index one position below the middle
			low = h_mid - 1
		# If the target is greater than the last value in the middle
		# row, we move the upper index as the value could be in the
		# lower rows
		elif target > matrix[h_mid][-1]:
			# Move upper index one position upwards from the middle
			up = h_mid + 1
	# If the value was never found
	return False

print(searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3)) # True
print(searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 13)) # False