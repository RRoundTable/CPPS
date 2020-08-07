'''
link: https://leetcode.com/problems/trapping-rain-water-ii/

Given an m x n matrix of positive integers representing the height of each unit cell in a 2D elevation map, compute the volume of water it is able to trap after raining.

Example:

Given the following 3x6 height map:
[
  [1,4,3,1,3,2],
  [3,2,1,3,2,4],
  [2,3,3,2,3,1]
]

Return 4.
'''
from collections import deque
from heapq import heappop, heappush, heapify

class Solution:
    def trapRainWater(self, grid: List[List[int]]) -> int:
            
        def min_surrounding_height(i, j):
            nonlocal grid
            left = grid[i][j-1] if (grid[i][j-1] != grid[i][j] or j - 1 == 0) else float('inf')
            right = grid[i][j+1] if (grid[i][j+1] != grid[i][j] or j + 1 == len(grid[0]) - 1) else float('inf')
            up = grid[i-1][j] if (grid[i-1][j] != grid[i][j] or i - 1 == 0) else float('inf')
            down = grid[i+1][j] if (grid[i+1][j] != grid[i][j] or i + 1 == len(grid) - 1) else float('inf')
        
            return min([left, right, up, down])
            
        
        heap, ans = [], 0
        for i in range(1, len(grid) - 1):
            for j in range(1, len(grid[0]) - 1):
                heappush(heap, (grid[i][j], i, j))
        
        while heap:
            lowest = heappop(heap)
            queue = deque([lowest])
            visited = set()
            upto = float('inf')
            
            while queue:
                h, i, j = queue.popleft()
                if (i, j) in visited: continue
                visited.add((i, j))
                upto = min(upto, min_surrounding_height(i, j))
                temp = []
                while heap and heap[0][0] == h:
                    h, ni, nj = heappop(heap)
                    if (ni, nj) in [(i, j + 1), (i, j - 1), (i + 1, j), (i - 1, j)]:
                        queue.append((h, ni, nj))
                    else:
                        temp.append((h, ni, nj))
                for t in temp:
                    heappush(heap, t)
                        
            
            for i, j in visited:
                if upto - grid[i][j] > 0:
                    ans += upto - grid[i][j]
                    grid[i][j] = upto
                    heappush(heap, (upto, i, j))
          
        return ans

class Solution:
    def trapRainWater(self, grid: List[List[int]]) -> int:  
        heap, ans = [], 0
        visited = [[False] * len(grid[0]) for _ in range(len(grid))]
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i == 0 or i == len(grid) - 1 or j == 0 or j == len(grid[0]) - 1:
                    visited[i][j] = True 
                    heappush(heap, (grid[i][j], i, j))
       
        while heap:
            h, i, j = heappop(heap)
            for ni, nj in [(i + 1, j), (i - 1, j), (i, j - 1), (i, j + 1)]:
                if ((ni >= 0 and ni < len(grid)) and (nj >= 0 and nj < len(grid[0]))) and not visited[ni][nj]:
                    ans += max(0, h - grid[ni][nj])
                    heappush(heap, (max(h, grid[ni][nj]), ni, nj))
                    visited[ni][nj] = True
                    
        return ans