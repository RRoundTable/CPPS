'''
link: https://leetcode.com/problems/matrix-block-sum/

Given a m * n matrix mat and an integer K, return a matrix answer where each answer[i][j] is the sum of all elements mat[r][c] for i - K <= r <= i + K, j - K <= c <= j + K, and (r, c) is a valid position in the matrix.
 

Example 1:

Input: mat = [[1,2,3],[4,5,6],[7,8,9]], K = 1
Output: [[12,21,16],[27,45,33],[24,39,28]]
Example 2:

Input: mat = [[1,2,3],[4,5,6],[7,8,9]], K = 2
Output: [[45,45,45],[45,45,45],[45,45,45]]
 

Constraints:

m == mat.length
n == mat[i].length
1 <= m, n, K <= 100
1 <= mat[i][j] <= 100
'''

class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        n, m, ans = len(mat), len(mat[0]), [[0] * m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if i == 0:
                    mat[i][j] += mat[i][j-1] if j - 1 >= 0 else 0; continue
                if j == 0:
                    mat[i][j] += mat[i-1][j] if i - 1 >= 0 else 0; continue
                mat[i][j] += mat[i][j-1] + mat[i-1][j] - mat[i-1][j-1]
        for i in range(n):
            for j in range(m):
                total = mat[min(n-1, i+k)][min(m-1, j+k)]
                left = mat[min(n-1, i+k)][j-k-1] if j - k - 1 >= 0 else 0
                up = mat[i - k - 1][min(m-1, j+k)] if i - k - 1 >= 0 else 0
                interpolate = mat[i-k-1][j-k-1] if i - k - 1 >= 0 and j - k - 1 >= 0 else 0
                ans[i][j] = total - left - up + interpolate
        return ans
        