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

        possible = defaultdict(lambda: [])

        total = set(str(i) for i in range(0, 10))
        for i in range(nrows):
            for j in range(ncols):
                if board[i][j] == ".":
                    matrix_idx = i // 3 + j // 3 * 3
                    t = total - row_dict[i]
                    possible[str(i) + str(j)] += list(
                        total - row_dict[i] - col_dict[j] - matrix_dict[matrix_idx]
                    )

    def get_possible(self, board, row_dict, col_dict, matrix_dict):
        possible = defaultdict(lambda: [])

        total = set(str(i) for i in range(0, 10))
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == ".":
                    matrix_idx = i // 3 + j // 3 * 3
                    t = total - row_dict[i]
                    ele = list(
                        total - row_dict[i] - col_dict[j] - matrix_dict[matrix_idx]
                    )
                    if not ele:
                        continue
                    possible[str(i) + str(j)] += ele
        return possible

