"""
link: https://leetcode.com/problems/longest-string-chain/

Given a non-empty array of integers, return the k most frequent elements.

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
Note:

You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
"""

from collections import defaultdict
import copy
from typing import List


class Solution:

    def longestStrChain(self, words: List[str]) -> int:
        '''O()/()'''
        d = defaultdict(lambda: [])
        words = sorted(words, key=lambda x: len(x))

        # dict for length of words
        for i in range(len(words)):
            d[len(words[i])] += [words[i]]

        keys = list(d.keys())
        max_val = len(keys)

        def search(path=[], i=0, ans=0):
            if i >= max_val:
                return path, i, ans
            temp_i = i
            for ele in d[keys[i]]:
                i = temp_i
                if not path:
                    path.append(ele)
                    ans = max(ans, len(path))
                    path, i, ans = search(path, i + 1, ans)
                    path.pop(-1)
                else:
                    if self.check_possible(path[-1], ele):
                        path.append(ele)
                        ans = max(ans, len(path))
                        path, i, ans = search(path, i + 1, ans)
                        path.pop(-1)
            return path, i, ans

        result = 0
        for i in range(max_val):
            if max_val - i < result:
                break
            path, i, ans = search([], i, 0)
            result = max(result, ans)
        return result

    def check_possible(self, ele1, ele2):
        if len(ele1) != len(ele2) - 1:
            return False
        key1 = set(ele1)
        key2 = set(ele2)
        diff = list(key2 - key1)
        diff_inv = list(key1 - key2)
        if len(diff) == 0 and not diff_inv:
            j = 0
            for i in range(len(ele1)):
                if ele2[i + j] == ele1[i]:
                    continue
                else:
                    if ele2[i] in key1:
                        j += 1
                        if j > 1:
                            return False
                    else:
                        return False
            return True

        elif len(diff) == 1 and not diff_inv:
            j = 0
            for i in range(len(ele1)):
                if ele2[i + j] == ele1[i]:
                    continue
                else:
                    if ele2[i] in diff:
                        j += 1
                        if j > 1:
                            return False
                    else:
                        return False
            return True
        else:
            return False
