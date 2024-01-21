# Based on @meowmaple comment in Neetcode's video

# Time complexity: O(n^2)
# Space complexity: O(1) as we are doing the shifting of values in-place

# First we transpose the matrix, which is basically swapping the values
# across the diagonal, that is, it switches the row and column indices
# of the matrix A by producing another matrix, often denoted by AT
# Then we reverse each row of the matrix.


class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        # transpose
        for row in range(len(matrix)):
            for col in range(row, len(matrix)):
                temp = matrix[row][col]
                matrix[row][col] = matrix[col][row]
                matrix[col][row] = temp

        # reverse
        for row in matrix:
            row.reverse()


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
