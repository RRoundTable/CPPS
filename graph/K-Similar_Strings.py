'''
link: https://leetcode.com/problems/k-similar-strings/
Strings A and B are K-similar (for some non-negative integer K) if we can swap the positions of two letters in A exactly K times so that the resulting string equals B.

Given two anagrams A and B, return the smallest K for which A and B are K-similar.

Example 1:

Input: A = "ab", B = "ba"
Output: 1
Example 2:

Input: A = "abc", B = "bca"
Output: 2
Example 3:

Input: A = "abac", B = "baca"
Output: 2
Example 4:

Input: A = "aabc", B = "abca"
Output: 2
Note:

1 <= A.length == B.length <= 20
A and B contain only lowercase letters from the set {'a', 'b', 'c', 'd', 'e', 'f'}
'''
from collections import deque

class Solution:
    '''O(2^(N+W))/O(2^(N+W))'''
    def kSimilarity(self, A: str, B: str) -> int:
        memo = {B:0}

        def swap(i, j):
            nonlocal A
            a, b = A[i], A[j]  
            A = A[:i] + b + A[i+1:]
            A = A[:j] + a + A[j+1:]
            
        def dfs(i):
            nonlocal A; pre = A
            if memo.get(pre, -1) >= 0: return memo[pre]
            while i < len(A) and A[i] == B[i]:
                i += 1
            memo[pre] = float('inf')
            for j in range(i + 1, len(A)):
                if B[i] != A[j]: continue
                swap(i, j)
                memo[pre] = min(dfs(i+1) + 1, memo[pre])
                swap(i, j)
            return memo[pre]
        return dfs(0)


class Solution:
    def kSimilarity(self, A: str, B: str) -> int:
        queue, seen = deque([A]), {A: 0}
        
        def swap(A, i, j):
            a, b = A[i], A[j]  
            A = A[:i] + b + A[i+1:]
            A = A[:j] + a + A[j+1:]
            return A
        
        def neighbor(A):        
            for i in range(len(A)):
                if A[i] != B[i] : break
            for j in range(i+1, len(A)):
                A = swap(A, i, j)
                yield A
                A = swap(A, i, j)
        
        while queue:
            state = queue.popleft()
            if state == B: return seen[state]
            for ne in neighbor(state):
                if ne not in seen:
                    seen[ne] = seen[state] + 1
                    queue.append(ne)
        return seen[B]