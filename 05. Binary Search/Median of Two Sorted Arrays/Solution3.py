# Time complexity: O(nlogn) - sorting
# Space complexity: O(1) - use the same lists

def findMedianSortedArrays(nums1: list[int], nums2: list[int]) -> float:
	# Append the values of nums2 into nums1
	nums1 += nums2
	# Sort all the numbers
	# Time complexity of sorting: O(nlogn)
	nums1.sort()
	# Get the size of the list to know if it's empty, even or odd
	size = len(nums1)

	# Empty
	if size == 0:
		# Return 0
		return 0.0
	# Even
	elif size % 2 == 0:
		# Return the mean between the 2 numbers in the middle
		return float((nums1[size//2-1] + nums1[size//2]) / 2)
	# Odd
	else:
		# Return the number in the middle
		return float(nums1[size//2])


print(findMedianSortedArrays([1,3], [2])) # 2.00000
print(findMedianSortedArrays([1, 2], [3, 4])) # 2.50000
print(findMedianSortedArrays([], [1, 2, 3])) # 2.00000
print(findMedianSortedArrays([1, 2, 3], [])) # 2.00000
print(findMedianSortedArrays([10], [1, 2, 3, 4, 5, 6, 7, 8, 9])) # 5.50000
print(findMedianSortedArrays([1, 2, 3, 4, 5, 6, 7, 8, 9], [10])) # 5.50000
print(findMedianSortedArrays([], [])) # 0.00000