'''
link: https://leetcode.com/problems/word-break/
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words.

Note:

The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.
Example 1:

Input: s = "leetcode", wordDict = ["leet", "code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
Example 2:

Input: s = "applepenapple", wordDict = ["apple", "pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
             Note that you are allowed to reuse a dictionary word.
Example 3:

Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
Output: false
'''

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        '''O(N^2)/O(N)'''
        wordDict, N, dp = set(wordDict), len(s), [False] * len(s)
        for i in range(N):
            for j in range(N):
                if s[i:j+1] in wordDict:
                    if i == 0: dp[j] = True
                    if dp[i-1]: dp[j] = True   
        return dp[N-1]