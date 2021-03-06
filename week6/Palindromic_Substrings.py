"""
link: https://leetcode.com/problems/palindromic-substrings/

Given a string, your task is to count how many palindromic substrings in this string.

The substrings with different start indexes or end indexes are counted as different substrings even they consist of same characters.

Example 1:

Input: "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".
 

Example 2:

Input: "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
 

Note:

The input string length won't exceed 1000.
"""


class Solution(object):
    
    def countSubstrings(self, s):
        """O(N ^ 2)/O(1)
        small -> long 
        :type s: str
        :rtype: int
        """
        ans = len(s)

        for i in range(len(s) - 1):
            if s[i] == s[i + 1]:
                left, right, ans = i - 1, i + 2, ans + 1
                while left >= 0 and right < len(s):
                    if s[left] == s[right]:
                        left, right, ans = left - 1, right + 1, ans + 1
                    else:
                        break
            if i > 0 and s[i - 1] == s[i + 1]:
                left, right, ans = i - 2, i + 2, ans + 1
                while left >= 0 and right < len(s):
                    if s[left] == s[right]:
                        left, right, ans = left - 1, right + 1, ans + 1
                    else:
                        break
        return ans


class Solution(object):
    def countSubstrings(self, s):
        """
        small -> long 
        :type s: str
        :rtype: int
        """
        def move(left, right, ans):
            while left >= 0 and right < len(s):
                if s[left] == s[right]:
                    left, right, ans = left - 1, right + 1, ans + 1
                else: break
            return ans
        ans = len(s)
        for i in range(len(s) - 1):
            if s[i] == s[i + 1]:
                left, right, ans = i - 1, i + 2, ans + 1            
                ans = move(left, right, ans)
            if i > 0 and s[i - 1] == s[i + 1]:
                left, right, ans = i - 2, i + 2, ans + 1
                ans = move(left, right, ans)
        return ans