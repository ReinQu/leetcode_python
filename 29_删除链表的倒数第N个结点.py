"""
给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:#双指针，遍历一遍，删除某结点要找到该结点的前一个结点，特殊情况：删除的是头结点
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        dummy=ListNode(0,head)#创建一个虚拟头结点，防止删除原来头结点报错的情况
        fast=dummy
        slow=dummy
        for i in range(n+1):
            fast=fast.next
        while fast:
            slow=slow.next
            fast=fast.next
        slow.next=slow.next.next
        return dummy.next


        
        