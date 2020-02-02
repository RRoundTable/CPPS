'''
link: https://leetcode.com/problems/longest-palindromic-substring/
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb"
'''

class Solution:
    def longestPalindrome(self, s: str) -> str:
        '''O(N^2)/O(1)'''
        ans = [0, (0, 0)]
        for i in range(1, len(s)):
            l, r, count = i, i, 0
            while l >= 0 and r < len(s):
                if s[l] == s[r]:
                    count = count + 1 if l == r else count + 2
                    if ans[0] < count: ans = [count, (l, r)]
                    l, r = l - 1, r + 1
                else: break
            l, r, count = i-1, i, 0
            while l >= 0 and r < len(s):
                if s[l] == s[r]:
                    count += 2
                    if ans[0] < count: ans = [count, (l, r)]
                    l, r = l - 1, r + 1
                else: break
        return s[ans[1][0]: ans[1][1] + 1] if s else ''