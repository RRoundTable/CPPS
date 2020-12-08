'''
link: https://leetcode.com/problems/pizza-with-3n-slices/
There is a pizza with 3n slices of varying size, you and your friends will take slices of pizza as follows:

You will pick any pizza slice.
Your friend Alice will pick next slice in anti clockwise direction of your pick. 
Your friend Bob will pick next slice in clockwise direction of your pick.
Repeat until there are no more slices of pizzas.
Sizes of Pizza slices is represented by circular array slices in clockwise direction.

Return the maximum possible sum of slice sizes which you can have.

 

Example 1:



Input: slices = [1,2,3,4,5,6]
Output: 10
Explanation: Pick pizza slice of size 4, Alice and Bob will pick slices with size 3 and 5 respectively. Then Pick slices with size 6, finally Alice and Bob will pick slice of size 2 and 1 respectively. Total = 4 + 6.
Example 2:



Input: slices = [8,9,8,6,1,1]
Output: 16
Output: Pick pizza slice of size 8 in each turn. If you pick slice with size 9 your partners will pick slices of size 8.
Example 3:

Input: slices = [4,1,2,5,8,3,1,9,7]
Output: 21
Example 4:

Input: slices = [3,1,2]
Output: 3
 

Constraints:

1 <= slices.length <= 500
slices.length % 3 == 0
1 <= slices[i] <= 1000

'''


class Node:
    def __init__(self, v):
        self.val = v
        self.next = None
        self.before = None


class Solution:
    def maxSizeSlices(self, slices: List[int]) -> int:
        memo, n = {}, len(slices)
        state = 1 << n
        
        node_to_idx = {}
        idx_to_node = {}
        head = node = Node(0)
        node_to_idx[node] = 0
        idx_to_node[0] = node
        
        for i in range(1, n):            
            next_node = Node(i)
            node.next, next_node.before = next_node, node
            node = node.next
            node_to_idx[node] = i
            idx_to_node[i] = node
            
        node.next, head.before = head, node
        def solve(state):
            nonlocal slices, memo, n, idx_to_node
            if state in memo:
                return memo[state]
            res = 0
            for i in range(n):
                if state & (1 << i) != 0:
                    continue
                curr = idx_to_node[i]
                bob, alice = curr.before, curr.next
                bob.before.next, alice.next.before = alice.next, bob.before
                next_state = state | (1 << i) | (1 << bob.val) | (1 << alice.val)
                res = max(res, solve(next_state) + slices[i])
                bob.before.next, alice.next.before = bob, alice
            memo[state] = res
            return memo[state]                
        
        return solve(state)
    
    
class Solution:
    def maxSizeSlices(self, slices: List[int]) -> int:
        n = len(slices)
        dp1 = [[0] * n for _ in range(n//3 + 1)]
        dp2 = [[0] * n for _ in range(n//3 + 1)]
        
        for i in range(1, n // 3 + 1):
            for j in range(1, n):
                if j == 1:
                    dp1[i][j] = slices[j-1]
                    dp2[i][j] = slices[j]
                    continue
                dp1[i][j] = max(dp1[i-1][j-2] + slices[j-1], dp1[i][j-1])
                dp2[i][j] = max(dp2[i-1][j-2] + slices[j], dp2[i][j-1]) 
        
        return max(dp1[-1][-1], dp2[-1][-1])
 