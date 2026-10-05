"""
给你一个单链表的头节点 head ，请你判断该链表是否为回文链表。如果是，返回 true ；否则，返回 false 
"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:#快慢指针找中点加反转链表
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head is None or head.next is None:#如果是空链表或者只有一个结点
            return True
        slow=head
        fast=head

        #令slow对应反转链表的头点
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next

        #反转后半部分
        prev=None
        curr=slow

        while curr:
            next_node=curr.next
            curr.next=prev
            prev=curr
            curr=next_node

        #从头和后半部分进行比较，此时：1->2->3<-2<-1
        left=head
        right=prev
        while right:
            if left.val!=right.val:
                return False
            left=left.next
            right=right.next
        return True




        
