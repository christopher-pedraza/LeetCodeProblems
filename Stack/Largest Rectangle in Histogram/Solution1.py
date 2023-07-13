# Neetcode.io solution

# Time complexity: O(n)
# Space complexity: O(n)

# Not needed in leetcode:
from typing import List

# The idea is that we are going to transverse accross
# the list of heights adding the heights to a stack.
# If the height is greater or equal than the previous
# one, we don't have to do anything to the previous
# heights stored in the stack, however, if the height
# is smaller, we have to pop from the top any height
# that is greater than the smaller height we just got
# in the list. This is because any height bigger than
# the new height won't be able to extend that height
# To make it clearer, here are some cases:
#
#   X⁻⁻⁻Cannot extend any further the height of 2
#   X X
#
#     X⁻⁻⁻We can continue to extend the height of 2
#   X X
#
#   X X⁻⁻⁻We can continue to extend the height of 2
#   X X
#
#         X⁻⁻⁻⁻As the next is 3, the 4 can't extend
#       X X X  any further, while the other heights
#     X X X X  still can
#   X X X X X
#
#         X
#       X X⁻⁻⁻⁻Here not only the four, but also the 3
#     X X X X
#   X X X X X

# We are going to have a stack that stores the current
# height that is being read from the list and the
# index from which it extends. If the new height is
# greater than the previous, the index will be the
# position in the list. However, if the new height is
# smaller, then we are going to pop the previous heights
# that are bigger than it and assign the index of that
# height as the index of the previous' bigger or equal
# heights. For example:
# 
#                       Stack
#       X X         index   height
#   X   X X X         0       2 ─┐
#   X X X X X X       0       1  ┴──(pop previous as
#   2·1·3·3·2·1       2       3      height is smaller)
#
# Everytime we pop a number, we are going to add to
# another stack the max area we could calculate with
# that height. In the previous example, we would have
# calculated an area of 2 (h=2, w=1) when popping the
# height of 2. Also, when we get the 2 after the 3's
# we calculate the area of the 3's before popping them
# getting 6 (h=3, w=2). The 2 that made us pop the 3's
# starts at index 2 (the index of the first 3). After
# the 2 we get a 1, making us pop the 2. So we get
# an area of 6 (h=2, w=3) before popping it. Then the
# index of the new 1 will extend all the way to the
# beginning, so we assing a 0 as its index. 

# As we saw, we calculate the area each time we pop a
# number as that number can't extend any further.
# However, there can be numbers that extend all the
# way to the end, meaning they were never popped. So
# After going through the list of heights, we need to
# get the area for everything that stayed in the stack
#
#       X       | Stack |   | Max Area |
#     X X       | i | h |   |          |
#     X X       | 0 | 2 |
#     X X   X  
# X   X X X X  
# X X X X X X  
# ^
#
#
#       X       | Stack |   | Max Area |
#     X X       | i | h |   |    2     |
#     X X      -|-0-|-2-|-
#     X X   X   | 0 | 1 |
# X   X X X X  
# X X X X X X  
#   ^
#
#
#       X       | Stack |   | Max Area |
#     X X       | i | h |   |    2     |
#     X X      -|-0-|-2-|-
#     X X   X   | 0 | 1 |
# X   X X X X   | 2 | 5 |
# X X X X X X  
#     ^
#
#
#       X       | Stack |   | Max Area |
#     X X       | i | h |   |    2     |
#     X X      -|-0-|-2-|-
#     X X   X   | 0 | 1 |
# X   X X X X   | 2 | 5 |
# X X X X X X   | 3 | 6 |
#       ^
#
#
#       X       | Stack |   | Max Area |
#     X X       | i | h |  -|----2-----|-
#     X X      -|-0-|-2-|- -|----6-----|-
#     X X   X   | 0 | 1 |   |    10    |
# X   X X X X  -|-2-|-5-|-
# X X X X X X  -|-3-|-6-|-
#         ^     | 2 | 2 |
#
#
#       X       | Stack |   | Max Area |
#     X X       | i | h |  -|----2-----|-
#     X X      -|-0-|-2-|- -|----6-----|-
#     X X   X   | 0 | 1 |   |    10    |
# X   X X X X  -|-2-|-5-|-
# X X X X X X  -|-3-|-6-|-
#           ^   | 2 | 2 |
#               | 5 | 3 |
#
# Checking the heights that are still in the stack
#
# | Stack |                     | Max Area |
# | i | h |                     |    10    |
# | 0 | 1 | -> 1x((5+1)-0)=6┐
# | 2 | 2 | -> 2x((5+1)-2)=8┐
# | 5 | 3 | -> 3x((5+1)-5)=3┐
#              │    │   │   └area
#              │    │   │
#              │    │   └start index of height
#            height │
#                   └last index of list + 1 as the
#                    height managed to extend up to
#                    the end of the histogram
# 
# None of the areas is greater than the previous max
# area, so we don't update it

def largestRectangleArea(heights: list[int]) -> int:
	# Will contain the max area that has been found
    maxArea = 0
    # Stack to store the index from which a certain
    # height begins and the height itselft
    stack = []  # pair: (index, height)

    # Iterate over the heights of the list
    for i, h in enumerate(heights):
    	# Store the start index of the current height
    	# as the index from the list. We still don't
    	# know if we can extend it backwards
        start = i
        # While the stack is not empty and the new height
        # we just found is smaller than the top value
        # from the stack. If so, we have to pop the top
        # value from the stack, calculate the area with it
        # and extend the starting index of the current
        # height backwards
        while stack and stack[-1][1] > h:
        	# We pop the top value
            index, height = stack.pop()
            # Calculate the area and keep the max from the
            # previous max area and the calculated
            # To get the area we compute height*width, in
            # which the width is the current index minus
            # the starting index of the height
            maxArea = max(maxArea, height * (i - index))
            # Update the start index with the start index
            # of the height we just popped. As the height
            # we popped is greater than the current one
            # we know that the index from which it starts
            # can also be the starting index for the lower
            # height
            start = index
        # Add the new height to the start with the
        # calculated starting index (this could be the
        # current index taken from the list, or if the top
        # height in the stack is greater than this height,
        # take the index from which this greater height
        # started)
        stack.append((start, h))

    # For any height that was able to extend to the end of
    # the histogram, as they are still in the stack, we
    # iterate over it computing the area.
    for i, h in stack:
        # Calculate the area and keep the max from the
        # previous max area and the calculated
        maxArea = max(maxArea, h * (len(heights) - i))

    return maxArea

print(largestRectangleArea([2,1,5,6,2,3])) # 10
print(largestRectangleArea([2,4])) # 4