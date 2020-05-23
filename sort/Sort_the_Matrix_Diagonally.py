'''
link: https://leetcode.com/problems/sort-the-matrix-diagonally/

Given a m * n matrix mat of integers, sort it diagonally in ascending order from the top-left to the bottom-right then return the sorted array.

 

Example 1:


Input: mat = [[3,3,1,1],[2,2,1,2],[1,1,1,2]]
Output: [[1,1,1,1],[1,2,2,2],[1,2,3,3]]
 

Constraints:

m == mat.length
n == mat[i].length
1 <= m, n <= 100
1 <= mat[i][j] <= 100
'''

class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        
        m, n = len(mat), len(mat[0])
        point = [(i, 0) for i in range(m)] + [(0, i) for i in range(1, n)]
        
        for i, j in point:
            ti, tj, k, temp = i, j, 0, []
            while ti < m and tj < n:
                temp.append(mat[ti][tj])
                ti, tj = ti + 1, tj + 1
            temp.sort()
            while i < m and j < n:
                mat[i][j] = temp[k]
                i, j, k = i + 1, j + 1, k + 1
        return mat
                
                