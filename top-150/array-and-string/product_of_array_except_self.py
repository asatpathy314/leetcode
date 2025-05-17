class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre_computed_products = dict()
        start = 0
        end = len(nums) - 1

        # calculate prefixes
        pre_computed_products[(0, 0)] = nums[0]
        for i in range(1, end + 1):
            pre_computed_products[(0, i)] = pre_computed_products[(0, i - 1)] * nums[i]

        # calculate suffixes
        pre_computed_products[(end, end)] = nums[end]
        for i in range(end - 1, 0, -1):
            pre_computed_products[(i, end)] = (
                nums[i] * pre_computed_products[(i + 1, end)]
            )

        for i, num in enumerate(nums):
            nums[i] = pre_computed_products.get(
                (0, i - 1), 1
            ) * pre_computed_products.get((i + 1, end), 1)

        return nums


"""
Pretty chill. Comments explain.
"""


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = [0] * n
        product = 1

        # calculate prefixes
        for i, num in enumerate(nums):
            output[i] = product
            product *= num

        # combine with suffixes
        product = 1
        for i in range(n - 1, -1, -1):
            output[i] *= product
            product *= nums[i]

        return output


"""
A more efficient solution that stores the prefixes and just uses a running value of the suffix and combines it with the stored prefixes instead of storing prefixes and suffixes in separate arrays. 
"""
