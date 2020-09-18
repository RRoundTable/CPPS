'''
link: https://leetcode.com/problems/majority-element/
Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.

Example 1:

Input: [3,2,3]
Output: 3
Example 2:

Input: [2,2,1,1,1,2,2]
Output: 2
'''
from collections import Counter


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = Counter(nums)
        return max(count, key=lambda x: count[x])
        
    
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        major, count = nums[0], 0
        for i in range(len(nums)):
            if count == 0: major = nums[i]
            if nums[i] == major:
                count += 1
            else:
                count -= 1
        return major