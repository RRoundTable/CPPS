'''
link: https://leetcode.com/problems/longest-substring-without-repeating-characters/
Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. 
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
'''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d, ans, i, j = {}, 0, -1, 0
        while j < len(s):
            if d.get(s[j], -1) == -1:
                d[s[j]], j = j, j + 1
            else:
                ans = max(ans, j - i - 1)
                while i < j:
                    d[s[i+1]], i = -1, i + 1
                    if s[i] == s[j]: break
        return max(ans, j - i - 1)