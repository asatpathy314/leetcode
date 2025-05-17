class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen_cache = defaultdict(lambda: -1)

        for i, num in enumerate(nums):
            seen_index = seen_cache[target - num]

            if seen_index > -1:
                return [seen_index, i]

            seen_cache[num] = i

        return []


"""
An alternate soln to two sum. 
"""
