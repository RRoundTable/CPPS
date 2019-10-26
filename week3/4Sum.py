"""
link: https://leetcode.com/problems/4sum/

Given an array nums of n integers and an integer target, are there elements a, b, c, and d in nums such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

Note:

The solution set must not contain duplicate quadruplets.

Example:

Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.

A solution set is:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]
"""
from collections import defaultdict
import copy
from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        '''O(N ^ 2)/ O(N)'''
        ans = []
        d1 = defaultdict(lambda: 0)
        for i in range(len(nums)):
            d1[nums[i]] += 1
        
        possible = self.possible(d1, target)
        for t1, t2 in possible:
            result, ele1 = self.twoSum(d1, t1)
            self.undo(d1, ele1)
            result, ele2 = self.twoSum(d1, t2)
            self.undo(d1, ele2)
            for e1 in ele1:
                d1[e1[0]] -= 1
                d1[e1[1]] -= 1
                for e2 in ele2:
                    d1[e2[0]] -= 1
                    d1[e2[1]] -= 1
                    if d1[e2[1]] < 0 or d1[e2[0]] < 0:
                        d1[e2[0]] += 1
                        d1[e2[1]] += 1
                        continue
                    else:
                        d1[e2[0]] += 1
                        d1[e2[1]] += 1
                        if sorted(e1 + e2) not in ans:
                            ans.append(sorted(e1 + e2))
                d1[e1[0]] += 1
                d1[e1[1]] += 1
        return ans    
        
    
    def possible(self, d1, target):
        result = set()
        keys = list(d1.keys())
        for k1 in keys:
            for k2 in keys:
                if k1 == k2:
                    if d1[k1] < 2:
                        continue
                result.add(k1 + k2)
        d = defaultdict(lambda: 0)
        possible = []
        for k in result:
            d[k] = target - k
        for k in result:
            if d[d[k]] == k:
                if [d[k], k] in possible:
                    continue
                possible.append([k, d[k]])
        return possible
        
    def twoSum(self, d1, target):
        '''O(N)/O(N)'''
        d2 = defaultdict(lambda:0)
        keys = list(d1)
        for k in keys:
            d2[k] = target - k
        result = False
        elements = []
        for k in keys:
            if d2[d2[k]] == k and d1[k] > 0 and d1[d2[k]] > 0:
                if k == d2[k] and d1[k] < 2:
                    continue
                d1[k] -= 1
                d1[d2[k]] -= 1
                elements.append([k, d2[k]])
                result = True
        return result, elements
    
    def undo(self, d1, ele):
        for k1, k2 in ele:
            d1[k1] += 1
            d1[k2] += 1
