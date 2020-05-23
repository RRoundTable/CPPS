'''
link: ßhttps://leetcode.com/problems/intersection-of-two-arrays/

Given two arrays, write a function to compute their intersection.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
Note:

Each element in the result must be unique.
The result can be in any order.
'''

from collections import defaultdict


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return set(nums1) & set(nums2)
        


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d, ans = defaultdict(int), []
        for ele in nums1:
            if d[ele] == 0: d[ele] += 1
        for ele in nums2:
            if d[ele] == 1:
                ans.append(ele); d[ele] += 1
        return ans
