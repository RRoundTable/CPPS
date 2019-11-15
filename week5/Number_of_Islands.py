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


class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0

        nrows = len(grid)
        ncols = len(grid[0])
        ans = 0

        def possible(point, used=[]):
            x, y = point
            p = []
            if x - 1 >= 0:
                p.append([x - 1, y])
            if x + 1 < nrows:
                p.append([x + 1, y])
            if y - 1 >= 0:
                p.append([x, y - 1])
            if y + 1 < ncols:
                p.append([x, y + 1])

            return p

        def bfs(x, y):
            queue, used = [[x, y]], []
            while queue:
                pop = queue.pop(0)
                if pop in used:
                    continue
                used.append(pop)
                grid[pop[0]][pop[1]] = 0
                for x, y in possible(pop):
                    if grid[x][y] == "1":
                        queue.append([x, y])

        for i in range(nrows):
            for j in range(ncols):
                if grid[i][j] == "1":
                    bfs(i, j)
                    ans += 1
        return ans

