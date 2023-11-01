# Neetcode.io solution

# Time complexity: O(n * m * 4^l) where n and m are the dimensions of the
#                  board and l the size of the word we are looking for. It's
#                  4^l because we go to the four directions for every single
#                  cell (one of the directions gets removed as we cannot
#                  repeat the cell, but we still go to it). And it's n*m as
#                  we have to check every cell of the board.

# We will do a recursive backtracking to check all the combinations that
# can be formed from the board. There's really no efficient way to do it, so
# we just do a backtracking, and in this case, we will use dfs so we can go 
# to all other cells starting from every cell in the board.

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # Get the dimensions of the board
        ROWS, COLS = len(board), len(board[0])
        # We will use a global set to keep track of the path we are taking.
        # We will add the cells we are visiting and then remove them when we
        # don't need them anymore (when we are exploring another path).
        path = set()

        # Receive the current position and the index of character in the word 
        # we are currently looking for
        def dfs(r, c, i):
            # If we reached the end of the word, it means we found the word in
            # a path so we return True
            if i == len(word):
                return True
            
            # Conditions that will make invalid our search, thus, return False
            if (
                # If we go out of bounds
                min(r, c) < 0
                or r >= ROWS
                or c >= COLS
                # If the characer in the current position we are exploring is
                # not the character we are looking for in the current index i
                # in the word (it means this path doesn't form the word)
                or word[i] != board[r][c]
                # If the current cell is already in the path, it means we came
                # back to a cell that was already used in the path, and as we
                # cannot reuse cells, it's also invalid
                or (r, c) in path
            ):
                return False
            
            # If none of the previous conditions happens, it means the current
            # cell contains the next character of the word we are looking for,
            # it's not an invalid cell, and we still haven't found the complete
            # word.
            path.add((r, c))

            # We go to the four directions from the current cell (at least one
            # of the directions will be invalid as it will be the cell from
            # which we arrived, or if it's the first cell, it will be out of
            # bounds)
            res = (
                # Do DFS to the four different directions and if any of the 
                # calls returns True, res will become True as it's using or's
                # Notice we move the index of i + 1 as we are now looking for
                # the next character in the word
                dfs(r + 1, c, i + 1)
                or dfs(r - 1, c, i + 1)
                or dfs(r, c + 1, i + 1)
                or dfs(r, c - 1, i + 1)
            )

            # After ending the current path, we remove the current cell from
            # 'path' so this cell can be used in another path
            path.remove((r, c))

            # Return whether we found the word in any path or not
            return res

        # To prevent TLE,reverse the word if frequency of the first letter is
        # more than the last letter's
        # For example, if we are looking for word "hi", in an array of
        # [h,h,h,i,], if you choose to match the first char "h" to start the
        # dfs, it will trigger 3 times. However, if you choose the last char 
        # "i" to start dfs, it would only trigger once. And by trigger, I mean
        # it will try to find a path starting at H 3 times as the starting
        # letter was found, however, if we start from I, we just need to create
        # 1 path, and look for the following chars in the word afterwards.
        
        # This is neetcode's way of getting the count of the characters in
        # the board: 
        # count = defaultdict(int, sum(map(Counter, board), Counter()))
        # if count[word[0]] > count[word[-1]]:
        #     word = word[::-1]

        # This came from @Lulit999's comment in Neetcode's video:
        # Cound the characters of the word and the board
        word_dict = Counter(word)
        board_dict = Counter(itertools.chain.from_iterable(board))
        # If any of the characters needed to form the word doesn't have
        # enough cells with it, it means the word cannot be formed with
        # the board. Basically, we are checking if the number of letters in
        # the board is enough to build the word
        if any (count > board_dict[char] for char, count in word_dict.items()):
            return False
        
        # Here we are reversing word if the count of the first letter occurs
        # more times than the last letter of the word as previously explained
        # in this code (the comment starting with "To prevent TLE...")
        if board_dict[word[0]] > board_dict[word[-1]]:
            word = word[::-1]
            
        # We go through all the positions in the board to start DFS from that
        # cell
        for r in range(ROWS):
            for c in range(COLS):
                # If DFS ever returns true, we stop going through all the cells
                # and return true
                if dfs(r, c, 0):
                    return True
        # If we go through all the positions in the board and never return true
        # it means the word cannot be found in the board
        return False
