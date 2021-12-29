# -- coding: utf-8 --
# Python Implementation of Trie Data Structure (Prefix Tree)
# 数据结构Trie(前缀树)的Python实现
# 前缀树 也是一种树  只不过不是二叉树了

class Trie:
    def __init__(self) -> None:
        self.data = {}
        self.isLeaf = False
    
    def insert(self, word):
        cur = self
        for i in word:
            if not i in cur.data:
                cur.data[i] = Trie()
            cur = cur.data[i]
        cur.isLeaf = True

    def search(self, word):
        cur = self
        for i in word:
            if i not in cur.data:
                return False
            cur = cur.data[i]
        return cur.isLeaf

    def startsWith(self, prefix):
        cur = self
        for i in prefix:
            if i not in cur.data:
                return False
            cur = cur.data[i]
        return True

obj = Trie()
obj.insert("alex")
print(obj.search("ale"))
print(obj.search("alex"))
print(obj.startsWith("al"))