'''
link:https://leetcode.com/problems/word-break-ii/

Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, add spaces in s to construct a sentence where each word is a valid dictionary word. Return all such possible sentences.

Note:

The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.
Example 1:

Input:
s = "catsanddog"
wordDict = ["cat", "cats", "and", "sand", "dog"]
Output:
[
  "cats and dog",
  "cat sand dog"
]
Example 2:

Input:
s = "pineapplepenapple"
wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
Output:
[
  "pine apple pen apple",
  "pineapple pen apple",
  "pine applepen apple"
]
Explanation: Note that you are allowed to reuse a dictionary word.
Example 3:

Input:
s = "catsandog"
wordDict = ["cats", "dog", "sand", "and", "cat"]
Output:
[]

'''

class Solution:
    def wordBreak(self, s: str, word: List[str]) -> List[str]:
        '''Recursion and Memorization'''
        word, N, memo = set(word), len(s), {}
        def backtrack(i, j):
            if memo.get(i) != -1: return memo[i]
            if j == N + 1: return [[s[i:j]]] if s[i:j] in word else []
            if s[i:j] in word:
                sub1 = [[s[i:j]] + ele for ele in backtrack(j, j + 1)] 
                sub2 = backtrack(i, j + 1)
                sub = sub1 + sub2
            else:
                sub = backtrack(i, j + 1)
            memo[i] = sub
            return sub
        return [" ".join(eles) for eles in backtrack(0, 1)]
    
    

class Solution:
    def wordBreak(self, s: str, word: List[str]) -> List[str]:
        '''Recursion and Memorization'''
        word, r, memo = set(word), max(len(w) for w in word + ['1']), {len(s): ['']}
        def sentence(start):
            if start not in memo:
                memo[start] = [
                    s[start:j] + (tail and " " + tail)
                    for j in range(start+1, start+r+1) if s[start:j] in word
                    for tail in sentence(j)
                ]
            return memo[start]
        return sentence(0)


  class Solution:
    '''Dynamic Programing'''
    def wordBreak(self, s: str, word: List[str]) -> bool:
        wordDict, r, dp, N = set(word), max(len(w) for w in word + ['1']), [[] for _ in range(len(s)+1)], len(s)
        dp[0] = ['']
        for i in range(N+1):
            for j in range(max(i-r, 0), i):
                if s[j:i] in wordDict and len(dp[j]) > 0:
                    dp[i] += [head + (head and " ") + s[j:i] for head in dp[j]]
        return dp[-1]