# Time complexity: O(n) where n is the number of cells
# Space complexity: O(1) we will reuse the grid, so no extra data structure is used


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # If we get an empty grid, we return 0
        if not grid or not grid[0]:
            return 0

        # Get the dimensions of the grid
        rows, cols = len(grid), len(grid[0])
        # Count the number of islands
        islands = 0

        def dfs(r, c, grid):
            # Check if the position is out of bounds, has a 0, or has been visited
            # If so, return from the dfs
            if r not in range(rows) or c not in range(cols) or grid[r][c] == "0":
                return

            # Add to the visited set the current position
            grid[r][c] = "0"

            # There are four direction from every cell. Go to all the directions
            directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            # Apply dfs to the four directions
            for dr, dc in directions:
                dfs(r + dr, c + dc, grid)

        # Go through the rows and columns of the grid
        for r in range(rows):
            for c in range(cols):
                # If the cell has a 1, and has not been visited (the visited cells are marked with "0")
                if grid[r][c] == "1":
                    # We increase the island count and do dfs from the current cell
                    islands += 1
                    dfs(r, c, grid)

        # Return the number of islands
        return islands
