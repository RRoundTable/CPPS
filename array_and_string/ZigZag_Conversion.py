'''
link: https://leetcode.com/problems/zigzag-conversion/submissions/
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);
Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:

P     I    N
A   L S  I G
Y A   H R
P     I
'''

from collections import defaultdict


class Solution:
    def convert(self, s: str, nrow: int) -> str:
        if nrow == 1: return s
        row_dict, row, dire = defaultdict(list), 1, -1
        for i in range(len(s)):
            row_dict[row].append(s[i])
            if row == 1 or row == nrow: dire *= -1
            row += dire
        
        return "".join(ele for i in range(1, nrow + 1) for ele in row_dict[i])
    
    
class Solution:
    def convert(self, s: str, nrow: int) -> str:
        if nrow == 1: return s
        rows = [[] for _ in range(nrow)]
        cycle = (nrow - 1) * 2
        for i in range(len(s)):
            mod = i % cycle
            if mod < nrow:
                rows[mod].append(s[i])
            else:
                rows[nrow - (mod - nrow + 2)].append(s[i])
        
        return "".join("".join(s) for s in rows)
    
    
