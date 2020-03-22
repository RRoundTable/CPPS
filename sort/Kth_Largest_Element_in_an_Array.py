'''
link: https://leetcode.com/problems/kth-largest-element-in-an-array/

Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.

Example 1:

Input: [3,2,1,5,6,4] and k = 2
Output: 5
Example 2:

Input: [3,2,3,1,2,4,5,5,6] and k = 4
Output: 4
Note:
You may assume k is always valid, 1 ≤ k ≤ array's length.
'''

from heapq import nlargest, heappop, heappush, heapify
import random


class Solution:
    '''O(NlogN)/O(1)'''
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return sorted(nums, reverse=True)[k-1]
        
        
class Solution:
    '''
    Heap
    O(Nlogk)/O(k)'''
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return nlargest(k, nums)[-1]
        
        
class Solution:
    '''
    Heap
    O(Nlogk)/O(k)'''
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for ele in nums:
            heappush(heap, ele)
            if len(heap) > k: heappop(heap)
        return heappop(heap)
    
    
class Solution:
    '''
    Quick Select
    avg O(N)/O(1) worst O(N^2)/O(1)'''
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        def partition(p, r, pivot_idx):
            pivot = nums[pivot_idx]; i = p
            nums[r], nums[pivot_idx] = nums[pivot_idx], nums[r]
            for j in range(p, r):
                if nums[j] <= pivot:
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1
            nums[i], nums[r] = nums[r], nums[i]
            return i
        
        def select(left, right, k_smallest):
            if left == right: return nums[left]
            pivot_idx = random.randint(left, right)
            pivot_idx = partition(left, right, pivot_idx)
            if k_smallest == pivot_idx: return nums[pivot_idx]
            elif k_smallest < pivot_idx:
                return select(left, pivot_idx - 1, k_smallest)
            else:
                return select(pivot_idx + 1, right, k_smallest)

        return select(0, len(nums)-1, len(nums) - k)
       