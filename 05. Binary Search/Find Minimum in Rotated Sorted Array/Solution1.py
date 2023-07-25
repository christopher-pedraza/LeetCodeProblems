# Neetcode.io solution

# My solution (Solution2.py) is also very
# good and well explained

# Time complexity: O(logn)
# Space complexity: O(1)

def findMin(nums: list[int]) -> int:
    # Left and right pointers
    l, r = 0, len(nums) - 1
    # Stores the current mid that's been found
    curr_min = float("inf")
    
    # While the pointers don't cross each other
    while l < r:
        # Get the middle pointer
        mid = (l + r) // 2
        # Calculate the minimum from the previous
        # min and the current value in the middle
        curr_min = min(curr_min, nums[mid])
        
        # If the value in the middle is greater
        # than the value at the right, it means
        # the right side contains the minimum
        # value
        if nums[mid] > nums[r]:
            # Move the left pointer to search the
            # right side
            l = mid + 1
        # Left side has the minimum
        else:
            # Move the right pointer to search the
            # left side
            r = mid - 1 
            
    # Return the minimum from the value at the left
    # and the previous minimum
    return min(curr_min,nums[l])

print(findMin([3,4,5,1,2])) # 1
print(findMin([4,5,6,7,0,1,2])) # 0
print(findMin([11,13,15,17])) # 11
print(findMin([-500])) # -500
print(findMin([-500, 500])) # -500