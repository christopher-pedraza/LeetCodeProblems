# Neetcode's solution

# Time complexity: O(m*n) as we have to visit all the elements in the matrix at least once
# Space complexity: O(m*n) as we have to create a list with all the elements from the matrix reordered. It would be
#                   O(1) if we don't consider the output as extra memory.

# A way to solve it is by dividing the matrix by rings, which basically means, dividing the problem in subproblems.
# We will first do the outermost ring going Right->Down->Left->Up until we arrive at an element that has already been
# processed. After that, we will move the pointers that represent the boundary of the ring by 1 position and repeat
# the same process. The pointers would be: Left, Right, Top, Bottom. Once the pointers Left-Right or Top-Bottom
# point to the same column/row respectively, it means we have already process everything. The Right and Bottom
# pointers will be 1 position after the end column/row respectively to make the code easier.
# Also, we will always start at our [Top, Left] position, then go right UNTIL we arrive at our Right boundary. When
# we reach it, we know that we have to go down. However, as we have already processed the complete first row, we also
# know that we can move the Top boundary one position downwards as the rectangle has shrank. The same will happen
# when we process the whole right column, we will shift the Right pointer one position to the left as the matrix
# shrank again. When we arrive at the Left boundary, we know that we have to still process that value (as the index
# is inclusive, different from the Right boundary), and we shift the Bottom boundary upwards once to mark the last
# row as processed. We then go up until we reach the Top boundary, which is also inclusive like the Left one. And
# then we go right, after shifting the Left boundary as the first column is already processed. This process will
# repeat until the pairs of pointers (Left-Right or Top-Bottom) are in the same position (same column/row).


class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        res = []
        # Right is the number of columns, which is the last column index + 1
        left, right = 0, len(matrix[0])
        # Bottom is the number of rows, which is the last row index + 1
        top, bottom = 0, len(matrix)

        # Keep looping until one of the pairs of pointers cross or are equal
        while left < right and top < bottom:
            # Get every value in the top row
            for i in range(left, right):
                # Add the value top the result. We know that we are in the top row, and the column is represented
                # by i
                res.append(matrix[top][i])
            # Shift the top boundary by one downwards
            top += 1

            # Get every value in the right col
            # We loop from Top to Bottom as we already incremented the Top index, so we won't have repeated elements
            for i in range(top, bottom):
                # The column is R-1 as we are out of bounds in the R index
                res.append(matrix[i][right - 1])
            # Shift the Right boundary as we already processed the Right column
            right -= 1

            # In case the pointers already cross each other (for example, if we have a 1 column/row matrix)
            if not (left < right and top < bottom):
                break

            # Get every value in the bottom row
            # Go from the right to the left. Substract 1 from the right as the beginning index of the range is
            # inclusive and the right pointer is out of bounds, and substract 1 from the left pointer as the end
            # index is not inclusive, so we need to go 1 more to the left.
            for i in range(right - 1, left - 1, -1):
                # As the Bottom index is out of bounds, substract 1 from it
                res.append(matrix[bottom - 1][i])
            # Move the Bottom pointer as we processed the bottom row
            bottom -= 1

            # Get every value in the left col
            # Go in reverse order from Bottom to Top. The -1 is explained in the Bottom Row code
            for i in range(bottom - 1, top - 1, -1):
                res.append(matrix[i][left])
            left += 1

        return res


s = Solution()

# [1,2,3,6,9,8,7,4,5]
print(s.spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
# [1,2,3,4,8,12,11,10,9,5,6,7]
print(s.spiralOrder([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]))
