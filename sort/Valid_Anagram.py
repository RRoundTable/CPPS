'''
link: https://leetcode.com/problems/valid-anagram/
Given two strings s and t , write a function to determine if t is an anagram of s.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
Note:
You may assume the string contains only lowercase alphabets.

Follow up:
What if the inputs contain unicode characters? How would you adapt your solution to such case?

'''

from collections import Counter
class Solution:
    '''
    O(N)/O(N)
    '''
    def isAnagram(self, s: str, t: str) -> bool:
        count = Counter(s)    
        for c in t:
            if count.get(c, 0) > 0:
                count[c] -= 1
                if count[c] == 0: count.pop(c)
    
        return len(s) == len(t) and len(count) == 0
    
class Solution:
    '''
    O(NlogN)/O(1)
    '''
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)