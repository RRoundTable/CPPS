'''
link: https://leetcode.com/problems/partition-equal-subset-sum/

Given a non-empty array containing only positive integers, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.

Note:

Each of the array element will not exceed 100.
The array size will not exceed 200.
 

Example 1:

Input: [1, 5, 11, 5]

Output: true

Explanation: The array can be partitioned as [1, 5, 5] and [11].
 

Example 2:

Input: [1, 2, 3, 5]

Output: false

Explanation: The array cannot be partitioned into equal sum subsets.
'''

from collections import Counter, defaultdict

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target = sum(nums) / 2
        memo = {}
        def search(target, i):
            if memo.get((target, i), -1) != -1: return memo[target, i]
            if target < 0: return False
            if target == 0: return True
            if i < len(nums) and (search(target - nums[i], i + 1) or search(target, i + 1)):
                memo[target, i] = True
                return True
            memo[target, i] = False
            return False
        return search(target, 0)
        