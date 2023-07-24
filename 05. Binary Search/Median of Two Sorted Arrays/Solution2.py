# Time complexity: O(m+n)
# Space complexity: O(n)

def findMedianSortedArrays(nums1: list[int], nums2: list[int]) -> float:
	# If both lists are empty, return 0 without doing anything else
	if not nums1 and not nums2:
		return 0.0

	# Left pointers for nums1 and nums2
	l1, l2 = 0, 0
	# Total size combining nums1 and nums2
	total_size = len(nums1) + len(nums2)
	# Check if the total quantity of the numbers is even or odd
	isEven = True if total_size%2 == 0 else False
	# List with half of the numbers
	half_nums = []

	# While the length of halfnums is still not the same as half the
	# size of all the numbers combined from nums1 and nums2 + 1
	while len(half_nums) < (total_size//2)+1:
		# If both lists still contain numbers
		if l1 < len(nums1) and l2 < len(nums2):
			# If the value in nums1 is smaller than the one in
			# nums2
			if nums1[l1] < nums2[l2]:
				# Add to the list the value of nums1 and move
				# once the pointer for nums1
				half_nums.append(nums1[l1])
				l1 += 1
			# If the value in nums2 is smaller than the one in
			# nums1
			else:
				# Add to the list the value of nums2 and move
				# once the pointer for nums2
				half_nums.append(nums2[l2])
				l2 += 1
		# If only nums1 still contains numbers
		elif l1 < len(nums1):
			# Add to the list the value of nums1 and move
			# once the pointer for nums1
			half_nums.append(nums1[l1])
			l1 += 1
		# If only nums2 still contains numbers
		else:
			# Add to the list the value of nums2 and move
			# once the pointer for nums2
			half_nums.append(nums2[l2])
			l2 += 1
			
	# Depending if the quantity of numbers when merging nums1 and
	# nums2 is even or odd, is how we calculate the median.
	# If it's even, it means in the middle there will be 2 numbers
	# from which we have to get the average. If, on the other hand
	# is odd, we just have to get the number in the middle.
	if isEven:
		# We get the last 2 numbers from the half nums list
		# and compute the mean
		return float((half_nums[-1] + half_nums[-2])/2)
	else:
		# We just get the last number from the half nums list
		return float(half_nums[-1])


print(findMedianSortedArrays([1,3], [2])) # 2.00000
print(findMedianSortedArrays([1, 2], [3, 4])) # 2.50000
print(findMedianSortedArrays([], [1, 2, 3])) # 2.00000
print(findMedianSortedArrays([1, 2, 3], [])) # 2.00000
print(findMedianSortedArrays([10], [1, 2, 3, 4, 5, 6, 7, 8, 9])) # 5.50000
print(findMedianSortedArrays([1, 2, 3, 4, 5, 6, 7, 8, 9], [10])) # 5.50000
print(findMedianSortedArrays([], [])) # 0.00000