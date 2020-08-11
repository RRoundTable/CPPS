'''
link: https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/

Given a n x n matrix where each of the rows and columns are sorted in ascending order, find the kth smallest element in the matrix.

Note that it is the kth smallest element in the sorted order, not the kth distinct element.

Example:

matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
],
k = 8,

return 13.
Note:
You may assume k is always valid, 1 ≤ k ≤ n2.
'''

class Solution:
    '''
    Binary Search
    O(N)/O(1)
    '''
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        lo, hi = matrix[0][0], matrix[-1][-1]
        while lo < hi:
            mid = lo + (hi - lo) / 2
            count, smaller, larger = self.countLessEqual(matrix, mid, matrix[0][0], matrix[-1][-1])
            if count == k: return smaller
            if count < k: lo = larger
            if count > k: hi = smaller
        return lo
        
    
    def countLessEqual(self, matrix, mid, smaller, larger):
        count, n = 0, len(matrix)
        row, col = n - 1, 0
        while row >= 0 and col < n:
            if matrix[row][col] > mid:
                larger = min(larger, matrix[row][col])
                row -= 1
            else:
                smaller = max(smaller, matrix[row][col])
                count += row + 1
                col += 1
        return count, smaller, larger

class Solution:
    '''O(MlogN)/O(N)'''
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        m, n = len(matrix), len(matrix[0])
        flatten = []
        for i in range(m):
            for j in range(n):
                flatten.append(matrix[i][j])
        return sorted(flatten)[k-1]
    
from heapq import heappop, heappush, heapify
class Solution:
    '''heap
    O(KlogN)/O(NM)'''
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        m = len(matrix)
        q, r = divmod(k, m)
        flatten = []
        
        indexes = [(i, 0) for i in range(m)]
        
        heap = [(matrix[i][0], i, 0) for i in range(m)]
        
        heapify(heap)
        count = 0
        while count <= k:
            val, i, j = heappop(heap)
            count += 1
            if count == k: return val
            if j + 1 < m:
                heappush(heap, (matrix[i][j+1], i, j + 1))