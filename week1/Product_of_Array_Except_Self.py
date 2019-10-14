
'''
link: https://leetcode.com/problems/product-of-array-except-self/

Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Example:

Input:  [1,2,3,4]
Output: [24,12,8,6]
Note: Please solve it without division and in O(n).

Follow up:
Could you solve it with constant space complexity? (The output array does not count as extra space for the purpose of space complexity analysis.)


- time complexity: O(N)
- space complexity: O(1) (The output array does not count as extra space for the purpose of space complexity analysis.)
'''
from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:        
        answers = [1] * len(nums)
        # right-side
        for i in range(1, len(nums)):
            answers[i] = answers[i-1] * nums[i-1]
        
        # left-side
        rightside = nums[-1]
        for i in range(len(nums)-2, -1, -1):
            answers[i] = rightside * answers[i]
            rightside *= nums[i]
        
        return answers