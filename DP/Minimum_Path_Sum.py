'''
link: https://leetcode.com/problems/minimum-path-sum/
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Example:

Input:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
Output: 7
Explanation: Because the path 1→3→1→1→1 minimizes the sum.
'''


class Solution:
    '''O(MN)/O(1)'''
    def minPathSum(self, grid: List[List[int]]) -> int:
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i == 0 and j == 0: continue
                up = grid[i-1][j] if i - 1 >= 0 else float('inf')
                left = grid[i][j-1] if j - 1 >= 0 else float('inf')
                grid[i][j] += min(up, left)
        return grid[-1][-1]