from collections import Counter


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        freq = [[] for _ in range(len(nums) + 1)]
        res = []

        for num, cnt in c.items():
            freq[cnt].append(num)

        for i in range(len(freq) - 1, -1, -1):
            for num in freq[i]:
                res.append(num)

        return res[0:k]


"""
Bucket sort that uses at most O(n) space and O(n) time complexity. Only works because n is small. 
"""
