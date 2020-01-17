'''
link: https://leetcode.com/problems/minimum-window-substring/
Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

Example:

Input: S = "ADOBECODEBANC", T = "ABC"
Output: "BANC"
Note:

If there is no such window in S that covers all characters in T, return the empty string "".
If there is such window, you are guaranteed that there will always be only one unique minimum window in S.
'''

from collections import Counter


class Solution:
    '''O(|S|+|T|)/O(|T|)'''
    def minWindow(self, s: str, t: str) -> str:
        ans, count, l, r, char, s = [float('inf'), ''], len(t) , 0, 0, Counter(t), s + ' '
        while r < len(s):
            if count > 0:
                if char.get(s[r], -float('inf')) > -float('inf'):
                    if char.get(s[r], -float('inf')) > 0: count -= 1
                    char[s[r]] -= 1
                r += 1
            else:
                if ans[0] > r - l:
                    ans = [r - l, s[l:r]]
                if char.get(s[l], -float('inf')) > -float('inf'):
                    if char.get(s[l], -float('inf')) >= 0: count += 1
                    char[s[l]] += 1
                l += 1
        return ans[1]
    