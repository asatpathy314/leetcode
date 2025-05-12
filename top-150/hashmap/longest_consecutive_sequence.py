class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        nums = set(nums)
        lcs_dp = defaultdict(int)

        def traverse_rec(num, length):
            if num not in nums:
                return length
            if lcs_dp[num] > 0:
                return length + lcs_dp[num]
            return traverse_rec(num - 1, length + 1)

        lcs = []

        for num in nums:
            lcs_dp[num] = traverse_rec(num - 1, 1)

        return max(lcs_dp.values())


"""
Use the fact that the longest sequence ending at n is the same length at the longest sequence ending at (n-1) and then you add 1. This lets us memoize and use a recursive soln in O(n) time. 
"""


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        lcs = 0
        nums = set(nums)

        for num in nums:
            l = 1

            if num - 1 in nums:
                continue

            while (num + l) in nums:
                l += 1

            lcs = max(lcs, l)

        return lcs


"""
More efficient soln. 
"""
