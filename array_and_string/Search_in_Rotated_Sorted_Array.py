'''
link: https://leetcode.com/problems/search-in-rotated-sorted-array/
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n).

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
'''


from typing import List
from bisect import bisect_left


class Solution:
    def find_pivot(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while r - l > 1:
            m = (l + r) // 2
            if nums[m] > nums[l]: l = m
            if nums[m] < nums[r]: r = m
        return l if r > 0 and nums[l] > nums[r] else -1
    
    def search(self, nums: List[int], target: int) -> int:
        pivot = self.find_pivot(nums)
        array1, array2 = nums[:pivot+1], nums[pivot+1:]
        max1 = array1[-1] if array1 else float('inf')
        max2 = array2[-1] if array2 else float('inf')
        if max2 and max1 > max2 and max2 >= target:
            i = bisect_left(array2, target)
            return i + pivot + 1 if i + pivot + 1 < len(nums) and nums[i + pivot + 1] == target else -1
        else:
            i = bisect_left(array1, target)
            return i if nums and i < len(nums) and nums[i] == target else -1