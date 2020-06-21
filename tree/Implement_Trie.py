'''
link: https://leetcode.com/problems/implement-trie-prefix-tree/
Implement a trie with insert, search, and startsWith methods.

Example:

Trie trie = new Trie();

trie.insert("apple");
trie.search("apple");   // returns true
trie.search("app");     // returns false
trie.startsWith("app"); // returns true
trie.insert("app");   
trie.search("app");     // returns true
Note:

You may assume that all inputs are consist of lowercase letters a-z.
All inputs are guaranteed to be non-empty strings.
'''

class Node:
    def __init__(self, value):
        self.value = value
        self.children = {}
        self.finish = False
        

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.node = Node(-1)

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        curr = self.node
        for i in range(len(word)):
            if not curr.children.get(word[i], False):
                curr.children[word[i]] = Node(word[i])
            curr = curr.children[word[i]]
        curr.finish = True
        
    
    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        curr = self.node
        for ele in word:
            if not curr.children.get(ele, False):
                return False
            curr = curr.children[ele]
        return curr.finish
        

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        curr = self.node
        for ele in prefix:
            if not curr.children.get(ele, False):
                return False
            curr = curr.children[ele]
        return True
            


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)