# Time complexity: O(n) - getting min and max is on O(n)
#                         also iterating over the list
# Space complexity: O(1) - no extra space needed

def maxArea(height):
        # Left and right pointers
        l, r = 0, len(height)-1

        # To calculate the water, you get the difference between the
        # left and right pointer and multiply it by the minimum height
        # between the two heights in the positions l and r
        water = (r-l) * min(height[l], height[r])

        # While l and r don't cross each other
        while l < r:
                # Calculate the max of water from the previous max and
                # the new one
                water = max(water, (r-l) * min(height[l], height[r]))

                # Move the pointer where the height is the least
                if height[l] < height[r]:
                        l += 1
                else:
                        r -= 1

        return water


print(maxArea([1,8,6,2,5,4,8,3,7])) # 49
print(maxArea([1,1])) # 1
print(maxArea([0,2])) # 0
print(maxArea([2,3,4,5,18,17,6])) # 17
print(maxArea([1,3,2,5,25,24,5])) # 24