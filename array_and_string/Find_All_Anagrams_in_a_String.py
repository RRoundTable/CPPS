'''
link: https://leetcode.com/problems/find-all-anagrams-in-a-string/
Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.

Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.

The order of output does not matter.

Example 1:

Input:
s: "cbaebabacd" p: "abc"

Output:
[0, 6]

Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
Example 2:

Input:
s: "abab" p: "ab"

Output:
[0, 1, 2]

Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".

'''
from collections import Counter

    
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        d, res, k, l, r = Counter(p), [], len(p), 0, 0
        while l <= r and r < len(s):
            d[s[r]] -= 1
            while d[s[r]] < 0 and l <= r:
                d[s[l]] += 1
                l += 1
            r += 1
            if r - l == k: res.append(l)
        return res
