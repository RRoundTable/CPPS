"""
link: https://leetcode.com/problems/burst-balloons/

Given n balloons, indexed from 0 to n-1. Each balloon is painted with a number on it represented by array nums. You are asked to burst all the balloons. If the you burst balloon i you will get nums[left] * nums[i] * nums[right] coins. Here left and right are adjacent indices of i. After the burst, the left and right then becomes adjacent.

Find the maximum coins you can collect by bursting the balloons wisely.

Note:

You may imagine nums[-1] = nums[n] = 1. They are not real therefore you can not burst them.
0 ≤ n ≤ 500, 0 ≤ nums[i] ≤ 100
Example:

Input: [3,1,5,8]
Output: 167 
Explanation: nums = [3,1,5,8] --> [3,5,8] -->   [3,8]   -->  [8]  --> []
             coins =  3*1*5      +  3*5*8    +  1*3*8      + 1*8*1   = 167
"""


class Solution(object):
    def maxCoins(self, nums):4
        """O(N!)/O(N!)
        Backtracking
        :type nums: List[int]
        :rtype: int
        """

        self.ans = 0

        def backtracking(remain, idx, coins):
            if not remain:
                self.ans = max(self.ans, coins)
                return coins

            for i in range(len(remain)):
                if i < 1:
                    left = 1
                else:
                    left = remain[i - 1]
                if i >= len(remain) - 1:
                    right = 1
                else:
                    right = remain[i + 1]
                backtracking(
                    remain[:i] + remain[i + 1 :],
                    idx + 1,
                    coins + left * remain[i] * right,
                )

        backtracking(nums, 0, 0)
        return self.ans


class Solution(object):
    def maxCoins(self, nums):
        '''O(N ^ 3)/O(N ^ 2)'''
        nums = [1] + nums + [1]
        n = len(nums)
        dp = [[0] * len(nums) for _ in range(n)] # n * n [left, right\
        for k in range(2, n):
            for left in range(0, n - k):
                right = left + k
                for i in range(left+1, right):
                    dp[left][right] = max(dp[left][right],
                                         nums[left] * nums[i] * nums[right] + dp[left][i] + dp[i][right])
                    
        return dp[0][n - 1]
