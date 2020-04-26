'''
link:https://leetcode.com/problems/substring-with-concatenation-of-all-words/
You are given a string, s, and a list of words, words, that are all of the same length. Find all starting indices of substring(s) in s that is a concatenation of each word in words exactly once and without any intervening characters.

 

Example 1:

Input:
  s = "barfoothefoobarman",
  words = ["foo","bar"]
Output: [0,9]
Explanation: Substrings starting at index 0 and 9 are "barfoo" and "foobar" respectively.
The output order does not matter, returning [9,0] is fine too.
Example 2:

Input:
  s = "wordgoodgoodgoodbestword",
  words = ["word","good","best","word"]
Output: []
'''

from collections import Counter

    
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words: return []
        count, wl, hist, ans = Counter(words), len(words[0]), [], []
        for i in range(len(s)):
            for j in range(i, len(s) + 1, wl):
                if count[s[j:j + wl]]:
                    count[s[j: j + wl]] -= 1
                    hist.append(s[j:j+wl])
                else:break
            if len(hist) == len(words): ans.append(i)
            while hist: count[hist.pop()] += 1
        return ans
    
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words: return []
        count, wl, hist, ans = Counter(words), len(words[0]), [], []
        for i in range(wl):
            for j in range(i, len(s) + 1, wl):
                for k in range(j, len(s) + 1, wl):
                    if count[s[k:k+wl]]:
                        count[s[k:k+wl]] -= 1
                        hist.append(s[k:k+wl])
                    else: break
                if len(hist) == len(words): ans.append(j)
                while hist: count[hist.pop()] += 1
        return ans
    
class Solution:
    '''O(S)/O(W)'''
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words: return []
        wl, ans = len(words[0]), []
        for i in range(wl):
            count = Counter(words)
            for j in range(i + wl, len(s) + 1, wl):
                word = s[j-wl:j]
                count[word] -= 1
                while count[word] < 0:
                    count[s[i:i+wl]] += 1
                    i += wl
                if i + wl * len(words) == j: ans.append(i)
        return ans

