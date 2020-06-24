'''
link: https://leetcode.com/problems/word-search-ii/


Given a 2D board and a list of words from the dictionary, find all words in the board.

Each word must be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

 

Example:

Input: 
board = [
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]
words = ["oath","pea","eat","rain"]

Output: ["eat","oath"]
 

Note:

All inputs are consist of lowercase letters a-z.
The values of words are distinct.
'''



class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        WORD_KEY = '$'
        trie = {}
        for word in words:
            node = trie
            for letter in word:
                node = node.setdefault(letter, {})
            node[WORD_KEY] = word
        
        nrow, ncol = len(board), len(board[0])
        
        ans = []
        
        def backtrack(row, col, parent):
            
            nonlocal ans
            
            letter = board[row][col]
            curr = parent[letter]
            
            word_match = curr.pop(WORD_KEY, False)
            if word_match:
                ans.append(word_match)
            
            board[row][col] = '#'
            for (rowoffset, coloffset) in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                newrow, newcol = row + rowoffset, col + coloffset
                if newrow < 0 or newrow >= nrow or newcol < 0 or newcol >= ncol or (not board[newrow][newcol] in curr):
                    continue
                    
                backtrack(newrow, newcol, curr)
            
            board[row][col] = letter
            
            if not curr:
                parent.pop(letter)
            
    
        for row in range(nrow):
            for col in range(ncol):
                if board[row][col] in trie:
                    backtrack(row, col, trie)
                    
        return ans
        
        
        
        