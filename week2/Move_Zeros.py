'''
link: https://leetcode.com/problems/move-zeroes/

Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
Note:

You must do this in-place without making a copy of the array.
Minimize the total number of operations.
'''
from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        '''O(N)/O(1)'''
        i = 0
        while i < len(nums) - 1:
            if nums[i] == 0:
                nums[i:-1], nums[-1] = nums[i + 1:], nums[i]
                if nums[i:] == [0] * len(nums[i:]):
                    break
            else:
                i += 1