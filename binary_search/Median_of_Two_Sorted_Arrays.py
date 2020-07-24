'''
link: https://leetcode.com/problems/median-of-two-sorted-arrays/
There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

You may assume nums1 and nums2 cannot be both empty.

Example 1:

nums1 = [1, 3]
nums2 = [2]

The median is 2.0
Example 2:

nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5

'''

import math

class Solution:
    '''O(N)/O(N)'''
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = []
        i, j = 0, 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                nums.append(nums1[i]); i += 1
            else:
                nums.append(nums2[j]); j += 1
        nums += nums1[i:] + nums2[j:]
        
        if len(nums) % 2 == 0:
            return (nums[len(nums) // 2 - 1] + nums[len(`b  nums) // 2]) / 2
        else:
            return nums[math.floor(len(nums) / 2)]

from bisect import bisect_left

class Solution:
    '''O(logN)/O(1)'''
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1, nums2 = sorted([nums1, nums2], key=len)
        m, n = len(nums1), len(nums2)
        after = (m + n - 1) / 2
        lo, hi = 0, m
        while lo < hi:
            i = (lo + hi) / 2
            if after-i-1 < 0 or a[i] >= b[after-i-1]:
            hi = i
        else:
            lo = i + 1
    i = lo
    nextfew = sorted(a[i:i+2] + b[after-i:after-i+2])
    return (nextfew[0] + nextfew[1 - (m+n)%2]) / 2.0
        
        
        
                
                

        
        
        