"""
link:https://leetcode.com/problems/combination-sum/
Given a set of candidate numbers (candidates) (without duplicates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

The same repeated number may be chosen from candidates unlimited number of times.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: candidates = [2,3,6,7], target = 7,
A solution set is:
[
  [7],
  [2,2,3]
]
Example 2:

Input: candidates = [2,3,5], target = 8,
A solution set is:
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]
"""

from collections import defaultdict


class Solution(object):
    def combinationSum(self, candidates, target):
        """O(N!)/O(N!)
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        self.ans = []

        def backtracking(remain, path):
            if remain < 0:
                return
            if remain == 0:
                path = sorted(path)
                if path not in self.ans:
                    self.ans.append(path)
                return
            for c in candidates:
                backtracking(remain - c, path + [c])

        backtracking(target, [])
        return self.ans


class Solution(object):
    def combinationSum(self, candidates, target):
        """O()
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        self.ans = []

        def backtracking(remain, path):
            if remain < 0:
                return
            if remain == 0:
                path = sorted(path)
                if path not in self.ans:
                    self.ans.append(path)
                return
            for c in candidates:
                backtracking(remain - c, path + [c])

        backtracking(target, [])
        return self.ans


class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        def backtracking(remain, path):
            if remain == 0:
                ans.append(path)
            for c in candidates:
                if remain - c >= 0 and (not path or path[-1] <= c):
                    backtracking(remain - c, path + [c])

        ans, candidates = [], sorted(candidates)
        backtracking(target, [])
        return ans


class Solution(object):
    def combinationSum(self, candidates, target):
        """Dynamic Programming
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        dp = defaultdict(lambda: [])
        for c in candidates:
            for t in range(c, target + 1):
                if t == c:
                    dp[t].append([c])
                for ele in dp[t - c]:
                    dp[t].append(ele + [c])
        return dp[target]
