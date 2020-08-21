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
        print(sorted(strs))
        groups = itertools.groupby(sorted(strs, key=sorted), sorted)
        return [list(members) for _, members in groups]
        