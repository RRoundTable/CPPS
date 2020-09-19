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
        ans = []
        def dfs(i, string, curr, last):
            nonlocal ans, num, target
            if i == len(num):
                if curr == target:
                    ans.append(string)
                return
            c = 0
            for j in range(i, len(num)):
                c = c * 10 + int(num[j])
                if i == 0:
                    dfs(j+1, str(c), c, c)
                else:
                    dfs(j+1, string + '*' + str(c), curr - last + last * c, last * c)
                    dfs(j+1, string + '+' + str(c), curr + c, c)
                    dfs(j+1, string + '-' + str(c), curr - c, -c)
                if num[i] == '0': break
        dfs(0, '', 0, 0)
        return ans