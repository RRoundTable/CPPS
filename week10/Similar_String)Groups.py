'''
link: https://leetcode.com/problems/similar-string-groups/
Two strings X and Y are similar if we can swap two letters (in different positions) of X, so that it equals Y.

For example, "tars" and "rats" are similar (swapping at positions 0 and 2), and "rats" and "arts" are similar, but "star" is not similar to "tars", "rats", or "arts".

Together, these form two connected groups by similarity: {"tars", "rats", "arts"} and {"star"}.  Notice that "tars" and "arts" are in the same group even though they are not similar.  Formally, each group is such that a word is in the group if and only if it is similar to at least one other word in the group.

We are given a list A of strings.  Every string in A is an anagram of every other string in A.  How many groups are there?

 

Example 1:

Input: A = ["tars","rats","arts","star"]
Output: 2
 

Constraints:

1 <= A.length <= 2000
1 <= A[i].length <= 1000
A.length * A[i].length <= 20000
All words in A consist of lowercase letters only.
All words in A have the same length and are anagrams of each other.
The judging time limit has been increased for this question.
'''

from collections import defaultdict
from itertools import combinations

class Solution:
    def numSimilarGroups(self, A: List[str]) -> int:
        '''
        if N < W ^ 2:
            O(N^2*W)/O(N)
        else:
            O(N*W^3)/O(N^2 W)
        '''
        A = list(set(A))
        n, w = len(A), len(A[0])
        
        def compare(a, b):
            count = 0
            for i in range(len(b)):
                if count > 2: return False
                if a[i] != b[i]: 
                    count += 1
            if count == 2: return True
            
        def find(x):
            while x != union[x]:
                x = union[x]
            return x
        
        union = list(range(len(A)))
        if n < w * w:
            for i in range(len(A)):
                for j in range(i+1, len(A)):
                    if find(i) == find(j):continue
                    if compare(A[i], A[j]):
                        union[find(i)] = find(j)
        else:
            d = defaultdict(lambda: set())
            for i, word in enumerate(A):
                L = list(word)
                for l1, l2 in combinations(range(w), 2):
                    L[l1], L[l2] = L[l2], L[l1]
                    d["".join(L)].add(i)
                    L[l1], L[l2] = L[l2], L[l1]
            for i1, word in enumerate(A):
                for i2 in d[word]:
                    union[find(i1)] = find(i2)
        union = [find(u) for u in union]
        return len(set(union))