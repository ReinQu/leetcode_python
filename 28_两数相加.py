"""
给你两个 非空 的链表，表示两个非负的整数。它们每位数字都是按照 逆序 的方式存储的，并且每个节点只能存储 一位 数字。
请你将两个数相加，并以相同形式返回一个表示和的链表。
你可以假设除了数字 0 之外，这两个数都不会以 0 开头。
"""# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        dum = ListNode(0)
        cur = dum
        remain_num = 0
        while l1 or l2:
            if l1 and l2:
                total = l1.val + l2.val + remain_num
                l1 = l1.next
                l2 = l2.next
            elif l1:
                total = l1.val + remain_num
                l1 = l1.next
            else:
                total = l2.val + remain_num
                l2 = l2.next
            cur.next = ListNode(total % 10)#用这个方式创建结点并赋值
            cur = cur.next
            remain_num = total // 10
        if remain_num:
            cur.next = ListNode(remain_num)
        return dum.next
