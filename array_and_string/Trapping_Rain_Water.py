'''
link: https://leetcode.com/problems/trapping-rain-water/
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.


The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped. Thanks Marcos for contributing this image!

Example:

Input: [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
'''

class Solution:
    def trap(self, height: List[int]) -> int:
        '''Brute-Force
        O(N^2)/O(1)
        '''
        left, right, ans, i = 0, 0, 0, 1
        for i in range(1, len(height)):
            left, right = max(height[j] for j in range(i)), max(height[j] for j in range(i, len(height)))
            ans, left, right = ans + max(min(left, right) - height[i], 0), 0, 0
        return ans

class Solution:
    def trap(self, height: List[int]) -> int:
        '''Dynamic programing: store max value
        O(N)/O(N)
        '''
        left, right, ans, i = [0] * len(height), [0] * len(height), 0, 1
        for i in range(1, len(height)):
            left[i] = max(left[i-1], height[i-1])
        for i in range(len(height)-2, -1, -1):
            right[i] = max(right[i+1], height[i+1])
        for i in range(1, len(height)):
            ans = ans + max(min(left[i], right[i]) - height[i], 0)
        return ans
    
class Solution:
    def trap(self, height: List[int]) -> int:
        '''Stack
        O(N)/O(N)
        '''
        s, ans, i = [], 0, 0
        while i < len(height):
            while s and height[s[-1]] < height[i]:
                top = s.pop()
                if not s: break
                dist = i - s[-1] - 1
                h = min(height[i], height[s[-1]]) - height[top]
                ans += dist * h
            s.append(i); i += 1
        return ans