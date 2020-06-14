'''
link: https://leetcode.com/problems/sliding-puzzle/

On a 2x3 board, there are 5 tiles represented by the integers 1 through 5, and an empty square represented by 0.

A move consists of choosing 0 and a 4-directionally adjacent number and swapping it.

The state of the board is solved if and only if the board is [[1,2,3],[4,5,0]].

Given a puzzle board, return the least number of moves required so that the state of the board is solved. If it is impossible for the state of the board to be solved, return -1.

Examples:

Input: board = [[1,2,3],[4,0,5]]
Output: 1
Explanation: Swap the 0 and the 5 in one move.
Input: board = [[1,2,3],[5,4,0]]
Output: -1
Explanation: No number of moves will make the board solved.
Input: board = [[4,1,2],[5,0,3]]
Output: 5
Explanation: 5 is the smallest number of moves that solves the board.
An example path:
After move 0: [[4,1,2],[5,0,3]]
After move 1: [[4,1,2],[0,5,3]]
After move 2: [[0,1,2],[4,5,3]]
After move 3: [[1,0,2],[4,5,3]]
After move 4: [[1,2,0],[4,5,3]]
After move 5: [[1,2,3],[4,5,0]]
Input: board = [[3,2,4],[1,5,0]]
Output: 14
Note:

board will be a 2 x 3 array as described above.
board[i][j] will be a permutation of [0, 1, 2, 3, 4, 5].

'''


from collections import deque
import copy
class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        
        def next_node(board):
            for i in range(len(board)):
                for j in range(len(board[0])):
                    if board[i][j] == 0: save = (i, j)
            res = []
            i, j = save
            if i + 1 < len(board):
                board[i][j], board[i+1][j] = board[i+1][j], board[i][j]
                res.append(copy.deepcopy(board))
                board[i][j], board[i+1][j] = board[i+1][j], board[i][j]
            if i - 1 >= 0:
                board[i][j], board[i-1][j] = board[i-1][j], board[i][j]
                res.append(copy.deepcopy(board))
                board[i][j], board[i-1][j] = board[i-1][j], board[i][j]
            if j + 1 < len(board[0]):
                board[i][j], board[i][j+1] = board[i][j+1], board[i][j]
                res.append(copy.deepcopy(board))
                board[i][j], board[i][j+1] = board[i][j+1], board[i][j]
            if j - 1 >= 0:
                board[i][j], board[i][j-1] = board[i][j-1], board[i][j]
                res.append(copy.deepcopy(board))
                board[i][j], board[i][j-1] = board[i][j-1], board[i][j]
            
            return res
        
        def hashable(board):
            res = ''
            for i in range(len(board)):
                for j in range(len(board[0])):
                    res += str(board[i][j])
            return res
        
        
        target = [[1,2,3],[4,5,0]]5
        que, seen, ans = deque([board]), set(), 0
       
        while que:
            size = len(que)
            count = 0
            while que and count < size:
                board = que.popleft(); count += 1
                if board == target: return ans
                h = hashable(board)
                if h not in seen:
                    seen.add(h)
                    for nei in next_node(board):
                        if hashable(nei) not in seen:
                            que.append(nei)  
            ans += 1
        return -1
        