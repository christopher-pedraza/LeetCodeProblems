# Neetcode.io solution

# Time complexity: O(n) - even if we have 2 loops, as it's 2D array
#                         it's still O(n)
# Space complexity: O(n) - store the numbers in 3 dicts representing
#                          the rows, cols and squares

# Not needed in leetcode:
from collections import defaultdict

def isValidSudoku(board):
    # Using dict to assign an index to the sets
    # Default dics helps us to prevent the need of
    # creating a new set the first time
    # The keys for the rows and cols will be the row
    # and col respectively. However, for the squares,
    # we will use a tuple of the rows and columns 
    # divided by 3. Notice that we'll use integer
    # division so we can group every 3 numbers:
    #   0 // 3 = 0
    #   1 // 3 = 0
    #   2 // 3 = 0
    #   3 // 3 = 1
    #   4 // 3 = 1
    #   5 // 3 = 1
    #   6 // 3 = 2
    #   7 // 3 = 2
    #   8 // 3 = 2
    cols = defaultdict(set)
    rows = defaultdict(set)
    squares = defaultdict(set)  # key = (r//3, c//3)

    # Iterate over the rows and columns
    for r in range(9):
        for c in range(9):
            # If the current position in the board empty you
            # skip it
            if board[r][c] == ".":
                continue
            # Check if the current value in the board is not
            # in either the current row, col, or square
            # If it is, it means the board is not valid
            # Time complexity of checking a hashmap is O(1)
            if (
                board[r][c] in rows[r] or
                board[r][c] in cols[c] or
                board[r][c] in squares[(r // 3, c // 3)]
            ):
                return False

            # If it's still valid, you add the current value
            # to the hash maps
            cols[c].add(board[r][c])
            rows[r].add(board[r][c])
            squares[(r // 3, c // 3)].add(board[r][c])

    # If it finishes the loop, it means the board is valid
    return True

print(isValidSudoku([["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]))
print(isValidSudoku([["8","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]))
print(isValidSudoku([[".",".",".",".","5",".",".","1","."],[".","4",".","3",".",".",".",".","."],[".",".",".",".",".","3",".",".","1"],["8",".",".",".",".",".",".","2","."],[".",".","2",".","7",".",".",".","."],[".","1","5",".",".",".",".",".","."],[".",".",".",".",".","2",".",".","."],[".","2",".","9",".",".",".",".","."],[".",".","4",".",".",".",".",".","."]]))