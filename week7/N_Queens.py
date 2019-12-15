'''
link: https://leetcode.com/problems/n-queens/
The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.



Given an integer n, return all distinct solutions to the n-queens puzzle.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space respectively.

Example:

Input: 4
Output: [
 [".Q..",  // Solution 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // Solution 2
  "Q...",
  "...Q",
  ".Q.."]
]
Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above.

'''


from collections import defaultdict
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        def get_possible(board, idx):
            rcol, rrow = [], []
            for i in range(n):
                if board[idx][i]: 
                    rrow.append(idx)
                    rcol.append(i)
            return rcol, rrow
        
        def make_ans(used):
            ans = ["." * n  for _ in range(n)]
            for r, c in used:
                temp = ""
                for i in range(n):
                    if i == c: temp += "Q"
                    else: temp += "."
                ans[r] = temp
            return ans
        
        def sub(board, c, r):
            change = []
            for i in range(n):
                if board[i][c]:
                    board[i][c] = False
                    change.append([i, c])
                if board[r][i]: 
                    board[r][i] = False
                    change.append([r, i])
            i, j = r, c
            while i >= 0 and i < n and j >= 0 and j < n:
                if board[i][j]:
                    board[i][j] = False
                    change.append([i, j])
                i -= 1
                j += 1
            i, j = r, c
            while i >= 0 and i < n and j >= 0 and j < n:
                if board[i][j]:
                    board[i][j] = False
                    change.append([i, j])
                i += 1
                j -= 1
            i, j = r, c
            while i >= 0 and i < n and j >= 0 and j < n:
                if board[i][j]:
                    board[i][j] = False
                    change.append([i, j])
                i -= 1
                j -= 1
            i, j = r, c
            while i >= 0 and i < n and j >= 0 and j < n:
                if board[i][j]:
                    board[i][j] = False
                    change.append([i, j])
                i += 1
                j += 1
            return board, change
        
        def restore(board, change):
            for r, c in change:
                board[r][c] = True
            return board
            
        def backtracking(board, used, idx=0):
            if len(used) == n:
                res = make_ans(used)
                ans.append(res)
                return
            rcol, rrow = get_possible(board, idx)
            for c, r in zip(rcol, rrow):
                tboard, change = sub(board, c, r)
                backtracking(tboard, used + [[c, r]], idx + 1)
                board = restore(board, change)
        ans, board = [], [[True] * n for _ in range(n)]
        backtracking(board, [], 0)
        return ans
        