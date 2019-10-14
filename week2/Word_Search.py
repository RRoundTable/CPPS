"""
link: https://leetcode.com/problems/word-search/

Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

Example:

board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

Given word = "ABCCED", return true.
Given word = "SEE", return true.
Given word = "ABCB", return false.

"""

import copy
from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        """O(SMN)/O(S)"""
        nrows = len(board)
        ncols = len(board[0])

        def get_positive(x, y, used):
            results = []
            if x - 1 >= 0:
                results.append([x - 1, y])
            if x + 1 <= nrows - 1:
                results.append([x + 1, y])
            if y - 1 >= 0:
                results.append([x, y - 1])
            if y + 1 <= ncols - 1:
                results.append([x, y + 1])
            results = [r for r in results if r not in used]
            return results

        def generate(board, positive, word_idx, used):
            temp_used = used
            for x, y in positive:
                if board[x][y] == word[word_idx]:
                    if word_idx == len(word) - 1:
                        return True
                    temp_used = used + [[x, y]]
                    temp_positive = get_positive(x, y, temp_used)
                    if not positive:
                        return False
                    ans = generate(board, temp_positive, word_idx + 1, temp_used)
                    if ans:
                        return True

            return False

        if nrows * ncols < len(word):
            return False

        for i in range(nrows):
            for j in range(ncols):
                if board[i][j] != word[0]:
                    continue
                if len(word) == 1:
                    return True
                positive = get_positive(i, j, [[i, j]])
                ans = generate(board, positive, 1, [[i, j]])
                if ans:
                    return True

        return False

