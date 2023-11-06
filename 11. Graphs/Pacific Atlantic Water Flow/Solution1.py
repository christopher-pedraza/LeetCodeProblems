# Neetcode.io solution

# Time complexity: O(n*m) just visit the cells once
# Space complexity: O(n*m) we saved in a Hashset the positions that have
#                   been visited so we don't visit them again

# A naive solution would be to apply DFS from each and every cell to see
# if we can get from that cell to both oceans. I also thought we could add
# a backtracking logic so we don't have to repeat the processing of
# certain paths. For example, if we know that we can get from cell (3, 5)
# to both oceans and we are coming in this path: (3, 6) -> (3, 5), then we
# know that from (3, 6) we can also arrive at both oceans and don't have
# to process the whole path again.

# However, neetcode's solution is a little bit different. Instead of
# applying dfs from every cell, we will start dfs from the border cells
# as we know these cells already touch one ocean. We will start dfs from
# the top row and left column to see all the cells that can get to the
# pacific ocean, and start dfs from the bottom row and right column to
# see the cells that can arrive at the atlantic ocean. After that, the
# cells that were reached by both oceans are the ones that are going to
# be returned as the output. An important thing to consider is that the
# water flows from the island to the ocean from cells that have a higher
# altitude, to the cells that have a lower one. As we are going to start
# the dfs from the ocean to the center of the island, we will reverse
# this: When pathing from the border to the center, we will go to the
# cells that have an equal or higher altitud.


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # Get the dimensions of the island
        ROWS, COLS = len(heights), len(heights[0])
        # Hashsets that contain all the cells that can be reached from
        # each of the two oceans (the cells that are in both sets at the
        # end are the ones that can be reached by both oceans)
        pac, atl = set(), set()

        # Visit is either the pacific or atlantic set
        # prevHeight is the height of the cell from which we are coming
        def dfs(r, c, visit, prevHeight):
            # If the current cell is already visited, out of bounds or
            # has a lower height (remember we reversed it) than the
            # previous cell, we return. We are checking for out of bounds
            # because we are not trying to arrive to the oceans, we are
            # reversing it and trying to arrive at all other cells
            if (
                (r, c) in visit
                or r < 0
                or c < 0
                or r == ROWS
                or c == COLS
                or heights[r][c] < prevHeight
            ):
                return

            # We are visiting a new and valid cell so we add it to
            # received set
            visit.add((r, c))

            # Apply dfs to the four directions
            dfs(r + 1, c, visit, heights[r][c])
            dfs(r - 1, c, visit, heights[r][c])
            dfs(r, c + 1, visit, heights[r][c])
            dfs(r, c - 1, visit, heights[r][c])

        # Go to all the columns in the first and last row
        for c in range(COLS):
            # Apply a dfs in the first row and every column
            # We pass the pacific set as the first row corresponds to
            # the pacific ocean
            # Pass the previous height, which is the one in the first row
            # and current column we are iterating
            dfs(0, c, pac, heights[0][c])
            # Apply dfs from the last row, which is for the atlantic
            # ocean, and every column
            # We pass the atlantic set as the last row corresponds to
            # this ocean.
            # The prevous heigh will be the cell in last row and in the
            # current column we are iterating
            dfs(ROWS - 1, c, atl, heights[ROWS - 1][c])

        # Apply dfs from all rows in the first and last column
        for r in range(ROWS):
            # The first column is the pacific
            dfs(r, 0, pac, heights[r][0])
            # The last column is the atlantic
            dfs(r, COLS - 1, atl, heights[r][COLS - 1])

        # Check for every cell if it is in both sets. If it's then it
        # means that cell can reach both oceans
        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pac and (r, c) in atl:
                    # Add the cell to the result as it can reach both
                    # oceans
                    res.append([r, c])
        return res
