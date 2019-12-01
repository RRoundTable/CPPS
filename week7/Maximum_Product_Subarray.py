'''
link: https://leetcode.com/problems/maximum-product-subarray/
Given an integer array nums, find the contiguous subarray within an array (containing at least one number) which has the largest product.

Example 1:

Input: [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
Example 2:

Input: [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
'''

class Solution(object):
    def maxProduct(self, nums):
        """O(N) / O(N)
        :type nums: List[int]
        :rtype: int
        """
        dp = [0 , 0]
        for i in range(len(nums)):
            if i == 0: dp[i] = [nums[i], nums[i]]
            else:
                dp[i] = [max(dp[i-1][0] *nums[i], dp[i-1][1] * nums[i], nums[i]), min(dp[i-1][0] *nums[i], dp[i-1][1] * nums[i], nums[i])]
                
        return len(nums) and max(map(max, dp))
    
    
class Solution(object):
    def maxProduct(self, nums):
        """O(N) / O(N)
        :type nums: List[int]
        :rtype: int
        """
        dp, ans = [0 , 0], -sys.maxsize
        for i in range(len(nums)):
            if i == 0: dp = [nums[i], nums[i]]
            else:
                dp = [max(dp[0] *nums[i], dp[1] * nums[i], nums[i]), min(dp[0] *nums[i], dp[1] * nums[i], nums[i])]
            ans = max(ans, dp[0])
        return len(nums) and ans