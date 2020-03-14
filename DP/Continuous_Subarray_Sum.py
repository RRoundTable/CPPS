'''
link: https://leetcode.com/problems/continuous-subarray-sum/
Given a list of non-negative numbers and a target integer k, write a function to check if the array has a continuous subarray of size at least 2 that sums up to a multiple of k, that is, sums up to n*k where n is also an integer.

 

Example 1:

Input: [23, 2, 4, 6, 7],  k=6
Output: True
Explanation: Because [2, 4] is a continuous subarray of size 2 and sums up to 6.
Example 2:

Input: [23, 2, 6, 4, 7],  k=6
Output: True
Explanation: Because [23, 2, 6, 4, 7] is an continuous subarray of size 5 and sums up to 42.
 

Note:

The length of the array won't exceed 10,000.
You may assume the sum of all the numbers is in the range of a signed 32-bit integer.

'''


class Solution:
    '''O(N^2)/O(1)'''
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        for i in range(len(nums)):
            s = nums[i]
            for j in range(i+1, len(nums)):
                s += nums[j]
                if (k and s % k == 0) or (k == 0 and s == 0): return True
        return False
    
class Solution:
    '''Math and Hash
    O(N)/O(N)'''
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        mod, s = {}, 0
        for i, n in enumerate(nums):
            if i < len(nums) - 1 and nums[i] == 0 and nums[i+1] == 0: return True
            s += n
            if i and k and s % k in mod and mod[s%k] < i - 1 or (i and k and s%k == 0): return True
            if k and s%k not in mod: mod[s%k] = i
        return len(nums) >=2 and False
        