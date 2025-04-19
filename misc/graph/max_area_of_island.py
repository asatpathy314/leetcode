class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.max_area = 0
        self.current_area = 0
        m = len(grid)
        n = len(grid[0])

        def solve_rec(i, j):
            if i < 0 or i >= m or j < 0 or j >= n:
                return

            if grid[i][j] == 1:
                grid[i][j] = 2
                self.current_area += 1
                solve_rec(i + 1, j)
                solve_rec(i - 1, j)
                solve_rec(i, j + 1)
                solve_rec(i, j - 1)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2 or grid[i][j] == 0:
                    continue
                solve_rec(i, j)
                self.max_area = max(self.max_area, self.current_area)
                self.current_area = 0

        return self.max_area


"""
DFS. We can mark seen islands with a 2. Explore the entire island.

Time complexity: O(m * n) (every island is considered a constant number of times)
Space Complexity: O(1) (we use the original grid so no extra space). let's say
we couldn't mutate the grid, then we might have to use at most O(m*n) space. 
"""
