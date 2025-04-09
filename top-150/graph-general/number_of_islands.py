SEEN = ""
LAND = "1"
WATER = "0"


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        islands = 0

        # traverse the grid
        def mark_island(i, j):
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] != LAND:
                return
            grid[i][j] = SEEN
            mark_island(i + 1, j)
            mark_island(i - 1, j)
            mark_island(i, j + 1)
            mark_island(i, j - 1)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == LAND:
                    islands += 1
                    mark_island(i, j)

        return islands


"""
This was my recursive solution. It beats 85.77%. The time complexity is O(M*N) because every cell is processed at most 2 * (M*N) times.
I provide an iterative solution below
"""


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0

        m, n = len(grid), len(grid[0])
        islands = 0

        # Iterative DFS using a stack.
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":  # Found unvisited land.
                    islands += 1
                    stack = [(i, j)]
                    while stack:
                        x, y = stack.pop()
                        if 0 <= x < m and 0 <= y < n and grid[x][y] == "1":
                            grid[x][y] = "2"  # Mark as visited.
                            # Push neighbors onto the stack.
                            stack.append((x + 1, y))
                            stack.append((x - 1, y))
                            stack.append((x, y + 1))
                            stack.append((x, y - 1))
        return islands
