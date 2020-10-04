'''
link: https://leetcode.com/problems/01-matrix/
Given a matrix consists of 0 and 1, find the distance of the nearest 0 for each cell.

The distance between two adjacent cells is 1.

 

Example 1:

Input:
[[0,0,0],
 [0,1,0],
 [0,0,0]]

Output:
[[0,0,0],
 [0,1,0],
 [0,0,0]]
Example 2:

Input:
[[0,0,0],
 [0,1,0],
 [1,1,1]]

Output:
[[0,0,0],
 [0,1,0],
 [1,2,1]]
 

Note:

The number of elements of the given matrix will not exceed 10,000.
There are at least one 0 in the given matrix.
The cells are adjacent in only four directions: up, down, left and right.
'''
from collections import deque


class Solution:
    '''O(N^2)/O(N)'''
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        r, c = len(matrix), len(matrix[0])
        dire = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        dist = [[None] * len(matrix[0]) for _ in range(len(matrix))]
        queue, seen = deque([]), set()
        for i in range(r):
            for j in range(c):
                if matrix[i][j] == 0:
                    dist[i][j] = 0
                    queue.append((i, j, 0))
        while queue:
            i, j, d = queue.popleft()
            if matrix[i][j] != 0: dist[i][j] = min(dist[i][j] if dist[i][j] else float('inf'), d)
            if (i, j) in seen: continue
            seen.add((i, j))
            for di, dj in dire:
                if i + di >= 0 and i + di < r and j + dj >= 0 and j + dj < c:
                    queue.append((i + di, j + dj, d + 1))
        return dist
    
    
class Solution:
    '''O(N)/O(N)'''
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        r, c = len(matrix), len(matrix[0])
        dire = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        dist = [[None] * len(matrix[0]) for _ in range(len(matrix))]
        queue, seen = deque([]), set()
        for i in range(r):
            for j in range(c):
                if matrix[i][j] == 0:
                    dist[i][j] = 0
                    queue.append((i, j, 0))
        while queue:
            i, j, d = queue.popleft()
            if matrix[i][j] != 0: dist[i][j] = min(dist[i][j] if dist[i][j] else float('inf'), d)
            if (i, j) in seen: continue
            seen.add((i, j))
            for di, dj in dire:
                if i + di >= 0 and i + di < r and j + dj >= 0 and j + dj < c:
                    queue.append((i + di, j + dj, d + 1))
        return dist
    

class Solution:
    '''O(N)/O(N)'''
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        r, c = len(matrix), len(matrix[0])
        dist = [[float('inf')] * len(matrix[0]) for _ in range(len(matrix))]
        for i in range(r):
            for j in range(c):
                if matrix[i][j] == 0:
                    dist[i][j] = 0
        
        for i in range(r):
            for j in range(c):
                dist[i][j] = min(dist[i][j], dist[i-1][j] + 1 if i - 1 >= 0 else float('inf'), dist[i][j-1] + 1 if j - 1 >= 0 else float('inf'))
        
        for i in range(r - 1, -1, -1):
            for j in range(c - 1, -1, -1):
                dist[i][j] = min(dist[i][j], dist[i+1][j] + 1 if i + 1 < r else float('inf'), dist[i][j+1] + 1 if j + 1 < c else float('inf'))
                
        return dist
    

        