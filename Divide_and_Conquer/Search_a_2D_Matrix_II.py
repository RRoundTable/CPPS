'''
link: https://leetcode.com/problems/search-a-2d-matrix-ii/
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.
Example:

Consider the following matrix:

[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
Given target = 5, return true.

Given target = 20, return false.
'''
class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix: return False
        n, m = len(matrix), len(matrix[0])
        row, col = n - 1, 0
        while row < n and row >= 0 and col < m and col >= 0:
            if matrix[row][col] > target:
                row -= 1
            elif matrix[row][col] < target:
                col += 1
            else:
                return True
        return False
    
    
class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix: return False
        n, m = len(matrix), len(matrix[0])
        
        def search(left, up, right, down):
            if left > right or up > down: return False       
            mid_h = (left + right) // 2
            mid_v = (up + down) // 2
            if matrix[mid_v][mid_h] < target:
                return search(left, mid_v + 1, right, down) or search(mid_h + 1, up, right, down)
            elif matrix[mid_v][mid_h] > target:
                return search(left, up, right, mid_v - 1) or search(left, up, mid_h - 1, down)
            else:
                return True

        return search(0, 0, len(matrix[0]) - 1, len(matrix) - 1)