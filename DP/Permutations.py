'''
link: https://leetcode.com/problems/permutations/
Given a collection of distinct integers, return all possible permutations.

Example:

Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
'''

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans, N = [], len(nums)
        def backtracking(remain, curr):
            if len(curr) == N: ans.append(curr); return
            for i in range(len(remain)):
                backtracking(remain[:i] + remain[i+1:], curr + [remain[i]])
        backtracking(nums, [])
        return ans
    
    
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        if not nums: return [[]]
        for p in self.permute(nums[1:]):
            temp = []
            for i in range(len(p)+1):
                temp.append(p[:i] + [nums[0]] + p[i:])
            ans += temp
        return ans or [[]]
    
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return nums and [p[:i] + [nums[0]] + p[i:]  for p in self.permute(nums[1:]) for i in range(len(p) + 1)] or [[]]
    
from functools import reduce
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return reduce(lambda P, n: [p[i:] + [n] + p[:i] for p in P for i in range(len(p) + 1)], nums, [[]])