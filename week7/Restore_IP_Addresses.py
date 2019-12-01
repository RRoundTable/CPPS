'''
link: https://leetcode.com/problems/restore-ip-addresses/
Given a string containing only digits, restore it by returning all possible valid IP address combinations.

Example:

Input: "25525511135"
Output: ["255.255.11.135", "255.255.111.35"]
'''

class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        def backtracking(indexs):
            if len(indexs) > 4 or len(s[indexs[-1]:]) / (4 - len(indexs) + 1) > 3: return
            if len(indexs) == 4 and not (s[indexs[-1]] == "0" and len(s[indexs[-1]:]) > 1) and int(s[indexs[-1]:]) <= 255: 
                boundary.append(indexs)
                return
            for i in range(indexs[-1]+1, min(indexs[-1]+4, len(s))):
                if int(s[indexs[-1]:i]) <= 255 and not (s[indexs[-1]] == "0" and len(s[indexs[-1]:i]) > 1):backtracking(indexs + [i])
            
        boundary, ans = [], []
        backtracking([0])
        for b in boundary:
            ans.append(s[b[0]: b[1]] + "." + s[b[1]:b[2]] + "." +s[b[2]:b[3]] + "."+ s[b[3]:])
        return ans