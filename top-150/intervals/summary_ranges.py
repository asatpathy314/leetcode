class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ranges = []
        n = len(nums)
        l = 0
        r = 1

        while r < len(nums):
            if nums[r] - nums[r - 1] != 1:
                range_arr = f"{nums[l]}" if r - 1 == l else f"{nums[l]}->{nums[r - 1]}"
                ranges.append(range_arr)
                l = r
            r += 1

        if nums:
            ranges.append(f"{nums[l]}" if r - 1 == l else f"{nums[l]}->{nums[r - 1]}")

        return ranges


"""
Just getting the daily leetcode in. This one was pretty chill, just go through
and if the current num is more than 1 more than the previous add the currently tracked range.
Then at the end add any remaining range if nums array is greater than one. The memory is BS on this
one though... 
"""
