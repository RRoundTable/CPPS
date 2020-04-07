'''
link: https://leetcode.com/problems/3sum/
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
'''
from collections import Counter, defaultdict
from typing import List


class Solution1:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        '''O(N^2)/O(N)'''
        count, ans = Counter(nums), set()
        for k in count.keys():
            count[k] -= 1
            target = -k
            for k in count.keys():
                if count[k] <= 0: continue
                if count[target -k] > 0 and count[k] > 0 and target - k != k:
                    ans.add(tuple(sorted((-target, target - k, k))))
                if count[target -k] > 1 and target - k == k:
                    ans.add(tuple(sorted((-target, k, k))))
            count[-target] += 1  
        return map(list, ans)
    
class Solution2(object):
    def threeSum(self, nums):
        '''O(N^2)/O(1)'''
        nums.sort()
        n, ans = len(nums), set()
        for i in range(n):
            left, right = i + 1, n - 1
            while left < right:
                s = nums[i] + nums[left] + nums[right]
                if s == 0:
                    ans.add((nums[i], nums[left], nums[right]))
                    left += 1; right -= 1
                    while left < n and nums[left-1] == nums[left]: left += 1
                    while right > left and nums[right + 1] == nums[right]: right -= 1
                if s < 0: left += 1
                if s > 0: right -= 1
        return ans if n >= 3 else []


class Solution:
    '''
    Hash Map   
    O(N ^ 2)/O(N)'''
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = set(); nums.sort()
        for i in range(len(nums)-2):
            h, target = {}, nums[i]
            for j in range(i+1, len(nums)):
                if nums[j] not in h:
                    h[-target - nums[j]] = 1
                else:
                    ans.add((target, -target-nums[j], nums[j]))
        return map(list, list(ans))