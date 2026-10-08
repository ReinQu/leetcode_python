"""
给你一个长度为 n 的链表，每个节点包含一个额外增加的随机指针 random ，该指针可以指向链表中的任何节点或空节点。
构造这个链表的 深拷贝。 深拷贝应该正好由 n 个 全新 节点组成，其中每个新节点的值都设为其对应的原节点的值。新节点的 next 指针和 random 指针也都应指向复制链表中的新节点，并使原链表和复制链表中的这些指针能够表示相同的链表状态。复制链表中的指针都不应指向原链表中的节点 
"""

# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solutio1:#哈希表
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:return
        dic={}
        #复制各结点
        cur=head
        while cur:
            dic[cur]=Node(cur.val)#这里字典的键和值都是node类型
            cur=cur.next
        cur=head

        while cur:
            dic[cur].next=dic.get(cur.next)#A.next=A.next.next
            dic[cur].random=dic.get(cur.random)
            cur=cur.next
        return dic[head]
