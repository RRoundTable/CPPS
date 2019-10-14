"""
link: https://leetcode.com/problems/first-missing-positive/
Given an unsorted integer array, find the smallest missing positive integer.

Example 1:

Input: [1,2,0]
Output: 3
Example 2:

Input: [3,4,-1,1]
Output: 2
Example 3:

Input: [7,8,9,11,12]
Output: 1
Note:

Your algorithm should run in O(n) time and uses constant extra space.
"""

from collections import defaultdict
from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        '''O(N)/O(S)'''
        i = 0
        nums = list(set(nums))
        total_sum = 0
        nums = [n for n in nums if n > 0]

        if not nums:
            return 1

        max_val = max(nums)
        min_val = min(nums)

        total_sum = 0

        if min_val > 1:
            return 1

        expected = (max_val + 1) * max_val / 2

        check = defaultdict(lambda: 0)
        for i in range(len(nums)):
            check[nums[i]] += 1
            total_sum += nums[i]

        diff = int(expected - total_sum)
        if diff == 0:
            return max_val + 1

        for i in range(2, max_val):
            if check[i] == 0:
                return i
