'''
link: https://leetcode.com/problems/subsets/
Given a set of distinct integers, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
'''

from itertools import combinations


class Solution:
    def __init__(self):
        self.ans = set()
        self.d = {}

    def subsets(self, nums: List[int]) -> List[List[int]]:
        '''Combinations'''
        if self.d.get(tuple(nums), False): return self.d[tuple(nums)]
        self.ans.add(tuple(nums))
        if not nums: return []
        for comb in combinations(nums, len(nums) - 1):
            self.ans = self.ans | set(self.subsets(comb))
        self.d[tuple(nums)] = self.ans
        return self.ans
    
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        '''combinations'''
        ans, depth = [[]], 1
        while depth <= len(nums):
            ans, depth = ans + list(combinations(nums, depth)), depth + 1
        return ans 

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        '''One-line'''
        return map(list, [ele for d in range(0, len(nums) + 1) for ele in combinations(nums, d)])


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        output = [[]]
        for num in nums:
            output += [curr + [num] for curr in output]
        return output

    
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans, N = [], len(nums)
        def backtrack(first = 0, curr = []):
            if first == N + 1: return
            ans.append(curr)
            for i in range(first, N):
                backtrack(i + 1, curr + [nums[i]])
        backtrack(0, [])
        return ans
    
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans, N = [], len(nums)
        for i in range(2 ** N, 2 ** (N+1)):
            bitmask = bin(i)[3:]
            ans.append([nums[i] for i, b in enumerate(bitmask) if b == '1'])
        return ans