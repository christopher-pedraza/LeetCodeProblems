# Neetcode.io solution

# Time complexity: O(logm) + O(logn) = O(log(m*n))
#                  This because we first did a binary search for
#                  the row that could contain the target, and then
#                  a binary search for the target in the row
# Space complexity: O(1)

# Same solution as mine (Solution2), the only difference is that
# here when we find the row that can contain the target we exit
# the loop and now do a binary search in that row, meaning we
# separate the process in 2.
# On the other hand, in my solution when I find a row that can
# contain the target, I do binary search over that row inside
# the same loop.

def searchMatrix(matrix: list[list[int]], target: int) -> bool:
    # Dimensions of the matrix
    ROWS, COLS = len(matrix), len(matrix[0])

    # Top and bottom pointers
    # The top starts at the top most row, the other one at the
    # quantity of rows - 1 as it's zero based
    top, bot = 0, ROWS - 1

    # Do binary search until we either find it or determine it
    # isn't in any row
    while top <= bot:
        # Get the middle row
        middle_row = (top + bot) // 2
        # If the target is greater than the last value in the
        # row, the it means that the target can only be on the
        # rows below the middle row. For this, we move the top
        # pointer up to the middle row, and add 1 to not include
        # the middle row again
        if target > matrix[middle_row][-1]:
            top = middle_row + 1
        # However, if the target is smaller than the first value,
        # then it means it can only be on the rows on top of the
        # middle, so we move the bottom pointer to the middle - 1
        elif target < matrix[middle_row][0]:
            bot = middle_row - 1
        # If target is not greater than the last value or smaller
        # than the first value, we exit the loop as it is within
        # the range of the current middle row
        else:
            break

    # If we never found a row that contained the target value, thus
    # breaking from the loop, we need to return false. In order to
    # determine we didn't find it, we check if the top and bottom
    # pointers crossed each other, this means the loop ended without
    # completely
    if not (top <= bot):
        return False

    # We're now going to do binary search over the middle row to see
    # if the target is inside this row (we know that this row CAN
    # contain the target as it's between the range of the first and
    # last value in the row, however we cannot be sure it WILL be 
    # in the row, so we do the search) 
    middle_row = (top + bot) // 2
    # Left and right pointers
    l, r = 0, COLS - 1

    # While the pointers don't cross each other
    while l <= r:
        # Compute the middle col
        middle_col = (l + r) // 2
        # If target is greater than the middle point, we
        # need to search the right side from the middle.
        # We move the left pointer one position to the
        # right from the middle
        if target > matrix[middle_row][middle_col]:
            l = middle_col + 1
        # If target is smaller than the middle point, we
        # need to search the left side from the middle.
        # We move the right pointer one position to the
        # left from the middle
        elif target < matrix[middle_row][middle_col]:
            r = middle_col - 1
        # If the target is not smaller or greater, we found
        # the target and return true
        else:
            return True

    # If the loop finished without ever returning true, it
    # means the target isn't in the matrix
    return False

print(searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3)) # True
print(searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 13)) # False