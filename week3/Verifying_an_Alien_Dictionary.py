"""
link: https://leetcode.com/problems/verifying-an-alien-dictionary/

In an alien language, surprisingly they also use english lowercase letters, but possibly in a different order. The order of the alphabet is some permutation of lowercase letters.

Given a sequence of words written in the alien language, and the order of the alphabet, return true if and only if the given words are sorted lexicographicaly in this alien language.

 

Example 1:

Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
Output: true
Explanation: As 'h' comes before 'l' in this language, then the sequence is sorted.
Example 2:

Input: words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
Output: false
Explanation: As 'd' comes after 'l' in this language, then words[0] > words[1], hence the sequence is unsorted.
Example 3:

Input: words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"
Output: false
Explanation: The first three characters "app" match, and the second string is shorter (in size.) According to lexicographical rules "apple" > "app", because 'l' > '∅', where '∅' is defined as the blank character which is less than any other character (More info).
 

Note:

1 <= words.length <= 100
1 <= words[i].length <= 20
order.length == 26
All characters in words[i] and order are english lowercase letters.
"""

from collections import defaultdict
from typing import List


class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        """O(NlogN)/O(N)"""
        d = defaultdict(lambda: 0)
        for i in range(len(order)):
            d[order[i]] = i

        return words == sorted(words, key=lambda x: [d[ele] for ele in x])

    def isAlienSorted2(self, words: List[str], order: str) -> bool:
        """O(N)/O(N)"""
        d = defaultdict(lambda: 0)
        for i in range(len(order)):
            d[order[i]] = i

        words = [[d[w] for w in word] for word in words]

        i = 0
        j = 0

        for i in range(len(words) - 1):
            if words[i] < words[i + 1]:
                continue
            else:
                return False
        return True

