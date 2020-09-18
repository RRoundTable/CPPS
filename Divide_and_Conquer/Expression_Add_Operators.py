'''
link: https://leetcode.com/problems/expression-add-operators/

Given a string that contains only digits 0-9 and a target value, return all possibilities to add binary operators (not unary) +, -, or * between the digits so they evaluate to the target value.

Example 1:

Input: num = "123", target = 6
Output: ["1+2+3", "1*2*3"] 
Example 2:

Input: num = "232", target = 8
Output: ["2*3+2", "2+3*2"]
Example 3:

Input: num = "105", target = 5
Output: ["1*0+5","10-5"]
Example 4:

Input: num = "00", target = 0
Output: ["0+0", "0-0", "0*0"]
Example 5:

Input: num = "3456237490", target = 9191
Output: []
 

Constraints:

0 <= num.length <= 10
num only contain digits.
'''

class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        oper = {'+': operator.add, '-': operator.sub, '*': operator.mul}
        ans = []
        def search(idx, pre_res, cum_res, string):
        
            nonlocal ans, target
            if idx >= len(num):
                if string and eval(string) == target:
                    ans.append(string)
                return
            # No operation
            if not (pre_res == 0 and string and string[-1] == '0'):
               
                search(idx + 1, pre_res * 10 + int(num[idx]), cum_res - pre_res + pre_res * 10 + int(num[idx]), string + num[idx])
            if string and string[-1] not in oper.keys():
                # add
                search(idx + 1, int(num[idx]), cum_res + int(num[idx]), string + '+' + num[idx])
                # sub
                search(idx + 1, int(num[idx]), cum_res - int(num[idx]), string + '-' + num[idx])
                # mul
                if num[idx] == '0' or (string and string[-1]) == '0': new_pre_res = 0
                else:
                    new_pre_res = int(num[idx]) * int(pre_res)
                search(idx + 1, new_pre_res, cum_res - pre_res + new_pre_res, string + '*' + num[idx])
        search(0, 0, 0, '')
        return ans