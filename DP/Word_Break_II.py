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
        '''Recursion and Memorization
        O(N^3)/O(N^3)
        '''
        word, N, memo = set(word), len(s), {}
        def backtrack(i, j):
            if memo.get((i, j), -1) != -1: return memo[i, j]
            if j == N + 1: return [[s[i:j]]] if s[i:j] in word else []
            if s[i:j] in word:
                sub1 = [[s[i:j]] + ele for ele in backtrack(j, j + 1)] 
                sub2 = backtrack(i, j + 1)
                sub = sub1 + sub2
            else:
                sub = backtrack(i, j + 1)
            memo[i, j] = sub
            return sub
        return [" ".join(eles) for eles in backtrack(0, 1)]
    