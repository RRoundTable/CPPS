'''
link: https://leetcode.com/problems/minimum-increment-to-make-array-unique/
Given an array of integers A, a move consists of choosing any A[i], and incrementing it by 1.

Return the least number of moves to make every value in A unique.

 

Example 1:

Input: [1,2,2]
Output: 1
Explanation:  After 1 move, the array could be [1, 2, 3].
Example 2:

Input: [3,2,1,2,1,7]
Output: 6
Explanation:  After 6 moves, the array could be [3, 4, 1, 2, 5, 7].
It can be shown with 5 or less moves that it is impossible for the array to have all unique values.
 

Note:

0 <= A.length <= 40000
0 <= A[i] < 40000
'''


from collections import Counter, deque


class Solution:
    '''O(N)/O(N)'''
    def minIncrementForUnique(self, A: List[int]) -> int:
        count, queue, ans, k = Counter(A), deque([]), 0, 0
        while count or queue:
            if count.get(k, 0) > 1: queue += [k] * (count[k] - 1)
            if count.get(k, 0) == 0 and queue: ans += k - queue.popleft()
            if k in count: count.pop(k)
            k += 1
        return ans


class Solution:
    '''O(NlogN)/O(1)'''
    def minIncrementForUnique(self, A: List[int]) -> int:
        tobe = ans = 0
        for ele in sorted(A):
            ans += max(tobe-ele, 0)
            tobe = max(tobe + 1, ele + 1)
        return ans
    
class Solution:
    '''O(NlogK)/O(N)'''
    def minIncrementForUnique(self, A: List[int]) -> int:
        tobe = ans = 0
        count = Counter(A)
        for ele in sorted(count):
            ans += count[ele] * max(tobe - ele, 0) + count[ele] * (count[ele] - 1) / 2
            tobe = max(tobe, ele) + count[ele]
        return int(ans)
    
class Solution:
    '''O(NlogK)/O(N)'''
    def minIncrementForUnique(self, A: List[int]) -> int:
        tobe = ans = 0
        count = Counter(A)
        for ele in sorted(count):
            ans += count[ele] * max(tobe - ele, 0) + count[ele] * (count[ele] - 1) / 2
            tobe = max(tobe, ele) + count[ele]
        return int(ans)
    
    
class Solution:
    '''O(N)/O(N)'''
    def minIncrementForUnique(self, A: List[int]) -> int:
        checked = {}
        def find(x):
            checked[x] = find(checked[x] + 1) if x in checked else x
            return checked[x]
        return sum(find(a) - a for a in A)