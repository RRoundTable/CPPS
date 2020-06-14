'''
link: https://leetcode.com/problems/rotting-oranges/

In a given grid, each cell can have one of three values:

the value 0 representing an empty cell;
the value 1 representing a fresh orange;
the value 2 representing a rotten orange.
Every minute, any fresh orange that is adjacent (4-directionally) to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange.  If this is impossible, return -1 instead.

 

Example 1:



Input: [[2,1,1],[1,1,0],[0,1,1]]
Output: 4
Example 2:

Input: [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation:  The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.
Example 3:

Input: [[0,2]]
Output: 0
Explanation:  Since there are already no fresh oranges at minute 0, the answer is just 0.
 

Note:

1 <= grid.length <= 10
1 <= grid[0].length <= 10
grid[i][j] is only 0, 1, or 2.
'''

from collections import deque

class Solution:
    '''
    BFS
    O(N)/O(N)ß
    '''
    def orangesRotting(self, grid: List[List[int]]) -> int:
        que, fresh, visited, time = deque([]), set(), set(), 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2: que.append((i, j))
                if grid[i][j] == 1: fresh.add((i,j))
        
        while que and fresh:
            size = len(que)
            while size:
                i, j = que.popleft(); size -= 1
                if (i, j) not in visited:
                    visited.add((i, j))
                    for ni, nj in [(i-1, j), (i+1, j), (i, j -1), (i, j + 1)]:
                        if ni < 0 or ni >= len(grid) or nj < 0 or nj >= len(grid[0]): continue
                        if grid[ni][nj] == 1:
                            que.append((ni, nj)); grid[ni][nj] = 2
                            fresh.remove((ni, nj))
            time += 1
                
        return time if not fresh else -1
        