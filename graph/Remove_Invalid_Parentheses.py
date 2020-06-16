'''
link: https://leetcode.com/problems/remove-invalid-parentheses/
Remove the minimum number of invalid parentheses in order to make the input string valid. Return all possible results.

Note: The input string may contain letters other than the parentheses ( and ).

Example 1:

Input: "()())()"
Output: ["()()()", "(())()"]
Example 2:

Input: "(a)())()"
Output: ["(a)()()", "(a())()"]
Example 3:

Input: ")("
Output: [""]

'''

from collections import deque

class Solution:
    '''O(2^N)/O(2^N)'''
    def removeInvalidParentheses(self, s: str) -> List[str]:
       
        def validate(s):
            stack = []
            for i in range(len(s)):
                if s[i] =='(':
                    stack.append(s[i])
                elif s[i] == ')':
                    if stack: stack.pop()
                    else: return False
            return not stack
        
        
        def neighbor(s):
            res = []
            for i in range(len(s)):
                if s[i] in '()':
                    res.append(s[:i] + s[i+1:])
            return res if res else [""]
        
        
        que, seen, res = deque([s]), set(), []
        
        while que:
            size = len(que)
            count = 0
            while que and count < size:
                node = que.popleft(); count += 1
                if node not in seen:
                    if validate(node): 
                        res.append(node)
                    seen.add(node)
                    for nei in neighbor(node):
                        if nei not in seen:
                            que.append(nei)
            if res: break
        
        return res
    
class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
       
        def validate(s):
            stack = []
            for i in range(len(s)):
                if s[i] =='(':
                    stack.append(s[i])
                elif s[i] == ')':
                    if stack: stack.pop()
                    else: return False
            return not stack
        
        que, seen, res = [s], set(), []
        
        while que:
            res = list(filter(validate, que))
            if res: 
                return res
            level = []
            for s in que:
                for i in range(len(s)):
                    if s[i] in '()' and s[:i] + s[i+1:] not in seen:
                        level.append(s[:i] + s[i+1:])
                        seen.add(s[:i] + s[i+1:])
            que = level