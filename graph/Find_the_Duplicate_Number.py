'''
link: https://leetcode.com/problems/find-the-duplicate-number/
Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive), prove that at least one duplicate number must exist. Assume that there is only one duplicate number, find the duplicate one.

Example 1:

Input: [1,3,4,2,2]
Output: 2
Example 2:

Input: [3,1,3,4,2]
Output: 3
Note:

You must not modify the array (assume the array is read only).
You must use only constant, O(1) extra space.
Your runtime complexity should be less than O(n2).
There is only one duplicate number in the array, but it could be repeated more than once.

'''

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i == j: continue
                if nums[i] == nums[j]: return nums[i]

class Solution:
    """
    https://www.youtube.com/watch?v=X_kwcctaQ4M
    https://cs.stackexchange.com/questions/10360/floyds-cycle-detection-algorithm-determining-the-starting-point-of-cycle
    """
    def findDuplicate(self, nums: List[int]) -> int:
        
        a, b = 0, 0
        a = nums[nums[a]]; b = nums[b]
        while a != b:
            a = nums[nums[a]]; b = nums[b]
        b = 0
        while a != b:
            a = nums[a]; b = nums[b]
        return a
    
    
class Solution:
    """
    binary search
    """
    def findDuplicate(self, nums: List[int]) -> int:
        
        lo, hi = 0, len(nums) - 1
        while lo < hi:
            mid, count = (lo + hi) // 2, 0
            for ele in nums:
                if mid < ele <= hi:
                    count += 1
            if count > hi - mid:
                lo = mid + 1
            else:
                hi = mid
        return lo
        