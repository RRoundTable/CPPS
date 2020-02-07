'''
link: https://leetcode.com/problems/maximal-rectangle/
Given a 2D binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.

Example:

Input:
[
  ["1","0","1","0","0"],
  ["1","0","1","1","1"],
  ["1","1","1","1","1"],
  ["1","0","0","1","0"]
]
Output: 6
'''


from typing import List


from collections import defaultdict    
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        '''Brute-Force
        O(MNN)/O(MN)
        '''
        ans, d = 0, defaultdict(lambda: 0)
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] != '1': continue
                r, c, count = i, j, 0
                while r >= 0 and c >= 0:
                    if matrix[r][c] == "1": count += 1; c -= 1
                    else: break
                d[(i, j)] = count
                ans = max(ans, count)
                r, c = i, j
                while r >= 0 and c >= 0:
                    if matrix[r][c] == "1":
                        ans = max(min(d[(k, c)] for k in range(r, i+1)) * (i - r + 1), ans) 
                        r -= 1
                    else: break
        return ans
    
class Solution:
    def largestRectangleArea(self, heights):
        stack = [-1]
        heights.append(0)
        ans = 0
        for i in range(len(heights)):
            while heights[i] < heights[stack[-1]]:
                h = heights[stack.pop(-1)]
                w = i - stack[-1] - 1
                ans = max(ans, h * w)
            stack.append(i)
        heights.pop()
        return ans
    
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        '''
        O(NM)/O(M)
        '''
        ans = 0 # row, col, rectangle
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                matrix[i][j] = int(matrix[i][j])
                if matrix[i][j] and i - 1 >= 0:
                    matrix[i][j] = matrix[i-1][j] + 1 
            ans = max(ans, self.largestRectangleArea(matrix[i]))
        return ans