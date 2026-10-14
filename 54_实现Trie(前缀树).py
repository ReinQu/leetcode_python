"""
Trie（发音类似 "try"）或者说 前缀树 是一种树形数据结构，用于高效地存储和检索字符串数据集中的键。这一数据结构有相当多的应用情景，例如自动补全和拼写检查。
请你实现 Trie 类：
Trie() 初始化前缀树对象。
void insert(String word) 向前缀树中插入字符串 word 。
boolean search(String word) 如果字符串 word 在前缀树中，返回 true（即，在检索之前已经插入）；否则，返回 false 。
boolean startsWith(String prefix) 如果之前已经插入的字符串 word 的前缀之一为 prefix ，返回 true ；否则，返回 false 。
"""

class Node:
    __slots__='son','end'#非必要：限制 Node 类的实例能够通过普通属性赋值拥有的属性，并且通常可以减少每个实例的内存占用。
    def __init__(self):
        self.son={}
        self.end=False
class Trie:#26叉树

    def __init__(self):
        self.root=Node()

    def insert(self, word: str) -> None:
        cur=self.root
        for c in word:
            if c not in cur.son:
                cur.son[c]=Node()#实现赋值
            cur=cur.son[c]
        cur.end=True

    def find(self,word:str)->int:
        cur=self.root
        for c in word:
            if c not in cur.son:
                return 0
            cur=cur.son[c]
        #2表示完全相同，1表示前缀相同，0表示完全不同
        return 2 if cur.end else 1

    def search(self, word: str) -> bool:
        return self.find(word)==2

    def startsWith(self, prefix: str) -> bool:
        return self.find(prefix)!=0#完全相同和前缀相同都成立