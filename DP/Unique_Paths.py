'''
link: https://leetcode.com/problems/unique-paths/
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?


Above is a 7 x 3 grid. How many possible unique paths are there?

 

Example 1:

Input: m = 3, n = 2
Output: 3
Explanation:
From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Right -> Down
2. Right -> Down -> Right
3. Down -> Right -> Right
Example 2:

Input: m = 7, n = 3
Output: 28
 

Constraints:

1 <= m, n <= 100
It's guaranteed that the answer will be less than or equal to 2 * 10 ^ 9.
'''

class Solution:
    '''O(mn)/O(mn)'''
    def uniquePaths(self, m: int, n: int) -> int:
        d = [[1] * n for _ in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                d[i][j] = d[i-1][j] + d[i][j-1]
                
        return min(d[-1][-1], 2 * 10 ** 9)


class Solution:
    '''O(mn)/O(mn)'''
    def __init__(self):
        self.d = {}
        
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 1 or n == 1: return 1
        if self.d.get((m, n), False): return self.d[m, n]
        ans = self.uniquePaths(m - 1, n) + self.uniquePaths(m, n - 1)
        self.d[m, n] = ans
        return ans