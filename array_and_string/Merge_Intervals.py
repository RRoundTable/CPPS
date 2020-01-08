'''
link: https://leetcode.com/problems/merge-intervals/
Given a collection of intervals, merge all overlapping intervals.

Example 1:

Input: [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
Example 2:

Input: [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
NOTE: input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.
'''

class Solution(object):
    def merge(self, intervals):
        """O(NlogN)/O(N)
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        if len(intervals) < 2: return intervals
        intervals, array = sorted(intervals, key=lambda x: x[1]), []
        for i, (l, r) in enumerate(intervals):
            array.append([l, i, 'left'])
            array.append([r, i, 'right'])
        d = {i: (l, r) for i, (l, r) in enumerate(intervals)}
        array, i, maxval, ans = sorted(array, key=lambda x: x[0]), 0, 0, []

        
        while i < len(array):
            if ans and ans[-1][1] == array[i][0]:
                left, _ = ans.pop()

            if i == 0 or left is None:
                left, maxval, i = array[i][0], max(maxval, d[array[i][1]][1]), i + 1
                continue            
            if array[i][2] == 'left':
                maxval, i = max(maxval, d[array[i][1]][1]), i + 1
            elif array[i][2] == 'right':
                if array[i][0] == maxval:
                    ans.append((left, maxval))    
                    left = None
                i += 1
        return ans