'''
link: https://leetcode.com/problems/next-permutation/
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place and use only constant extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.

1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1
'''

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def reverse(idx):
            start, end = idx, len(nums) - 1
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start, end = start + 1, end - 1

        for i in range(len(nums)-1, 0, -1):
            if nums[i] > nums[i-1]:
                j = len(nums) - 1
                while j > i - 1:
                    if nums[j] > nums[i-1]: break
                    j -= 1
                nums[i-1], nums[j] = nums[j], nums[i-1]
                reverse(i); return
        reverse(0)