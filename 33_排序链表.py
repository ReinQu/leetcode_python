"""
给你链表的头结点 head ，请将其按 升序 排列并返回 排序后的链表 。
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:#归并排序（递归法），二分
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        #用快慢指针找到中点
        slow,fast=head,head.next
        while fast and fast.next:
            fast=fast.next.next
            slow=slow.next
        #切分
        mid,slow.next=slow.next,None
        #递归再次切分，一直切分到两个一组
        #把左半边链表排序后，返回排序好的左链表头节点，交给 left。
        #把右半边链表排序后，返回排序好的右链表头节点，交给 right。
        left,right=self.sortList(head),self.sortList(mid)

        h=res=ListNode(0)
        while left and right:
            if left.val<right.val:
                h.next,left=left,left.next
            else:h.next,right=right,right.next
            h=h.next
        h.next=left or right
        return res.next




