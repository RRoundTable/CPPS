'''
link: https://leetcode.com/problems/group-anagrams/
Given an array of strings, group anagrams together.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note:

All inputs will be in lowercase.
The order of your output does not matter.

'''

from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group_to_anagram = defaultdict(list)
        for word in strs:
            group_to_anagram["".join(sorted(word))].append(word)
        return group_to_anagram.values()
    
from itertools import groupby
class Solution:
    def groupAnagrams(self, strs):
        groups = itertools.groupby(sorted(strs, key=sorted), sorted)
        return [list(members) for _, members in groups]
        

from collections import defaultdict, Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for word in strs:
            base = ['0'] * 26
            count = Counter(word)
            for key in count:
                base[ord(key) - ord('a')] = str(count[key])
            d["".join(base)].append(word)
        return d.values()