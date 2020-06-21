'''
link: https://leetcode.com/problems/largest-number/
Given a list of non negative integers, arrange them such that they form the largest number.

Example 1:

Input: [10,2]
Output: "210"
Example 2:

Input: [3,30,34,5,9]
Output: "9534330"
Note: The result may be very large, so you need to return a string instead of an integer.
'''
class Larger(str):
    def __lt__(x, y):
        return x+y > y+x

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        
        nums = sorted(map(str, nums), key=Larger)
        
        return "".join(nums) if not all(ele == '0' for ele in nums) else '0'
