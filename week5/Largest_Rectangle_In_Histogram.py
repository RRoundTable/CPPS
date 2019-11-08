"""
link: https://leetcode.com/problems/largest-rectangle-in-histogram/

Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, find the area of largest rectangle in the histogram.



Above is a histogram where width of each bar is 1, given height = [2,1,5,6,2,3].

 


The largest rectangle is shown in the shaded area, which has area = 10 unit.

 

Example:

Input: [2,1,5,6,2,3]
Output: 10
"""


class Solution1(object):
    def largestRectangleArea(self, heights):
        """O(N)/O(N)
        :type heights: List[int]
        :rtype: int
        """
        if not heights:
            return 0

        left_lower = [0] * len(heights)
        right_lower = [0] * len(heights)

        left_lower[0] = -1
        right_lower[-1] = len(heights)

        # dynamic programing
        for i in range(1, len(heights)):
            p = i - 1
            while p >= 0 and heights[p] >= heights[i]:
                p = left_lower[p]
            left_lower[i] = p

        for i in range(len(heights) - 2, -1, -1):
            p = i + 1
            while p < len(heights) and heights[p] >= heights[i]:
                p = right_lower[p]
            right_lower[i] = p

        maxArea = 0
        for i in range(len(heights)):
            maxArea = max(maxArea, heights[i] * (right_lower[i] - left_lower[i] - 1))
        return maxArea


class Solution2(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        stack = [-1]
        heights.append(0)
        ans = 0
        for i in range(len(heights)):
            while heights[i] < heights[stack[-1]]:
                h = heights[stack.pop(-1)]
                w = i - stack[-1] - 1
                ans = max(ans, h * w)
            stack.append(i)
        return ans