class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp_2 = 1
        dp_1 = 1
        temp = 0

        for i in range(2, n + 1):
            temp = dp_1
            dp_1 += dp_2
            dp_2 = temp

        return dp_1


"""
Very basic DP. Idea is that at any given stair other than the first, there are two ways to get there.

Two steps from two stairs down and one step from one stair down.
"""
