# Neetcode.io's solution

# Time complexity: O(n^2)
# Space complexity: O(1) as we are doing the shifting of values in-place

# To solve this problem, we will have 4 pointers for the boundaries of the matrix: Left, Right, Top, Bottom.
# We will rotate element by element from the outer "ring/square" to the innermost. For example, in a 4x4 matrix:
#
#   L     R
# T □ □ □ □
#   □ □ □ □
#   □ □ □ □
# B □ □ □ □
# We will move the element in the (T, L) position to the (T, R). Then the (T, R) to (B, R), and (B, R) to (B, L),
# and finally, (B, L) to the initial position of (T, L). Then we will shift from the pointers by 1 position to
# continue with the rest of the values: (T, L+1) to (T-1, R), (T-1, R) to (B, R-1), (B, R-1) to (B+1, L), and finally,
# (B+1, L) to (T, L+1). Lastly, for the outermost ring, we shift (T, L+2) to (T-2, R), (T-2, R) to (B, R-2), (B, R-2)
# to (B+2, L), and (B+2, L) to (T, L+2). As we already rotated the corners, we already finished with the outermost ring
# and can pass to the next ring by shifting the pointers: L->L+1, R->R-1, T->T-1, B->B+1. This means that for every layer
# we will be doing n-1 operations (for a 3x3 matrix just 2 in the outer most ring and then 1 [which is in-place so we
# could ignore it], and for a 4x4 3 operations).
# Left pointer should always be less than Right, so once they cross, we can stop.
#
# To preven having to have temporary variables for every shift we do, we can do the shifting in reverse and only store
# the first value in a temporary variable. All other shifts won't need temporary variables as we will be replacing values
# that have already moved to another position, so it's safe to replace them:
#
# Original
# Temp: -
# 5  □  □  11
# □  □  □  □
# □  □  □  □
# 15 □  □  16
#
# Save the initial value (5) in a temp variable and move the second value (15) to that position
# Temp: 5
# 15 □  □  11
# □  □  □  □
# □  □  □  □
# 15 □  □  16
#
# Move 16 to the place of 15
# Temp: 5
# 15 □  □  11
# □  □  □  □
# □  □  □  □
# 16 □  □  16
#
# Move 11 to the place of 16
# Temp: 5
# 15 □  □  11
# □  □  □  □
# □  □  □  □
# 16 □  □  11
#
# Move 5 from the temp variable to the place of 11
# Temp: -
# 15 □  □  5
# □  □  □  □
# □  □  □  □
# 16 □  □  11


class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        l, r = 0, len(matrix) - 1
        while l < r:
            # Iterate over the entire row except the last element to consider the elements in between the corners
            # Basically, to handle L, L+1, L+2...
            for i in range(r - l):
                # As it's a square matrix
                top, bottom = l, r

                # save the topleft as a temporary variable (last comments in the explanation)
                topLeft = matrix[top][l + i]

                # Move the elements to the correct spot. Notice we are just replacing the values without storing
                # what is inside them, this, as already explained, is due to the fact that we are doing it in
                # reverse, thus, we only need to store a value once, which is the one in the top left position.
                # We are doing the shift counterclockwise.
                # move bottom left into top left
                matrix[top][l + i] = matrix[bottom - i][l]
                # move bottom right into bottom left
                matrix[bottom - i][l] = matrix[bottom][r - i]
                # move top right into bottom right
                matrix[bottom][r - i] = matrix[top + i][r]
                # move top left into top right (this last one is from the temp variable)
                matrix[top + i][r] = topLeft

            # Shift the left and right pointers, we don't need to shift the T and B as they are updated with the value of
            # L and R.
            r -= 1
            l += 1


s = Solution()

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]
s.rotate(matrix)
# [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
print(matrix)

matrix = [
    [1, 2],
    [3, 4],
]
s.rotate(matrix)
# [[3, 1], [4, 2]]
print(matrix)

matrix = [[1]]
s.rotate(matrix)
# [[1]]
print(matrix)

matrix = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25],
]
s.rotate(matrix)
# [[21, 16, 11, 6, 1], [22, 17, 12, 7, 2],
# [23, 18, 13, 8, 3], [24, 19, 14, 9, 4],
# [25, 20, 15, 10, 5]]
print(matrix)
