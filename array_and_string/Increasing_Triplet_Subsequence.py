'''
link: https://leetcode.com/problems/increasing-triplet-subsequence/

Given an unsorted array return whether an increasing subsequence of length 3 exists or not in the array.

Formally the function should:

Return true if there exists i, j, k
such that arr[i] < arr[j] < arr[k] given 0 ≤ i < j < k ≤ n-1 else return false.
Note: Your algorithm should run in O(n) time complexity and O(1) space complexity.

Example 1:

Input: [1,2,3,4,5]
Output: true
Example 2:

Input: [5,4,3,2,1]
Output: false
'''

import bisect


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        triple = [float('inf'), float('inf')]
        for ele in nums:
            i = bisect.bisect_left(triple, ele)
            if i >= 2: return True
            triple[i] = ele
        return False