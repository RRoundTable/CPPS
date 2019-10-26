"""
link: https://leetcode.com/problems/top-k-frequent-elements/

Given a non-empty array of integers, return the k most frequent elements.

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
Note:

You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
"""

from collections import defaultdict, Counter
from typing import List
from itertools import chain

class Solution:
    def topKFrequent1(self, nums: List[int], k: int) -> List[int]:

        d = defaultdict(lambda: 0)

        for i in range(len(nums)):
            d[nums[i]] += 1

        keys = d.keys()
        d1 = defaultdict(lambda: [])  # the number of elements
        for k_ in keys:
            d1[d[k_]].append(k_)

        d1 = sorted(d1.items(), key=lambda x: x[0], reverse=True)
        ans = []

        for i in range(k):
            ans += d1[i][1]
            if len(ans) >= k:
                break

        return ans[:k]

    def topKFrequent2(self, nums: List[int], k: int) -> List[int]:
        '''O(N)/O(N): bucket sort'''
        bucket =[[] for _ in range(len(nums))]
        for ele, count in Counter(nums).items():
            bucket[-count] += [ele]
        return list(chain.from_iterable(bucket))[:k]

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        '''O(NlogK)/O(N)'''
        heap = []
        for ele, count in Counter(nums).items():
            heapq.heappush(heap, (count, ele))
            if len(heap) > k:
                heapq.heappop(heap)
        return [h[1] for h in heap]

      