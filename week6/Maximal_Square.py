"""
link: https://leetcode.com/problems/maximal-square/
Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

Example:

Input: 

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0

Output: 4
"""


class Solution(object):
    def maximalSquare(self, matrix):
        """O(MN)/O(MN)
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix:
            return 0
        ans = 0
        dp = []

        nrows = len(matrix)
        ncols = len(matrix[0])

        for i in range(nrows):
            for j in range(ncols):
                if matrix[i][j] == "0":
                    continue
                ans = max(1, ans)
                maxval = (nrows - i) * (ncols - j)
                if maxval <= ans:
                    break
                w, h, p = [[i, j]], [[i, j]], [i, j]
                temp_w, temp_h = [], []
                Done = False
                while not Done:
                    for ele1, ele2 in zip(w, h):
                        if ele1[0] + 1 >= nrows or ele2[1] + 1 >= ncols:
                            Done = True
                            break
                        if (
                            matrix[ele1[0] + 1][ele1[1]] != "1"
                            or matrix[ele2[0]][ele2[1] + 1] != "1"
                        ):
                            Done = True
                            break
                        temp_w.append([ele1[0] + 1, ele1[1]])
                        temp_h.append([ele2[0], ele2[1] + 1])
                    else:
                        if matrix[p[0] + 1][p[1] + 1] == "1":
                            p = [p[0] + 1, p[1] + 1]
                            w, h = temp_w + [p], temp_h + [p]
                            ans = max(ans, (p[0] - i + 1) * (p[1] - j + 1))
                        else:
                            Done = True
        return ans


class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                matrix[i][j] = int(matrix[i][j])
                if (i and j) and matrix[i][j]:
                    matrix[i][j] = (
                        min(matrix[i - 1][j], matrix[i][j - 1], matrix[i - 1][j - 1])
                        + 1
                    )
        return len(matrix) and max(map(max, matrix)) ** 2
