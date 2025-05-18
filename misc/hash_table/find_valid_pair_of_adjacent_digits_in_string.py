class Solution:
    def findValidPair(self, s: str) -> str:
        count = [0 for _ in range(10)]
        nums = [int(c) for c in s]

        for num in nums:
            count[num] += 1

        qualified = set(num for i, num in enumerate(count) if num == i)

        for num1, num2 in zip(nums[0:-1], nums[1:]):
            if num1 in qualified and num2 in qualified:
                if num1 != num2:
                    return f"{num1}{num2}"

        return ""


"""
100% solution. Uses hashset + converting to an integer array.    
"""
