"""
给你链表的头节点 head ，每 k 个节点一组进行翻转，请你返回修改后的链表。
k 是一个正整数，它的值小于或等于链表的长度。如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序。
你不能只是单纯的改变节点内部的值，而是需要实际进行节点交换。
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:#第一道自己做出的困难题
    def reverseKGroup(self, head: ListNode | None, k: int) -> ListNode | None:
        step=head
        len=0
        while step:
            step=step.next
            len+=1
        epoch=len//k
        second=head
        dummy=ListNode(0,head)
        first=dummy
        for i in range(epoch):
            for j in range(k):
                third=second.next
                second.next=first
                first=second
                second=third
            prev=first
            for l in range(k-1):
                first=first.next
            first.next.next=prev
            first.next=second
        return dummy.next


