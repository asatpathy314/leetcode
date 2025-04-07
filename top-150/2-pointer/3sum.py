class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        soln = []

        for i in range(0, len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l = i + 1
            r = len(nums) - 1
            while l < r:
                if l > i + 1 and nums[l] == nums[l - 1]:
                    l += 1
                    continue
                s = nums[i] + nums[l] + nums[r]
                if s == 0:
                    soln.append([nums[i], nums[l], nums[r]])
                if s > 0:
                    r -= 1
                else:
                    l += 1

        return soln


"""
Hold the left most pointer to be fixed and then consider all possible pairs as follows
(l, [l2, r2), (l2, r2]) depending on feasibility. We determine feasibility by checking whether
the sum is below or above the target and subtracting from the right hand side if its greater
and vice versa. This works because sorted the nums array. A more optimal solution is as
follows. It does better because it has less conditional checks overall.
"""


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            j = i + 1
            k = len(nums) - 1

            while j < k:
                total = nums[i] + nums[j] + nums[k]

                if total > 0:
                    k -= 1
                elif total < 0:
                    j += 1
                else:
                    res.append([nums[i], nums[j], nums[k]])
                    j += 1

                    while nums[j] == nums[j - 1] and j < k:
                        j += 1

        return res
