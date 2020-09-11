'''
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
'''

class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        n = len(nums)
        
        memo = [[None] * n for _ in range(n)]
        for i in range(n):
            memo[i][i] = nums[i]
        
        def backtrack(i, j):
            nonlocal memo, n, nums
            if i + 1 == j: return 0
            if memo[i][j] is not None: return memo[i][j]
            memo[i][j] = 0
            for k in range(i + 1, j):
                k_earn = nums[i] * nums[k] * nums[j] + backtrack(i, k) + backtrack(k, j)
                memo[i][j] = max(memo[i][j], k_earn)
            return memo[i][j]
        
        return backtrack(0, n - 1)