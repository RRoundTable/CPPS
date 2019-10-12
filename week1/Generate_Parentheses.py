'''
link: https://leetcode.com/problems/generate-parentheses/

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]

# main idea

recusion tree, DEF

# check how to calculate time complexity
- link: https://leetcode.com/problems/generate-parentheses/discuss/10099/time-complexity-to-generate-all-combinations-of-well-formed-parentheses

- time complexcity: O(4 ^ N / N ^ 0.5)

- space complexity: O(4 ^ N / N ^ 0.5)

'''

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        left = 0
        right = 0
        s = ""
        def generate(s, left, right):
            if len(s) == 2 * n:
                ans.append(s)
            if left < n:
                generate(s + "(", left + 1, right)
            if right < left:
                generate(s + ")", left, right + 1)
        generate(s, left, right)
        return ans