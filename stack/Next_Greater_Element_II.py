'''
link: https://leetcode.com/problems/next-greater-element-ii/

Given a circular array (the next element of the last element is the first element of the array), print the Next Greater Number for every element. The Next Greater Number of a number x is the first greater number to its traversing-order next in the array, which means you could search circularly to find its next greater number. If it doesn't exist, output -1 for this number.

Example 1:
Input: [1,2,1]
Output: [2,-1,2]
Explanation: The first 1's next greater number is 2; 
The number 2 can't find next greater number; 
The second 1's next greater number needs to search circularly, which is also 2.
Note: The length of given array won't exceed 10000.
'''

from collections import deque


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        
        ans, stack, n = [-1] * len(nums), [], len(nums)
        
        for i, ele in enumerate(nums):
            while stack and stack[-1][1] < ele:
                j, _ = stack.pop()
                ans[j] = ele
            stack.append((i, ele))

        for i in range(stack[-1][0] if stack else 0):
            while stack and nums[i] > stack[-1][1]:
                j, _ = stack.pop()
                ans[j] = nums[i]
        return ans