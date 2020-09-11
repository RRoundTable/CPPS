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


from collections import deque


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        '''O(N^2)/O(N)'''
        wordDict, N, dp = set(wordDict), len(s), [False] * len(s)
        for i in range(N):
            for j in range(i, N):
                if s[i:j+1] in wordDict:
                    if i == 0: dp[j] = True
                    if dp[i-1]: dp[j] = True   
        return dp[N-1]
    
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        '''O(N^2)/O(N)'''
        wordDict, N, dp = set(wordDict), len(s), [True]
        for i in range(1, N + 1):
            dp += any(dp[j] and s[j:i] in wordDict for j in range(i)),
        return dp[-1]


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        '''O(N^2)/O(N)'''
        wordDict, visited, queue = set(wordDict), [False] * len(s), deque([])
        queue.append(0)
        while queue:
            start = queue.popleft()
            if not visited[start]:
                for end in range(start+1, len(s)+1):
                    if s[start:end] in wordDict:
                        queue.append(end)
                        if end == len(s): return True
                visited[start] = True
        return False


class Solution:
    def wordBreak(self, s: str, word_dict: List[str]) -> bool:
        word_dict = set(word_dict)
        word_len = set(map(len, word_dict))

        def backtrack(s):
            nonlocal word_dict, word_len
            if s == '': return True
            for window in word_len:
                for i in range(len(s) - window + 1):
                    if s[i: i + window] in word_dict:
                        if backtrack(s[:i]) and backtrack(s[i+window:]):
                            return True
            return False
        return backtrack(s)
    
    
class Solution:
    def wordBreak(self, s: str, word_dict: List[str]) -> bool:
        word_dict = set(word_dict)
        word_len, n  = set(map(len, word_dict)), len(s)
        
        dp = [[False] * n for _ in range(n)]
        
        for i in range(n):
            for j in range(i, n):
                if s[i:j+1] in word_dict: dp[i][j] = True

        for i in range(n):
            for j in range(i, n):
                for k in range(i, j):
                    dp[i][j] = dp[i][j] or (dp[i][k] and dp[k+1][j])
        return dp[0][-1]