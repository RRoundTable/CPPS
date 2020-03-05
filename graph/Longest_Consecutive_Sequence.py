'''
link: https://leetcode.com/problems/longest-consecutive-sequence/

Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

Your algorithm should run in O(n) complexity.

Example:

Input: [100, 4, 200, 1, 3, 2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
'''

from collections import Counter

class Solution:
    '''O(NlogN)/O(N)'''
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = sorted(nums)
        ans, stack = 0, []
        for i in range(len(nums)):
            if not stack or stack[-1]+1 == nums[i]: stack.append(nums[i])
            elif stack[-1] == nums[i]: continue
            else: ans, stack = max(ans, len(stack)), [nums[i]]
        return max(ans, len(stack))
        
class Solution:
    '''O(NlogN)/O(N)'''
    def longestConsecutive(self, nums: List[int]) -> int:
        s, edges = set([ele for ele in nums]), {}
    
        for ele in nums:
            if ele + 1 in s: edges[ele] = ele + 1
        u = {ele: ele for i, ele in enumerate(nums)}

        def union(a, b):
            a, b = find(a), find(b)
            u[a] = b
        
        def find(a):
            if u[a] == a: return a
            u[a] = find(u[a])
            return u[a]
        
        for ele in nums:
            if edges.get(ele, float('inf')) < float('inf'):
                union(ele, edges[ele])
        
        for ele in nums:
            u[ele] = find(ele)
            
        return nums and max(Counter(u.values()).values()) or 0


class Solution:
    '''O(N)/O(N)'''
    def longestConsecutive(self, nums: List[int]) -> int:
        s, ans, c = set(nums), 0, 0
        for ele in nums:
            if ele - 1 not in s:
                c = 1
                while ele + 1 in s:
                    ele, c = ele + 1, c + 1
            ans = max(ans, c)
        return ans