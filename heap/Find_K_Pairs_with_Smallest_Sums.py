'''
link: https://leetcode.com/problems/find-k-pairs-with-smallest-sums/
You are given two integer arrays nums1 and nums2 sorted in ascending order and an integer k.

Define a pair (u,v) which consists of one element from the first array and one element from the second array.

Find the k pairs (u1,v1),(u2,v2) ...(uk,vk) with the smallest sums.

Example 1:

Input: nums1 = [1,7,11], nums2 = [2,4,6], k = 3
Output: [[1,2],[1,4],[1,6]] 
Explanation: The first 3 pairs are returned from the sequence: 
             [1,2],[1,4],[1,6],[7,2],[7,4],[11,2],[7,6],[11,4],[11,6]
Example 2:

Input: nums1 = [1,1,2], nums2 = [1,2,3], k = 2
Output: [1,1],[1,1]
Explanation: The first 2 pairs are returned from the sequence: 
             [1,1],[1,1],[1,2],[2,1],[1,2],[2,2],[1,3],[1,3],[2,3]
Example 3:

Input: nums1 = [1,2], nums2 = [3], k = 3
Output: [1,3],[2,3]
Explanation: All possible pairs are returned from the sequence: [1,3],[2,3]
'''
from heapq import heappop, heappush, nsmallest, heapify


class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        heap = []
        for n1 in nums1:
            for n2 in nums2:
                heappush(heap, [n1 + n2, n1, n2])
        return [ele[1:] for ele in nsmallest(k, heap)]


class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        if not nums1 or not nums2: return []
        res, heap = [], [[nums1[i] + nums2[0], i, 0] for i in range(len(nums1))]
        heapify(heap)
        while heap and len(res) < k:
            s, n1, n2 = heappop(heap)
            if n2 < len(nums2):
                res.append([nums1[n1], nums2[n2]])
            if n2 + 1 < len(nums2):
                heappush(heap, [nums1[n1] + nums2[n2+1], n1, n2 + 1])
        return res