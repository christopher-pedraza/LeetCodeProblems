# Time complexity: O(logn)
# Space complexity: O(1)

# Someone in the comments of the neetcode video
# shared this version saying it was easier to
# read. The only differences are the if statements

def search(nums: list[int], target: int) -> int:
	# Left and right pointers
	l, r = 0, len(nums) - 1

	# While the pointers don't cross each other
	while l <= r:
		# Get the middle pointer
	    mid = (l + r) // 2
	    
	    # If the target is in the middle pointer
        # we return the mid index as we already 
        # found it
	    if nums[mid] == target:
	        return mid
	    
	    # We now need to check where the mid pointer is
        # is it in the right or left sorted portion?
        # Left sorted portion
        # We know we're in the left sorted portion if
        # the value in the middle pointer is greater or
        # equal than the value in the left pointer
	    # Middle pointer is in the left sorted portion
	    elif nums[mid] >= nums[l]:
	    	# If the target is greater than the left value
	    	# and also less than the middle value, we need
	    	# to continue searching the left side
	        if nums[l] <= target <= nums[mid]:
	            r = mid - 1
            # Search the right side
	        else:
	            l = mid + 1
	            
	    # Middle pointer is in the right sorted portion
	    else:
	    	# If the target is greater than the middle 
	    	# value and also less than the right value, we 
	    	# need to continue searching the right side
	        if nums[mid] <= target <= nums[r]:
	            l = mid + 1
            # Search the left side
	        else:
	            r = mid - 1
	      
	# If we never found the target, return -1      
	return -1

print(search([4,5,6,7,0,1,2], 0)) # 4
print(search([4,5,6,7,0,1,2], 3)) # -1
print(search([1], 0)) # -1
print(search([6,7,0,1,2,3,4,5], 3)) # 5