class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        dp = [[-1 for _ in range(n)] for _ in range(m)]

        starting_col = 0
        starting_row = 0

        # diagonal DP traversal
        while starting_row != m:
            row = starting_row
            col = starting_col
            if row == 0 and col == 0:
                dp[0][0] = grid[0][0]
            else:
                while row < m and col > -1 and col < n:
                    prev_above = dp[row - 1][col] if row - 1 >= 0 else float("inf")
                    prev_left = dp[row][col - 1] if col - 1 >= 0 else float("inf")
                    dp[row][col] = min(
                        grid[row][col] + prev_above, grid[row][col] + prev_left
                    )
                    row += 1
                    col -= 1

            if starting_col < n - 1:
                starting_col += 1
            else:
                starting_row += 1

        return dp[m - 1][n - 1]


"""
My solution is relatively simple and directly does diagonal path traversal.
However, there's a much easier soln that directly fills in the grid horizontally.
This keeps in mind that all the top cells need only consider cells to the left.
Everything in the left col need only consider cells above. 
"""


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]

        for r in range(m):
            for c in range(n):
                # base case
                if r == 0 and c == 0:
                    dp[r][c] = grid[r][c]
                # top row
                elif r == 0:
                    dp[r][c] = grid[r][c] + dp[r][c - 1]
                # left col
                elif c == 0:
                    dp[r][c] = grid[r][c] + dp[r - 1][c]
                else:
                    dp[r][c] = grid[r][c] + min(dp[r - 1][c], dp[r][c - 1])
        return dp[-1][-1]
