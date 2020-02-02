/*
link: https://leetcode.com/problems/trapping-rain-water/
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.


The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped. Thanks Marcos for contributing this image!

Example:

Input: [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
*/

#include <iostream>
#include <stack>

class Solution {
public:
    int trap(vector<int>& height) {
        stack<int> s;
        int ans = 0;
        int top = 0;
        int dist = 0;
        int h = 0;
        for (int i = 0; i < height.size(); i++){
            while (not s.empty() and height[i] > height[s.top()]){
                top = s.top();
                s.pop();
                if (s.empty()){
                    break;
                }
                dist = i - s.top() - 1;
                h = min(height[i], height[s.top()]);
                ans += (h - height[top]) * dist;
            }
            s.push(i);
        }
    return ans;    
    }
};