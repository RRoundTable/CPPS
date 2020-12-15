'''
link: https://leetcode.com/problems/word-ladder/
Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation sequence from beginWord to endWord, such that:

Only one letter can be changed at a time.
Each transformed word must exist in the word list.
Note:

Return 0 if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume beginWord and endWord are non-empty and are not the same.
Example 1:

Input:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

Output: 5

Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
return its length 5.
Example 2:

Input:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]

Output: 0

Explanation: The endWord "cog" is not in wordList, therefore no possible transformation
'''
from collections import defaultdict, deque
from heapq import heappop, heappush, heapify


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        graph, length = defaultdict(list), len(beginWord)
        
        wordList += [beginWord]
        for i, w1 in enumerate(wordList[:-1]):
            for j, w2 in enumerate(wordList[i + 1:]):
                count = 0
                for k in range(length):
                    if w1[k] != w2[k]: count += 1
                if count == 1:
                    graph[w1].append(w2); graph[w2].append(w1)
        
        queue, visit, res = deque([(1, beginWord)]), set(), 0
                                               
        while queue:
            c, w = queue.popleft()
            if w in visit: continue
            if w == endWord:
                res = c; break
            for nw in graph[w]:
                if nw in visit: continue
                queue.append((c + 1, nw))

            visit.add(w)
        return res
    
    
class Solution:
    '''
    O(M^2N)/O(M^2N)
    
    '''
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        graph, length = defaultdict(list), len(beginWord)
        
        for w in wordList:
            for i in range(length):
                mid = w[:i] + '*' + w[i+1:]
                graph[mid].append(w)
        
        queue, seen, res = deque([(beginWord, 0)]), set(), 0
        
        while queue:
            w, c = queue.popleft()
            if w == endWord:
                res = c + 1; break
            for i in range(length):
                mid = w[:i] + '*' + w[i+1:]
                neis = graph[mid]
                for nei in neis:
                    if nei not in seen:
                        queue.append((nei, c + 1))
            seen.add(w)
                
        return res