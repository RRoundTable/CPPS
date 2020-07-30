"""
link: https://leetcode.com/explore/learn/card/queue-stack/231/practical-application-queue/1374/
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input:
11110
11010
11000
00000

Output: 1
Example 2:

Input:
11000
11000
00100
00011

Output: 3
"""

from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        queue, visited, ans = deque(), set(), 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i, j) not in visited and grid[i][j] == '1':
                    queue.append((i, j)); ans += 1 
                while queue:
                    x, y = queue.popleft()
                    if (x, y) in visited or grid[x][y] == '0': continue
                    visited.add((x, y))
                    for ni, nj in [(x, y - 1), (x, y + 1), (x + 1, y), (x - 1, y)]:
                        if (ni >= 0 and ni < len(grid)) and (nj >= 0 and nj < len(grid[0])):
                            queue.append((ni, nj))
        return ans
    