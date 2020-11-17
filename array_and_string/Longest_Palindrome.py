'''
link: https://leetcode.com/problems/longest-palindrome/
Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.

Letters are case sensitive, for example, "Aa" is not considered a palindrome here.

 

Example 1:

Input: s = "abccccdd"
Output: 7
Explanation:
One longest palindrome that can be built is "dccaccd", whose length is 7.
Example 2:

Input: s = "a"
Output: 1
Example 3:

Input: s = "bb"
Output: 2
 

Constraints:

1 <= s.length <= 2000
s consits of lower-case and/or upper-case English letters only.

'''
from collections import Counter


class Solution:
    def longestPalindrome(self, s: str) -> int:
        count, res, odd = Counter(s), 0, 0
        for c in count.values():
            if c % 2 == 1:
                c -= 1; odd += 1
            res += c
        return res + min(odd, 1)