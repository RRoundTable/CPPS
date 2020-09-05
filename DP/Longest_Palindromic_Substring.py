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


class Solution:
    def longestPalindrome(self, s: str) -> str:
        left, right, max_length = 0, 0, min(1, len(s))
        for c_idx in range(len(s) - 1):
            l, r = c_idx, c_idx
            while l - 1 >= 0 and r + 1 < len(s) and s[l-1] == s[r+1]:
                l -= 1; r += 1
            if r - l + 1 > max_length:
                max_length = r - l + 1
                left, right = l, r
            l, r = c_idx, c_idx + 1
            while l - 1 >= 0 and r + 1 < len(s) and s[l-1] == s[r+1] and s[l] == s[r]:
                l -= 1; r += 1
            if r - l + 1 > max_length and s[c_idx] == s[c_idx+1]:
                max_length = r - l + 1
                left, right = l, r
        
        return s[left:right+1]

class Solution:
    def longestPalindrome(self, s: str) -> str:
        T = '#'.join(f'#{s}#')
        dp, R, C = [0] * len(T), 0, 0
        for i in range(1, len(T) - 1):
            dp[i] = (R > i) and min(R - i, dp[2*C - i])
            while i + 1 + dp[i] < len(T) and i - 1 - dp[i] >= 0 and T[i + 1 + dp[i]] == T[i - 1 - dp[i]]:
                dp[i] += 1
            if i + dp[i] > R:
                C, R = i, dp[i] + i
        maxLen, centerIndex = max((n, i) for i, n in enumerate(dp))
        return s[(centerIndex  - maxLen)//2: (centerIndex  + maxLen)//2]