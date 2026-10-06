"""
将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:#双指针，创建一个伪结点
    def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
        cur=dum=ListNode(0)
        while list1 and list2:
            if list1.val<list2.val:
                cur.next,list1=list1,list1.next
            else:
                cur.next,list2=list2,list2.next
            cur=cur.next
        #若其中一个结束，另一个没结束
        if list1:
            cur.next=list1
        else:
            cur.next=list2
        return dum.next
        