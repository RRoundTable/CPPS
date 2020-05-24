'''
link: https://leetcode.com/problems/basic-calculator/
Implement a basic calculator to evaluate a simple expression string.

The expression string may contain open ( and closing parentheses ), the plus + or minus sign -, non-negative integers and empty spaces .

Example 1:

Input: "1 + 1"
Output: 2
Example 2:

Input: " 2-1 + 2 "
Output: 3
Example 3:

Input: "(1+(4+5+2)-3)+(6+8)"
Output: 23
Note:
You may assume that the given expression is always valid.
Do not use the eval built-in library function.

'''

class Solution:
    def calculate(self, s: str) -> int:
        stack, ans = [], 0
        for ele in s:
            if ele == ' ': continue
            if ele == ')':
                temp = ''
                while stack:
                    pop = stack.pop()
                    if pop == '(': break
                    temp = pop + temp
                stack.append(str(eval(temp)))
            else:
                stack.append(ele)
        return eval("".join(stack))
    
class Solution:    
    
    def calculate(self, s: str) -> int:
        s, stack, ans = "(" + s + ")", [], 0
        
        for ele in s:
            if ele == ' ': continue
            if ele == ')':
                inner = 0
                while stack:
                    pop = stack.pop()
                    if pop == '(': break
                    elif pop == '+':
                        inner += int(temp)
                    elif pop == '-':
                        inner -= int(temp)
                    else:
                        temp = pop
                inner += int(temp)
                stack.append(str(inner))
            else:
                if stack and ele not in {'+', '-', '(', ')'} and stack[-1] not in {'+', '-', '(', ')'}:
                    stack[-1] += ele
                else: stack.append(ele)
    
        return int(stack[-1])
        