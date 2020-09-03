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

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n, m = len(board), len(board[0])
        
        def get_neighbor(i, j):
            nonlocal n, m
            nei = [(i, j)]
            if i - 1 >= 0: nei.append((i - 1, j))
            if j - 1 >= 0: nei.append((i, j - 1))
            if i + 1 < n: nei.append((i + 1, j))
            if j + 1 < m: nei.append((i, j + 1))
            return nei
            
        def backtrack(i, j, word_idx):
            nonlocal board, word
            if word_idx == len(word): return True
            if board[i][j] == -1: return False
            if board[i][j] == word[word_idx]:
                temp = board[i][j]
                board[i][j] = -1
                for ni, nj in get_neighbor(i, j):
                    if backtrack(ni, nj, word_idx + 1):
                        return True
                board[i][j] = temp
        
        for i in range(n):
            for j in range(m):
                if backtrack(i, j, 0): return True
                
                
        return False
