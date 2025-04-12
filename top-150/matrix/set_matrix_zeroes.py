class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        rows = set()
        columns = set()

        # determine what rows and columns to set to zero
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    rows.add(i)
                    columns.add(j)

        # set matrix to zeroes
        for row in rows:
            for col in range(n):
                matrix[row][col] = 0

        for col in columns:
            for row in range(m):
                matrix[row][col] = 0


"""
Above solution is O(m + n) space, but I'm trying to think about a solution that can
run in constant space. The above is fairly obvious. Simply find the rows and columns that have
zeroes and keep track of them. Then modify the matrix in-place using the list.  1 
"""


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])

        def set_matrix(row, col):
            for r in range(m):
                if matrix[r][col] == 0:
                    continue
                matrix[r][col] = "0"

            for c in range(n):
                if matrix[row][c] == 0:
                    continue
                matrix[row][c] = "0"

        # determine what rows and columns to set to zero
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    set_matrix(i, j)

        for i in range(m):
            for j in range(n):
                matrix[i][j] = int(matrix[i][j])


"""
Unbelieveably slow but it uses constant space.  
"""


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        col_zero = None  # row zero and col zero occupy same space

        # determine what rows and columns to set to zero
        for i in range(m):
            if matrix[i][0] == 0:
                col_zero = 0
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[0][j] = matrix[i][0] = 0

        for j in range(1, n):
            if matrix[0][j] == 0:
                for i in range(m):
                    matrix[i][j] = 0

        for i in range(m):
            if matrix[i][0] == 0:
                for j in range(n):
                    matrix[i][j] = 0

        if col_zero == 0:
            for i in range(m):
                matrix[i][0] = 0


"""
Optimal soln I think. Constant space. Idea is instead of storing
the state in a separate array store the state in the matrix itself.
Set the beginning of the row to zero if it has a zero
and set the beginning of the column to zero if it has a zero
We need a separate var for column zero because they occupy the same space.
"""
