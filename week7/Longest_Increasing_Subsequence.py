'''
link: https://leetcode.com/problems/longest-increasing-subsequence/
Given an unsorted array of integers, find the length of longest increasing subsequence.

Example:

Input: [10,9,2,5,3,7,101,18]
Output: 4 
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4. 
Note:

There may be more than one LIS combination, it is only necessary for you to return the length.
Your algorithm should run in O(n2) complexity.
Follow up: Could you improve it to O(n log n) time complexity?

'''
import sys
from collections import defaultdict
class Solution(object):
    def lengthOfLIS(self, nums):
        """Brute Force
        :type nums: List[int]
        :rtype: int
        """
        
        def recurssion(prev, length):
            if length == len(nums): return 0
            taken = 0
            if nums[length] > prev:
                taken = 1 + recurssion(nums[length], length + 1)
            notaken = recurssion(prev, length + 1)
            return max(taken, notaken)
        
        return recurssion(-sys.maxsize, 0)
        
class Solution(object):
    def lengthOfLIS(self, nums):
        """Recursion and Memorization
        :type nums: List[int]
        :rtype: int
        """
        def recurssion(prev, curr):
            if curr == len(nums): return 0
            if self.memo[prev][curr]:
                return self.memo[prev][curr]
            taken = 0
            if (nums[curr] > nums[prev]) or prev < 0:
                taken = 1 + recurssion(curr, curr + 1)
            notaken = recurssion(prev, curr + 1)
            self.memo[prev][curr] = max(taken, notaken)
            return self.memo[prev][curr]
        self.memo = [[0] * len(nums) for _ in range(len(nums))]
        return recurssion(-1, 0)


class Solution(object):
    def lengthOfLIS(self, nums):
        """DynamicPrograming
        :type nums: List[int]
        :rtype: int
        """
        dp = [1] * len(nums)
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j]: dp[i] = max(dp[i], dp[j] + 1)
        return len(nums) and max(dp)