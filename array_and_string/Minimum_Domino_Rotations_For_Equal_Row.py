'''
link: https://leetcode.com/problems/minimum-domino-rotations-for-equal-row/
In a row of dominoes, A[i] and B[i] represent the top and bottom halves of the i-th domino.  (A domino is a tile with two numbers from 1 to 6 - one on each half of the tile.)

We may rotate the i-th domino, so that A[i] and B[i] swap values.

Return the minimum number of rotations so that all the values in A are the same, or all the values in B are the same.

If it cannot be done, return -1.

 

Example 1:



Input: A = [2,1,2,4,2,2], B = [5,2,6,2,3,2]
Output: 2
Explanation: 
The first figure represents the dominoes as given by A and B: before we do any rotations.
If we rotate the second and fourth dominoes, we can make every value in the top row equal to 2, as indicated by the second figure.
Example 2:

Input: A = [3,5,1,2,3], B = [3,6,3,3,4]
Output: -1
Explanation: 
In this case, it is not possible to rotate the dominoes to make one row of values equal.

'''


class Solution(object):
    def minDominoRotations(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        self.ans, n = float('inf'), len(A)
        def backtrack(idx, prev, line, swap):
            if idx == n - 1:
                self.ans = min(self.ans, swap)
                return
            if prev is None:
                backtrack(idx + 1, A[idx + 1], 'A', 0)
                backtrack(idx + 1, B[idx + 1], 'B', 0)
            else:
                if line == 'A' and A[idx + 1] == prev:
                    backtrack(idx + 1, prev, 'A', swap)
                if line == 'A' and B[idx + 1] == prev:
                    backtrack(idx + 1, prev, 'A', swap + 1)
                if line == 'B' and B[idx + 1] == prev:
                    backtrack(idx + 1, prev, 'B', swap)
                if line == 'B' and A[idx + 1] == prev:
                    backtrack(idx + 1, prev, 'B', swap + 1)
                    
        backtrack(-1, None, None, 0)
        return self.ans if self.ans != float('inf') else - 1
    
class Solution(object):
    def minDominoRotations(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        a, b, n, ca, cb = A[0], B[0], len(A), float('inf'), float('inf')
        c = 0
        for i in range(n):
            if A[i] != a and B[i] != a: break;
            if A[i] != a and B[i] == a: c += 1;
        
        ca = min(c, ca) if i == n - 1 else ca
        c = 0
        for j in range(n):
            if B[j] != b and A[j] != b: break;
            if B[j] != b and A[j] == b: c += 1;
        cb = min(c, cb) if j == n - 1 else cb
        
        c = 0
        for i in range(n):
            if A[i] != b and B[i] != b: break;
            if A[i] != b and B[i] == b: c += 1;
        ca = min(ca, c) if j == n - 1 else ca
        
        c = 0
        for j in range(n):
            if B[j] != a and A[j] != a: break;
            if B[j] != a and A[j] == a: c += 1;
        cb = min(c, cb) if j == n - 1 else cb
        
        return min(ca, cb) if min(ca, cb) < float('inf') else - 1
        
class Solution(object):
    def minDominoRotations(self, A, B):
        """O(N)/O(1)
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        def is_possible(A, B, cand):
            c = 0
            for i in range(len(A)):
                if A[i] != cand and B[i] != cand: break;
                if A[i] != cand and B[i] == cand: c += 1;
            return c if i == len(A) - 1 else float('inf')
        
        c1, c2, c3, c4 = is_possible(A, B, A[0]), is_possible(A, B, B[0]), is_possible(B, A, A[0]), is_possible(B, A, B[0])
        return min(c1, c2, c3, c4) if min(c1, c2, c3, c4) != float('inf') else -1
