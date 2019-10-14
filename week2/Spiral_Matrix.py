"""
link: https://leetcode.com/problems/spiral-matrix/

Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

Example 1:

Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output: [1,2,3,6,9,8,7,4,5]
Example 2:

Input:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
"""

from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        """O(MN)/O(1)"""
        if not matrix:
            return []
        ans = []

        right = True
        down = True
        max_row = len(matrix)
        min_row = 0
        max_col = len(matrix[0])
        min_col = 0
        while len(ans) < len(matrix) * len(matrix[0]):

            if right and down:
                ans += matrix[min_row][min_col:max_col]
                min_row += 1
                right = False
                down = True

            elif not right and down:
                ans += [x[max_col - 1] for x in matrix[min_row:max_row]]
                max_col -= 1
                down = False
                right = False

            elif not right and not down:
                ans += matrix[max_row - 1][min_col:max_col][::-1]
                max_row -= 1
                down = False
                right = True
            elif right and not down:
                ans += [x[min_col] for x in matrix[min_row:max_row]][::-1]
                min_col += 1
                right = True
                down = True

        return ans

