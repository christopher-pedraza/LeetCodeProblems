# Time complexity: O(n) - even if we have 2 loops, as it's 2D array
#                         it's still O(n)
# Space complexity: O(n) - store the numbers in 3 dicts representing
#                          the rows, cols and squares

def isValidSudoku(board):
    # Using dict to assign an index to the sets
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
    cols = dict()
    rows = dict()
    squares = dict()

    # Iterate rows
    for row in range(9):
        # Iterate over the cols
        for col in range(9):
            # If the current position in the board is not empty
            if board[row][col] != ".":
                # Get the column set stored in cols with key col
                # If it doesn't exist, return empty set
                colsSet = cols.get(col, set())
                # Check if the current numbers is not in the set
                # It means that the board is still valid
                if board[row][col] not in colsSet:
                    # Add it to the set
                    colsSet.add(board[row][col])
                    # Store the new set 
                    cols[col] = colsSet
                # If not, the board is not valid
                else:
                    return False

                # Get the row set stored in rows with key row
                # If it doesn't exist, return empty set
                rowsSet = rows.get(row, set())
                # Check if the current numbers is not in the set
                # It means that the board is still valid
                if board[row][col] not in rowsSet:
                    # Add it to the set
                    rowsSet.add(board[row][col])
                    # Store the new set 
                    rows[row] = rowsSet
                # If not, the board is not valid
                else:
                    return False

                # Get the square set stored in squares with the key
                # being a tuple of row//3 and col//3. We divide by
                # 3 to group the rows and cols in groups of 3
                # If it doesn't exist, return empty set
                squaresSet = squares.get((row//3, col//3), set())
                # Check if the current numbers is not in the set
                # It means that the board is still valid
                if board[row][col] not in squaresSet:
                    # Add it to the set
                    squaresSet.add(board[row][col])
                    # Store the new set 
                    squares[(row//3, col//3)] = squaresSet
                # If not, the board is not valid
                else:
                    return False

    # If it finishes the loop, it means the board is valid
    return True




print(isValidSudoku([["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]))
print(isValidSudoku([["8","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]))
print(isValidSudoku([[".",".",".",".","5",".",".","1","."],[".","4",".","3",".",".",".",".","."],[".",".",".",".",".","3",".",".","1"],["8",".",".",".",".",".",".","2","."],[".",".","2",".","7",".",".",".","."],[".","1","5",".",".",".",".",".","."],[".",".",".",".",".","2",".",".","."],[".","2",".","9",".",".",".",".","."],[".",".","4",".",".",".",".",".","."]]))

