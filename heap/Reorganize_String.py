'''
link: https://leetcode.com/problems/reorganize-string/

Given a string S, check if the letters can be rearranged so that two characters that are adjacent to each other are not the same.

If possible, output any possible result.  If not possible, return the empty string.

Example 1:

Input: S = "aab"
Output: "aba"
Example 2:

Input: S = "aaab"
Output: ""
Note:

S will consist of lowercase letters and have length in range [1, 500].

'''

from collections import Counter
from heapq import heappop, heappush, heapify

class Solution:
    def reorganizeString(self, s: str) -> str:
        count, ans = Counter(s), ""
        items = [[-count[k], k] for k in count.keys()]
        heapify(items)

        tries = []
        while items:
            pop = heappop(items)
            if not ans or ans[-1] != pop[1]:
                ans += pop[1]
                pop[0] += 1
                while tries:
                    heappush(items, tries.pop())
                if pop[0] < 0: heappush(items, pop)
            else:
                tries.append(pop)
        return ans if len(ans) == len(s) else ""
    
    