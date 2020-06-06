'''
link: https://leetcode.com/problems/accounts-merge/
Given a list accounts, each element accounts[i] is a list of strings, where the first element accounts[i][0] is a name, and the rest of the elements are emails representing emails of the account.

Now, we would like to merge these accounts. Two accounts definitely belong to the same person if there is some email that is common to both accounts. Note that even if two accounts have the same name, they may belong to different people as people could have the same name. A person can have any number of accounts initially, but all of their accounts definitely have the same name.

After merging the accounts, return the accounts in the following format: the first element of each account is the name, and the rest of the elements are emails in sorted order. The accounts themselves can be returned in any order.

Example 1:
Input: 
accounts = [["John", "johnsmith@mail.com", "john00@mail.com"], ["John", "johnnybravo@mail.com"], ["John", "johnsmith@mail.com", "john_newyork@mail.com"], ["Mary", "mary@mail.com"]]
Output: [["John", 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com'],  ["John", "johnnybravo@mail.com"], ["Mary", "mary@mail.com"]]
Explanation: 
The first and third John's are the same person as they have the common email "johnsmith@mail.com".
The second John and Mary are different people as none of their email addresses are used by other accounts.
We could return these lists in any order, for example the answer [['Mary', 'mary@mail.com'], ['John', 'johnnybravo@mail.com'], 
['John', 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com']] would still be accepted.
Note:

The length of accounts will be in the range [1, 1000].
The length of accounts[i] will be in the range [1, 10].
The length of accounts[i][j] will be in the range [1, 30].

'''



from collections import defaultdict

class Solution:
    '''O(NMlogN)/O(NM)'''
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        
        d, email2name, ans= {}, {}, defaultdict(list)
        
        def find(x):
            if d[x] == x: return x
            return find(d[x])
            
        def merge(a, b):
            nonlocal d
            a, b = find(a), find(b)
            d[a] = a; d[b] = a
        
        
        for i, acc in enumerate(accounts):
            name, emails, other_account = acc[0], acc[1:], None
            for email in emails:
                email2name[email] = name
                if d.get(email, 'initial') == 'initial' :
                    d[email] = emails[0]
                else: 
                    other_account = d[email]
                    
            if other_account:
                for email in emails:
                    merge(other_account, email)
                    
        for key in d.keys():
            d[key] = find(key)
            
        for em1, em2 in d.items():
            ans[em2].append(em1)
            
        return [[email2name[key], *sorted(emails) ] for key, emails in ans.items()]
    
    
class Solution:
    '''O(NMlogN)/O(NM)'''
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        
        ids = list(range(10001))
        em2name, em2id, ans= {}, {}, defaultdict(list)
        
        def find(x):
            if ids[x] == x: return x
            return find(ids[x])
            
        def merge(a, b):
            nonlocal ids
            ids[find(a)] = find(b)
           
        i = 0
        for acc in accounts:
            name = acc[0]
            for email in acc[1:]:
                em2name[email] = name
                if email not in em2id:
                    em2id[email] = i; i += 1;
                merge(em2id[acc[1]], em2id[email])
        
        for email in em2name:
            ans[find(em2id[email])].append(email)
            
        return [[em2name[emails[0]], *sorted(emails) ] for key, emails in ans.items()]
    
    
class Solution:
    '''BFS
    O(MNlogM)/O(MN)
    '''
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        
        em2name, seen, graph, ans = {}, set(), defaultdict(set), []
        
        for acc in accounts:
            name = acc[0]
            for email in acc[1:]:
                graph[acc[1]].add(email)
                graph[email].add(acc[1])
                em2name[email] = name
    
        for email in graph:
            if email not in seen:
                seen.add(email)
                stack = [email]
                component = []
                while stack:
                    node = stack.pop()
                    component.append(node)
                    for nei in graph[node]:
                        if nei not in seen:
                            seen.add(nei)
                            stack.append(nei)       
                ans.append([em2name[email]]+ sorted(component))
        return ans
    
    
