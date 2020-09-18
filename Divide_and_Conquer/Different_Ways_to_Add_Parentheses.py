'''
link: https://leetcode.com/problems/different-ways-to-add-parentheses/
Given a string of numbers and operators, return all possible results from computing all the different possible ways to group numbers and operators. The valid operators are +, - and *.

Example 1:

Input: "2-1-1"
Output: [0, 2]
Explanation: 
((2-1)-1) = 0 
(2-(1-1)) = 2
Example 2:

Input: "2*3-4*5"
Output: [-34, -14, -10, -10, 10]
Explanation: 
(2*(3-(4*5))) = -34 
((2*3)-(4*5)) = -14 
((2*(3-4))*5) = -10 
(2*((3-4)*5)) = -10 
(((2*3)-4)*5) = 10
'''
import operator

class Solution:
    def diffWaysToCompute(self, input: str) -> List[int]:
        oper = {
            '+': operator.add, '-': operator.sub, '*': operator.mul
        }
        memo = {}
        def backtrack(input):
            nonlocal oper, memo
            if input in memo: return memo[input]
            if '+' not in input and '-' not in input and '*' not in input: return [int(input)]
            possible_res = []
            for i, ele in enumerate(input):
                if ele in ['+', '-', '*']:
                    for front in backtrack(input[:i]):
                        for back in backtrack(input[i+1:]): 
                            possible_res.append(oper[ele](front, back))
            memo[input] = possible_res
            return possible_res
        return backtrack(input)
        