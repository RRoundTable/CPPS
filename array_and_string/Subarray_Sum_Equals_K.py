'''
link: https://leetcode.com/problems/subarray-sum-equals-k/
Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.

Example 1:
Input:nums = [1,1,1], k = 2
Output: 2
Note:
The length of the array is in range [1, 20,000].
The range of numbers in the array is [-1000, 1000] and the range of the integer k is [-1e7, 1e7].

'''

from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        '''O(N^2)/O(N^2)'''
        ans, d, n = 0, {}, len(nums)
        start, s = 0, 0
        for i in range(n):
            s += nums[i]
            d[(start, i)] = s
            if d[(start, i)] == k: ans +=1
                
        for start in range(1, n):
            for i in range(start, n):
                d[(start, i)] = d[(start - 1, i)] - nums[start - 1]
                if d[(start, i)] == k: ans +=1
        return ans
    
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        '''O(N^2)/O(N)'''
        ans, d, n = 0, [], len(nums)
        start, s = 0, 0
        for i in range(n):
            s += nums[i]
            d.append(s)
            if s == k: ans +=1
        for start in range(1, n):
            for i in range(start, n):
                d[i] = d[i] - nums[start - 1]
                if d[i] == k: ans +=1
        return ans
    
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        '''O(N^2)/O(N)'''
        ans, d, n = 0, [], len(nums)
        start, s = 0, 0
        for i in range(n):
            s += nums[i]
            d.append(s)
            for j in range(len(d) - 1):
                if d[-1] - d[j] == k: ans += 1;         
            if s == k: ans +=1
        return ans
    
from collections import Counter
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        '''O(N^2)/O(N)'''
        ans, d, n = 0, [], len(nums)
        start, s, abs_sum = 0, 0, 0
        for i in range(n):
            s += nums[i]
            abs_sum += abs(nums[i])
            d.append(s)
            if (k > s and s + abs_sum < k) or (k < s and s - abs_sum > k): continue
            for j in range(len(d) - 1):
                if d[-1] - d[j] == k: ans += 1;         
            if s == k: ans +=1
        return ans


class Solution(object):
     def subarraySum(self, nums, k):
        '''O(N^2)/O(1)'''
        ans, n = 0, len(nums)
        start, s = 0, 0
        for i in range(n):
            s = 0
            for j in range(i, n):
                s += nums[j]
                if s == k: ans += 1
        return ans
        
class Solution:
    def subarraySum(self, nums, k):
        '''O(N)/O(N)'''
        d = defaultdict(lambda: 0)
        d[0], s, ans = 1, 0, 0
        for ele in nums:
            s += ele
            ans += d[s - k]
            d[s] += 1
        return ans

    