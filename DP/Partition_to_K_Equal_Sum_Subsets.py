'''
link:https://leetcode.com/problems/partition-to-k-equal-sum-subsets/
Given an array of integers nums and a positive integer k, find whether it's possible to divide this array into k non-empty subsets whose sums are all equal.

 

Example 1:

Input: nums = [4, 3, 2, 3, 5, 2, 1], k = 4
Output: True
Explanation: It's possible to divide it into 4 subsets (5), (1, 4), (2,3), (2,3) with equal sums.
 

Note:

1 <= k <= len(nums) <= 16.
0 < nums[i] < 10000.
'''

class Solution:
    '''O(N * 2 ^ N)/O(2^N)'''
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        s = sum(nums)
        if s % k != 0 : return False
        target = [s / k] * k
        nums.sort(reverse=True)
        
        def dfs(pos):
            if pos == len(nums): return True
            for i in range(k):
                if target[i] >= nums[pos]:
                    target[i] -= nums[pos]
                    if dfs(pos + 1): return True
                    target[i] += nums[pos]
            return False
        return dfs(0)
    
    
class Solution:
    '''O(N * 2 ^ N)/O(2^N)'''
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        target, r = divmod(sum(nums), k)
        if r != 0 or max(nums) > target: return False
        memo = [None] * (1 << len(nums)); memo[-1] = True
       
        def dfs(used, todo):
            if memo[used] is None:
                targ = (todo - 1) % target + 1
                memo[used] = any(dfs(used | (1<<i), todo - num) 
                                for i, num in enumerate(nums)
                                if (used >> i) & 1 == 0 and num <= targ)
                
            return memo[used]
        return dfs(0, target * k)