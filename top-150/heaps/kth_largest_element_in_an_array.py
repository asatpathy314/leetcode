class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return sorted(nums)[-k]

"""
Above solution is the obvious one. But we can get theoretically faster than that.
This will always take at least n log n depending on the implementation of the sorting algorithm.
We can optimize this with a heap. 
"""

import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = [-num for num in nums]
        heapq.heapify(nums)
        for i in range(k - 1):
            heapq.heappop(nums)
        return -heapq.heappop(nums)

"""
The above solution runs in k log n time. We can turn this into n log k time by creating a heap of size at most k 
"""

import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for i in range(k):
            heapq.heappush(heap, nums[i])
        for num in nums[k:]:
            if num > heap[0]:
                heapq.heapreplace(heap, num)
        return heapq.heappop(heap)

"""
The general idea is if we maintain a heap of size k then we have at most log(k) time complexity for any heap operations which we perform at most n times. But
we can get even better than that by creating a median of medians solution that runs on average in n time and n^2 in the worst case
"""

import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        n = len(nums)
        def swap(i, j):
            nums[i], nums[j] = nums[j], nums[i]
        def solve_rec(l, r):
            m = l + (r - l) // 2
            while l < r:
                if nums[l] > nums[m]:
                    if nums[l]
            swap(m, l)
        solve_rec(0, n-1)
        print(nums)
