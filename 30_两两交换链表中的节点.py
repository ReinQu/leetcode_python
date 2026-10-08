"""
给你一个链表，两两交换其中相邻的节点，并返回交换后链表的头节点。你必须在不修改节点内部的值的情况下完成本题（即，只能进行节点交换）。
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:#交换需要三个变量，其中一个prev用于维护
    def swapPairs(self, head: ListNode | None) -> ListNode | None:
        dummy=ListNode(0,head)
        prev=dummy
        while prev.next and prev.next.next:
            first=prev.next
            second=first.next
            first.next=second.next
            second.next=first
            prev.next=second
            prev=first



        return dummy.next