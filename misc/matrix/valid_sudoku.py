class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        counts = [set() for _ in range(9)]

        # iterate through rows
        for r, row in enumerate(board):
            for elem in row:
                if elem != "." and elem in counts[r]:
                    return False
                counts[r].add(elem)

        # iterate through cols
        counts = [set() for _ in range(9)]
        for c in range(9):
            for r in range(9):
                if board[r][c] == ".":
                    continue
                if board[r][c] in counts[c]:
                    return False
                counts[c].add(board[r][c])

        # iterate through boxes
        counts = [set() for _ in range(9)]
        for b in range(9):
            for r in range(3):
                for c in range(3):
                    row = ((b // 3) * 3) + r
                    col = ((b % 3) * 3) + c
                    if board[row][col] == ".":
                        continue
                    if board[row][col] in counts[b]:
                        print(b, row, col, counts[b])
                        return False
                    counts[b].add(board[row][col])

        return True
