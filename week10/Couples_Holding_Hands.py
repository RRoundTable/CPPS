'''
link: https://leetcode.com/problems/couples-holding-hands/
N couples sit in 2N seats arranged in a row and want to hold hands. We want to know the minimum number of swaps so that every couple is sitting side by side. A swap consists of choosing any two people, then they stand up and switch seats.

The people and seats are represented by an integer from 0 to 2N-1, the couples are numbered in order, the first couple being (0, 1), the second couple being (2, 3), and so on with the last couple being (2N-2, 2N-1).

The couples' initial seating is given by row[i] being the value of the person who is initially sitting in the i-th seat.

Example 1:

Input: row = [0, 2, 1, 3]
Output: 1
Explanation: We only need to swap the second (row[1]) and third (row[2]) person.
Example 2:

Input: row = [3, 2, 0, 1]
Output: 0
Explanation: All couples are already seated side by side.
Note:

len(row) is even and in the range of [4, 60].
row is guaranteed to be a permutation of 0...len(row)-1.

'''
class Solution:
    def minSwapsCouples(self, row: List[int]) -> int:
        '''
        greedy solution
        O(N)/O(N)
        '''
        place, swap = {x:i for i, x in enumerate(row)}, 0
        for i in range(0 , len(row), 2):
            if row[i] % 2 == 0:
                y = row[i] + 1
            else:
                y = row[i] - 1
            i, j = place[row[i]], place[y]
            if abs(i-j) > 1:
                row[i+1], row[j] = row[j], row[i+1]
                place[row[j]] = j
                place[row[i+1]] = i + 1
                swap += 1
        return swap
    
from collections import Counter
class Solution:
    def minSwapsCouples(self, row: List[int]) -> int:
        '''
        union find
        '''
        couple, edges, graph, n = {}, {}, [], len(row)
        
        for i in range(0, n, 2):       
            couple[(i, i + 1)] = i // 2
            edges[i], edges[i+1] = (i, i + 1), (i, i + 1)
        
        for i in range(0, n, 2):
            x = row[i]
            a = (x, x + 1) if x % 2 ==0 else (x - 1, x)
            b = edges[row[i+1]]
            if a == b:
                continue
            graph.append([couple[a], couple[b]])
                
        def find(x):
            while x != union[x]:
                x = union[x]
            return x
        
        union = list(range(n // 2))
        for u, v in graph:
            uu, uv = find(u), find(v)
            union[uu], union[uv] = min(uu, uv), min(uu, uv)
        union = [find(u) for u in union]
        c = Counter(union)
        
        return sum(c.values()) - len(set(union))