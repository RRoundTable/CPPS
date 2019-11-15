"""
link: https://leetcode.com/explore/learn/card/queue-stack/230/usage-stack/1394/

Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, /. Each operand may be an integer or another expression.

Note:

Division between two integers should truncate toward zero.
The given RPN expression is always valid. That means the expression would always evaluate to a result and there won't be any divide by zero operation.
Example 1:

Input: ["2", "1", "+", "3", "*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9
Example 2:

Input: ["4", "13", "5", "/", "+"]
Output: 6
Explanation: (4 + (13 / 5)) = 6
Example 3:

Input: ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
Output: 22
Explanation: 
  ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
= ((10 * (6 / (12 * -11))) + 17) + 5
= ((10 * (6 / -132)) + 17) + 5
= ((10 * 0) + 17) + 5
= (0 + 17) + 5
= 17 + 5
= 22
"""

import math


class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        eq = None
        for i in range(len(tokens)):
            if tokens[i] in ["+", "-", "/", "*"]:
                s1, s2 = stack.pop(-1), stack.pop(-1)
                if tokens[i] == "+":
                    eq = int(s2) + int(s1)
                elif tokens[i] == "-":
                    eq = int(s2) - int(s1)
                elif tokens[i] == "*":
                    eq = int(s2) * int(s1)
                elif tokens[i] == "/":
                    eq = float(s2) / int(s1)
                    if eq < 0:
                        eq = math.ceil(eq)
                stack.append(eq)
            else:
                stack.append(tokens[i])

        return int(stack.pop(-1))
