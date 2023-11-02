# Neetcode.io solution

# Time complexity: O(n) where n is the number of cells
# Space complexity: O(n) where n is the number of cells


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # If we get an empty grid, we return 0
        if not grid:
            return 0

        # Get the dimensions of the grid
        rows, cols = len(grid), len(grid[0])
        # Set to keep track of the visited cells
        visited = set()
        # Count the number of islands
        islands = 0

        def bfs(r, c):
            q = deque()
            # Mark as visited the position
            visited.add((r, c))
            # Add to the queue the current position
            q.append((r, c))

            # While the queue is not empty
            while q:
                # Get the last position from the queue
                row, col = q.popleft()

                # There are four direction from every cell. Go to all the directions
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                for dr, dc in directions:
                    # Get the new position by adding to the current position the movement
                    r, c = row + dr, col + dc
                    # Check if the position is in bounds, has a 1, and hasn't been visited
                    if (
                        (r) in range(rows)
                        and (c) in range(cols)
                        and grid[r][c] == "1"
                        and (r, c) not in visited
                    ):
                        # Add the new position to the queue to later perform BFS from that
                        # position
                        q.append((r, c))
                        # Add the new position to the visited cells set
                        visited.add((r, c))

        # Go through the rows and columns of the grid
        for r in range(rows):
            for c in range(cols):
                # If the cell has a 1, and has not been visited
                if grid[r][c] == "1" and (r, c) not in visited:
                    # We perform BFS and after going through all the adyacent
                    # cells we increase the number of islands
                    bfs(r, c)
                    islands += 1

        # Return the number of islands
        return islands
