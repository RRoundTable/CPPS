'''
link:https://leetcode.com/problems/trapping-rain-water/
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.


The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped. Thanks Marcos for contributing this image!

Example:

Input: [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
'''

class Solution {
    public int trap(int[] height) {
        
        int n = height.length;
        int ans = 0;
        int[] right = new int[n];
        int[] left = new int[n];
        
        for(int i = 1; i < n; i ++){
            left[i] = Math.max(left[i-1], height[i-1]);
        }
        
        for (int i = n - 2; i >= 0; i --){
            right[i] = Math.max(right[i+1], height[i+1]);
        }
        
        for(int i = 1; i < n; i ++){
            ans += Math.max(Math.min(left[i], right[i]) - height[i], 0);
        }
        
    return ans;
    }
}