class Solution:
    def minPathCost(self, grid: List[List[int]], moveCost: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        for row in range(m - 2, -1, -1):
            for col in range(0, n):
                min_path_cost = float("inf")
                val = grid[row][col]
                for next_col in range(0, n):
                    move_cost = moveCost[val][next_col]
                    path_cost = grid[row + 1][next_col] + move_cost
                    min_path_cost = min(path_cost, min_path_cost)
                grid[row][col] += min_path_cost

        return min(grid[0])


"""
Store shortest path to cell starting from the bottom. O(1) space. m * n * n path complexity. 
"""
