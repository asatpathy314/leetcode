LIVE = 1
DEAD = 0


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])

        live_board = self.get_num_live_neighbors(board, m, n)

        for i in range(m):
            for j in range(n):
                if board[i][j] == LIVE:
                    if live_board[i][j] < 2 or live_board[i][j] > 3:
                        board[i][j] = DEAD
                    elif live_board[i][j] < 4:
                        board[i][j] = LIVE
                elif live_board[i][j] == 3:
                    board[i][j] = LIVE

    def get_num_live_neighbors(self, board: List[List[int]], m: int, n: int):
        neighbor_board = [[0 for _ in range(n)] for _ in range(m)]

        for i, row in enumerate(board):
            for j, cell in enumerate(row):
                if cell == LIVE:
                    for x, y in self.get_neighbors(i, j, m, n):
                        neighbor_board[x][y] += 1

        return neighbor_board

    def get_neighbors(self, i: int, j: int, m: int, n: int):
        neighbors = []
        possible_points = [
            (i - 1, j - 1),
            (i - 1, j),
            (i, j - 1),
            (i + 1, j),
            (i, j + 1),
            (i + 1, j + 1),
            (i + 1, j - 1),
            (i - 1, j + 1),
        ]
        for x, y in possible_points:
            if x > -1 and x < m and y > -1 and y < n:
                neighbors.append((x, y))
        return neighbors
