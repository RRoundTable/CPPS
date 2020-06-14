'''
link: https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
'''

from bisect import bisect_left, bisect_right

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        ans = [bisect_left(nums, target), bisect_right(nums, target) - 1]
        return ans if nums and ans[0] < len(nums) and target == nums[ans[0]] else [-1, -1]
    
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        def search(nums, target, left):
            lo = 0; hi = len(nums)
            while lo < hi:
                mid = (lo + hi) // 2
                if nums[mid] > target or (left and nums[mid] == target):
                    hi = mid
                else:
                    lo = mid + 1
            return lo
        
        left_idx = search(nums, target, True)
        
        if left_idx == len(nums) or (left_idx < len(nums) and nums[left_idx] != target):
            return [-1, -1]
        
        
        return [left_idx, search(nums, target, False) - 1]
        
        
        