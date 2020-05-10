'''
link: https://leetcode.com/problems/knight-dialer/
A chess knight can move as indicated in the chess diagram below:

 .           

 

This time, we place our chess knight on any numbered key of a phone pad (indicated above), and the knight makes N-1 hops.  Each hop must be from one key to another numbered key.

Each time it lands on a key (including the initial placement of the knight), it presses the number of that key, pressing N digits total.

How many distinct numbers can you dial in this manner?

Since the answer may be large, output the answer modulo 10^9 + 7.

 

Example 1:

Input: 1
Output: 10
Example 2:

Input: 2
Output: 20
Example 3:

Input: 3
Output: 46
 

Note:

1 <= N <= 5000
'''

# {1:2, 2:2, 3:2, 4:3, 5:0, 6:3, 7:2, 8:2, 9:2, 0:2}
class Solution:
    '''O(N)/O(1)'''
    def knightDialer(self, N: int) -> int:
        d = [{i:1 for i in range(10)}, {i:1 for i in range(10)}]
        dire = {
            1:[6, 8],
            2:[7, 9], 
            3:[4, 8], 
            4:[3, 9, 0],
            5:[],
            6:[1, 7, 0],
            7:[2, 6],
            8:[1, 3],
            9:[2, 4],
            0:[4, 6]
        }
        for i in range(1, N):
            for j in range(10):
                curr = 0
                for next_ in dire[j]:
                    curr += d[0][next_]
                d[1][j] = curr
            d = [d[1], {i:1 for i in range(10)}]
            
        return sum(d[0].values()) % (10**9 + 7)
        