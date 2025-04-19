class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        for i in range(n):
            for j in range(n):
                if i != j and nums[i] + nums[j] == target:
                    return [i, j] if i < j else [j, i]
        return []


"""
Brute force O(n^2)
"""


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prev = dict()
        for i, num in enumerate(nums):
            if target - num in prev:
                return [prev[target - num], i]
            prev[num] = i
        return []


"""
One pass hash-map O(n)
"""


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums = [(num, i) for i, num in enumerate(nums)]
        nums.sort()

        l = 0
        r = len(nums) - 1

        while l < r:
            if nums[l][0] + nums[r][0] == target:
                return sorted([nums[l][1], nums[r][1]])
            elif nums[l][0] + nums[r][0] < target:
                l += 1
            else:
                r -= 1

        return []


"""
Sorting solution (O(n log n)) 
"""
