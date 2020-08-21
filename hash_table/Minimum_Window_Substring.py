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
                if s[r] in char:
                    count -= char[s[r]] > 0
                    char[s[r]] -= 1
                r += 1
            else:
                if ans[0] > r - l:
                    ans = [r - l, (l, r)]
                if s[l] in char:
                    count += char[s[l]] >= 0
                    char[s[l]] += 1
                l += 1
        return s[ans[1][0]:ans[1][1]] if ans[0] < float('inf') else ''


from collections import Counter, defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        count = Counter(t)
        i, j, check, ans = 0, 0, set(count.keys()), ''
     
        while i <= j and j < len(s):
            if s[j] in check:
                count[s[j]] -= 1

            if all(v <= 0 for v in count.values()):
                while s[i] not in check or count[s[i]] < 0:
                    if s[i] in check:
                        count[s[i]] += 1
                    i += 1
                if ans == '' or j - i + 1 < len(ans):
                    ans = s[i:j+1]
                if s[i] in check:
                    count[s[i]] += 1
                i += 1
            j += 1
        return ans
        
    