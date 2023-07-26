# Neetcode.io solution

# Time complexity: O(logn)
# Space complexity: O(1)

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
        if target == nums[mid]:
            return mid

        # We now need to check where the mid pointer is
        # is it in the right or left sorted portion?
        # Left sorted portion
        # We know we're in the left sorted portion if
        # the value in the middle pointer is greater or
        # equal than the value in the left pointer
        if nums[l] <= nums[mid]:
            # If the target is greater than the middle or
            # less than the left most value, we search the
            # right portion
            if target > nums[mid] or target < nums[l]:
                l = mid + 1
            # If target is less than the middle and greater
            # than the left, we search the left portion
            else:
                r = mid - 1
        # Right sorted portion
        else:
            # If the target is less than the middle or 
            # greater than the right most value, we have
            # to search the left portion
            if target < nums[mid] or target > nums[r]:
                r = mid - 1
            # If target is greater than the middle and
            # smaller than the value at the left, we
            # search the right portion of the array
            else:
                l = mid + 1

    # If we never found the target, return -1
    return -1

print(search([4,5,6,7,0,1,2], 0)) # 4
print(search([4,5,6,7,0,1,2], 3)) # -1
print(search([1], 0)) # -1
print(search([6,7,0,1,2,3,4,5], 3)) # 5