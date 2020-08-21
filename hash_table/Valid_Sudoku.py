'''
link: https://leetcode.com/problems/valid-sudoku/

Determine if a 9x9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the 9 3x3 sub-boxes of the grid must contain the digits 1-9 without repetition.

A partially filled sudoku which is valid.

The Sudoku board could be partially filled, where empty cells are filled with the character '.'.
'''

from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_to_exist = defaultdict(list)
        col_to_exist = defaultdict(list)
        table_to_exist = defaultdict(list)
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.': continue
                table = i // 3  * 3 + j // 3 % 3
                if board[i][j] in row_to_exist[i] + col_to_exist[j] + table_to_exist[table]:
                   
                    return False
                row_to_exist[i].append(board[i][j])
                col_to_exist[j].append(board[i][j])
                table_to_exist[table].append(board[i][j])
        return True
        