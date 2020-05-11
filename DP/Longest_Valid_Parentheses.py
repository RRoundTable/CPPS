'''
link: https://leetcode.com/problems/longest-valid-parentheses/

Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

Example 1:

Input: "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()"
Example 2:

Input: ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()"
'''

class Solution:
    '''O(N^3)/O(N)'''
    def longestValidParentheses(self, s: str) -> int:
        ans = 0
        for i in range(len(s)):
            for j in range(i+1, len(s) + 1):
                if self.isValid(s[i:j]): ans = max(ans, j - i) 
        return ans
    
    def isValid(self, s: str) -> bool:
        stack, d = [], {"(": ')', '{': '}', '[': ']'}
        for ele in s:
            if ele in ['(', '[', '{']: stack.append(ele)
            else:
                if stack:
                    pop = stack.pop()
                    if d[pop] != ele: return False
                else: return False
        return not stack
    
class Solution:
    '''O(N)/O(N)'''
    def longestValidParentheses(self, s: str) -> int:
        stack, ans = [-1], 0
        for i in range(len(s)):
            if s[i] == "(": 
                stack.append(i);
            else:
                j = stack.pop()
                if stack: ans = max(ans, i - stack[-1])
                if not stack: 
                    stack.append(i)
        return ans