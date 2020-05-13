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


class Solution:
    '''O(N)/O(N)'''
    def longestValidParentheses(self, s: str) -> int:
        dp = [0] * len(s)
        for i in range(1, len(s)):
            if s[i] == ')':
                if s[i-1] == '(':
                    dp[i] = 2 + dp[i-2] if i - 2 >= 0 else 2
                elif s[i - dp[i-1] - 1] == "(":
                    dp[i] = dp[i-1] + dp[i - dp[i-1] - 2] + 2
        return max(dp) if s else 0 
    
class Solution:
    '''O(N)/O(1)'''
    def longestValidParentheses(self, s: str) -> int:
        ans, left, right = 0, 0, 0
        for i in range(len(s)):
            if s[i] == ')':
                right += 1
                if right > left: left, right = 0, 0
                ans = max(ans, right * 2) if left == right else ans
            else:
                left += 1
        left, right = 0, 0
        for i in reversed(range(len(s))):
            if s[i] == ')':
                right += 1
            else:
                left += 1
                if left > right: left, right = 0, 0
                ans = max(ans, right * 2) if left == right else ans
        return ans