"""
给你单链表的头节点 head ，请你反转链表，并返回反转后的链表。
"""
#Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        if  head is None:#c语言中head可以是头结点（空的），也可以是有值的，但在py中一般head都是有值的
            return None
        first=None
        second=head#和c语言不同，这里直接赋给head而不是head.next
        while second!=None:
            third=second.next
            second.next=first
            first=second
            second=third
        return first#没有头结点


