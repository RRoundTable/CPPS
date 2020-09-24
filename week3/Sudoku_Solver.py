"""
link: https://leetcode.com/problems/sudoku-solver/

Write a program to solve a Sudoku puzzle by filling the empty cells.

A sudoku solution must satisfy all of the following rules:

Each of the digits 1-9 must occur exactly once in each row.
Each of the digits 1-9 must occur exactly once in each column.
Each of the the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
Empty cells are indicated by the character '.'.


A sudoku puzzle...


...and its solution numbers marked in red.

Note:

The given board contain only digits 1-9 and the character '.'.
You may assume that the given Sudoku puzzle will have a single unique solution.
The given board size is always 9x9.
"""

from collections import defaultdict
import copy
from typing import List


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        '''O(1)/O(1)'''
        """
        Do not return anything, modify board in-place instead.
        """
        row_dict = defaultdict(lambda: set())
        col_dict = defaultdict(lambda: set())
        matrix_dict = defaultdict(lambda: set())
        nrows = len(board)
        ncols = len(board[0])
        for i in range(nrows):
            for j in range(ncols):
                if board[i][j] == ".":
                    continue
                row_dict[i].add(board[i][j])
                col_dict[j].add(board[i][j])
                matrix_idx = i // 3 + j // 3 * 3
                matrix_dict[matrix_idx].add(board[i][j])

        possible = self.get_possible(board, row_dict, col_dict, matrix_dict)

        def undo(board, row_dict, col_dict, matrix_dict, key, ele):
            i, j = int(key[0]), int(key[1])
            row_dict[i].remove(ele)
            col_dict[j].remove(ele)
            matrix_idx = i // 3 + j // 3 * 3
            matrix_dict[matrix_idx].remove(ele)
            board[i][j] = "."

        def simulator(row_dict, col_dict, matrix_dict):
            possible = self.get_possible(board, row_dict, col_dict, matrix_dict)
            if len(possible.keys()) == 0:
                if self.check_board(board):
                    return True
                else:
                    return False
            k = list(possible.keys())[0]
            for ele in possible[k]:
                i, j = int(k[0]), int(k[1])
                matrix_idx = i // 3 + j // 3 * 3
                row_dict[i].add(ele)
                col_dict[j].add(ele)
                matrix_dict[matrix_idx].add(ele)
                board[i][j] = ele
                complete = simulator(row_dict, col_dict, matrix_dict)
                if complete:
                    return complete
                else:
                    undo(board, row_dict, col_dict, matrix_dict, k, ele)

        simulator(row_dict, col_dict, matrix_dict)

    def check_board(self, board):
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == ".":
                    return False
        return True

    def get_possible(self, board, row_dict, col_dict, matrix_dict):
        possible = defaultdict(lambda: [])
        total = set(str(i) for i in range(1, 10))
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == ".":
                    matrix_idx = i // 3 + j // 3 * 3
                    ele = list(
                        total - (row_dict[i] | col_dict[j] | matrix_dict[matrix_idx])
                    )
                    if not ele:
                        return possible
                    possible[str(i) + str(j)] += ele
                    return possible
        return possible


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        row, col, table = defaultdict(set), defaultdict(set), defaultdict(set)
        empty = 0
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.': empty +=1; continue
                row[i].add(board[i][j])
                col[j].add(board[i][j])
                table[i//3*3+j//3].add(board[i][j])
                
        def undo(i, j, v):
            nonlocal board, row, col, table
            board[i][j] = "."
            row[i].remove(v); col[j].remove(v); table[i // 3 * 3 + j // 3].remove(v)
            
        def solve(idx, empty):
            nonlocal board, row, col, table
            if idx == 81:
                return empty == 0
            i, j = idx // 9, idx % 9
            if board[i][j] == ".":
                for v in {"1", "2", "3", "4", "5", "6", "7", "8", "9"} - (row[i] | col[j] | table[i // 3 * 3 + j // 3]):
                    board[i][j] = v
                    row[i].add(v); col[j].add(v); table[i // 3 * 3 + j // 3].add(v)
                    if solve(idx + 1, empty - 1): return True
                    undo(i, j, v)
            else:
                if solve(idx + 1, empty): return True
            return False

        solve(0, empty)