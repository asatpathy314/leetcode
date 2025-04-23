class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        max_water = 0

        l = 0
        r = n - 1

        while l < r:
            max_water = max(max_water, (r - l) * min(height[l], height[r]))
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return max_water


"""
Review why this is inequivocably true. 
"""
