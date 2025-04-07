class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0 for _ in range(n)]

        if len(nums) == 1:
            return nums[0]

        if len(nums) == 2:
            return max(nums[0], nums[1])

        dp[0] = nums[0]
        dp[1] = nums[1]
        dp[2] = max(nums[0] + nums[2], nums[1])

        for h in range(3, n):
            dp[h] = nums[h] + max(dp[h - 2], dp[h - 3])

        return max(dp[n - 1], dp[n - 2])


"""
The idea behind this is that we need to consider two houses back
and three houses back respectively. We don't consider the house immediately
behind the current because both houses can't be robbed. (no robbing adjacent houses)
The rest is pretty simple.
"""
