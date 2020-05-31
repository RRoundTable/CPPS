'''
link: https://leetcode.com/problems/concatenated-words/
Given a list of words (without duplicates), please write a program that returns all concatenated words in the given list of words.
A concatenated word is defined as a string that is comprised entirely of at least two shorter words in the given array.

Example:
Input: ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]

Output: ["catsdogcats","dogcatsdog","ratcatdogcat"]

Explanation: "catsdogcats" can be concatenated by "cats", "dog" and "cats"; 
 "dogcatsdog" can be concatenated by "dog", "cats" and "dog"; 
"ratcatdogcat" can be concatenated by "rat", "cat", "dog" and "cat".
Note:
The number of elements of the given array will not exceed 10,000
The length sum of elements in the given array will not exceed 600,000.
All the input string will only include lower case letters.
The returned elements order does not matter.


'''

class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        
        words = set(words)
        ans = []
        max_length = max(map(len, words))
    
        memo = {}
        def dfs(word, n):
            nonlocal words, max_length, ans
            if memo.get(word, False):
                return memo[word]
            if len(word) > max_length: 
                return []
            if word in words and n >= 2: 
                return [word]
            res = []
            for ele in words :
                res += dfs(word + ele, n + 1)
            if res: memo[word] = res
            return res

        return dfs("", 0) if len(words) >= 2 else None
    
    

class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        
        word_set, res = set(words), []
        
        def complete(word):
            nonlocal word_set
            if word in word_set: 
                return True
            for i in range(len(word)):
                for j in range(i + 1, len(word) + 1):
                    if word[i:j] in word_set:
                        if complete(word[:i] + word[j:]):
                            return True
            return False
        
        for word in words:
            word_set.remove(word)
            if complete(word):
                res.append(word)
            word_set.add(word)
        return res
    
class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        
        word_set, res = set(words), []
        def complete(word):
            nonlocal word_set
            dp = [False for _ in range(len(word) + 1)]
            dp[0] = True
            for i in range(1, len(word) + 1):
                for j in range(i):
                    if not dp[j]: continue
                    if word[j:i] in word_set:
                        dp[i] = True
                        break
            return dp[-1]
        
        for word in words:
            if not word: continue
            word_set.remove(word)
            if complete(word):
                res.append(word)
            word_set.add(word)
        return res
            

            