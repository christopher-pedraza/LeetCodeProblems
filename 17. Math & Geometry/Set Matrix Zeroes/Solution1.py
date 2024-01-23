# Neetcode's solution

# Time complexity: O(m*n)
# Space complexity: O(1)

# O(m*n) memory complexity approach:
# Time complexity greater than O(m*n) as we will be repeating the process of
# filling up with 0s the copy. Also, creating a copy would be O(m*n)
# Create a copy of the input matrix and every time we find a 0 in the matrix
# update the columns and rows of that copy to not create discrepancies with the
# correct 0s. For example if we had this matrix:
# 1 0 1
# 1 0 1
# 1 1 1
# The first time we encounter a zero, we will make the first row and second
# column 0s:
# 0 0 0
# 1 0 1
# 1 0 1
# However, this will lead to us adding 0s in the last column as we now put a 0
# in the top right position, which previously had a 1
# 0 0 0
# 1 0 0
# 1 0 0
# With a copy of the matrix, this problem can be solved as the reference we
# use to create columns and rows of 0s won't change, and we'll only change the
# copy.

# O(m+n) memory complexity approach
# O(m*n) time complexity as you will have to go through the matrix once to
# check the rows and columns that have 0s, and one more time for every array
# that puts the zeros. Really O(3*m*n)
# Actually, we only need to store the columns and rows that need to be updated
# instead of updating a copy of the matrix. Thus, we can forget about the copied
# matrix and just have 2 arrays: for the columns and the rows. In these, we will
# store the column and row index where we find the 0 in the input array so at
# the end, we can update the matrix inplace without having problems.

# O(1) memory complexity approach
# O(m*n) time complexity
# We will store the columns and rows that need to be zeroed in the first
# position of the rows and columns of the input matrix, we will just need to
# have one extra variable. For the columns that need to be zeroed, we will put
# a 0 in the corresponding column in the first row. For the case of the columns
# as there would be a overlap in the top left position with the rows, we will
# store if the first row needs to be 0ed in the extra variable, and for the
# other rows, in the first column of the corresponding row. We will go from top
# to bottom, and for every row, from left to right. This way, there won't be
# any problem with updating a position with a 0 that previously didn't have a 0.


class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        ROWS, COLS = len(matrix), len(matrix[0])

        # Extra variable to represent if the first row should have 0s
        rowZero = False

        # Determine which rows/cols need to be zero
        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0:
                    # Set the first row in the current column to 0 to represent
                    # that this column should be zeroed
                    matrix[0][c] = 0
                    # As the first row (0-indexed row) is represented with the
                    # extra variable, only if we are refering to a different
                    # row from the first one, will we update the first column
                    # in the current row. If we are in the first row, then we
                    # just update the extra variable. This way we are skipping
                    # the top left position
                    if r > 0:
                        matrix[r][0] = 0
                    else:
                        rowZero = True

        # Zero everything except the first column and row. This to prevent
        # problems with the top left position which should only represent the
        # columns, but with this loop, it could think that the row should
        # also be 0ed
        for r in range(1, ROWS):
            for c in range(1, COLS):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0

        # If the top left position is 0, it means we can fill with 0s the first
        # column
        if matrix[0][0] == 0:
            for r in range(ROWS):
                matrix[r][0] = 0

        # If the extra variable is True, it means the first row has to be 0ed
        if rowZero:
            for c in range(COLS):
                matrix[0][c] = 0


s = Solution()

matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
s.setZeroes(matrix)
# Expected output: [[1,0,1],[0,0,0],[1,0,1]]
print(matrix)

matrix = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
s.setZeroes(matrix)
# Expected output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
print(matrix)
