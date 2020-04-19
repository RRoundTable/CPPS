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

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n1, n2, nums, j, k = len(nums1), len(nums2), [], 0, 0
        for i in range(n1 + n2):
            if j == n1: 
                nums += nums2[k:]; break
            if k == n2:
                nums += nums1[j:]; break
            if nums1[j] < nums2[k]:
                nums.append(nums1[j]); j += 1
            else:
                nums.append(nums2[k]); k += 1
        
        return nums[(n1 + n2) // 2] if (n1 + n2) % 2 == 1 else (nums[(n1+n2)//2 -1] + nums[(n1+n2)//2])/2
        
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        a, b = sorted((nums1, nums2), key=len)
        m, n = len(a), len(b)
        if not a: 
            return (b[n//2] + b[n//2 - int((m+n)%2 == 0)]) / 2.0
        after = (m + n - 1) // 2
        io, hi = 0, after
        while io < hi:
            i = (io + hi) // 2
            if after - i - 1 < 0 or i >= m or a[i] >= b[after-i-1]:
                hi = i
            else:
                io = i + 1
        i = io
        nextfew = sorted(a[i:i+2] + b[after-i:after-i+2])
        return (nextfew[0] + nextfew[1 - (m+n)%2]) /2.0