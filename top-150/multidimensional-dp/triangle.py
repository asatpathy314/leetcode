class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        for row in range(len(triangle) - 2, -1, -1):
            for i, item in enumerate(triangle[row]):
                triangle[row][i] += min(triangle[row + 1][i], triangle[row + 1][i + 1])

        return triangle[0][0]


"""
The basic idea for this solution is that we can backtrack and create an optimal path. The shortest path from the bottom
to the top is the same as the shortest path from the top to the bottom. From any ending square you can traverse to at most two squares in the row above. The same is true
in the opposite. By that principle we can determine an absolute minimum path from anything between the end row and the second to last row and then recurse. In this case
we used a tabular soln though
"""
