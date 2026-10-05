"""
给你两个单链表的头节点 headA 和 headB ，请你找出并返回两个单链表相交的起始节点。如果两个链表不存在相交节点，返回 null 。
图示两个链表在节点 c1 开始相交：
"""
#Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:#双指针，让两个指针分别从a和b开始，若ab不同长，就在完成一圈后，分别从另外的结点开始
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        A,B=headA,headB
        while A!=B:
            if A:
                A=A.next
            else:
                A=headB
            if B:
                B=B.next
            else:
                B=headA
        return A
            

