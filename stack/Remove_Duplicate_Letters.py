'''
link: https://leetcode.com/problems/remove-duplicate-letters/
Given a string which contains only lowercase letters, remove duplicate letters so that every letter appears once and only once. You must make sure your result is the smallest in lexicographical order among all possible results.

Example 1:

Input: "bcabc"
Output: "abc"
Example 2:

Input: "cbacdcbc"
Output: "acdb"
Note: This question is the same as 1081: https://leetcode.com/problems/smallest-subsequence-of-distinct-characters/
'''

from collections import Counter, defaultdict
class Solution:
    '''O(N)/O(N)'''
    def removeDuplicateLetters(self, s: str) -> str:
        count, used, remain = Counter(s), set(), []
        for c in s:
            if c in used: 
                count[c] -= 1; continue
            while remain and remain[-1] >= c and count[remain[-1]] >= 1:
                used.remove(remain.pop())
            if c not in used:
                used.add(c); count[c] -= 1
                remain.append(c)
        
        return "".join(remain)