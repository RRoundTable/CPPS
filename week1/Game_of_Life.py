
'''
link: https://leetcode.com/problems/game-of-life/

According to the Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

Given a board with m by n cells, each cell has an initial state live (1) or dead (0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

Any live cell with fewer than two live neighbors dies, as if caused by under-population.
Any live cell with two or three live neighbors lives on to the next generation.
Any live cell with more than three live neighbors dies, as if by over-population..
Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
Write a function to compute the next state (after one update) of the board given its current state. The next state is created by applying the above rules simultaneously to every cell in the current state, where births and deaths occur simultaneously.

Example:

Input: 
[
  [0,1,0],
  [0,0,1],
  [1,1,1],
  [0,0,0]
]
Output: 
[
  [0,0,0],
  [1,0,1],
  [0,1,1],
  [0,1,0]
]
Follow up:

Could you solve it in-place? Remember that the board needs to be updated at the same time: You cannot update some cells first and then use their updated values to update other cells.
In this question, we represent the board using a 2D array. In principle, the board is infinite, which would cause problems when the active area encroaches the border of the array. How would you address these problems?

- time complexity: O(MN)
- space complexity: O(1)


'''
from typing import List
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        nrows = len(board)
        ncols = len(board[0])
        for row in range(nrows):
            for col in range(ncols):
                high_row = min(row + 1, nrows - 1)
                low_row = max(row - 1, 0)
                high_col = min(col + 1, ncols - 1)
                low_col = max(col - 1, 0)

                temp = self.get_sum(board, low_row, high_row, low_col, high_col)
                if board[row][col] == 1:
                    temp -= 1
                    if temp < 2 or temp > 3:
                        board[row][col] = -1
                else:
                    if temp == 3:
                        board[row][col] = 2
                        
        for row in range(nrows):
            for col in range(ncols):
                if board[row][col] == 2:
                    board[row][col] = 1
                elif board[row][col] == -1:
                    board[row][col] = 0
                
                        
    def get_sum(self, matrix, low_row, high_row, low_col, high_col):
        temp = 0
        for i in range(low_row, high_row+1):
            for j in range(low_col, high_col+1):
                if matrix[i][j] == 2:
                    val = 0
                elif matrix[i][j] == -1:
                    val = 1
                else:
                    val = matrix[i][j]
                temp += val  
        return temp