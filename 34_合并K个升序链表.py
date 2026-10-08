"""
给你一个链表数组，每个链表都已经按升序排列。
请你将所有链表合并到一个升序链表中，返回合并后的链表。
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution1:
    def mergeKLists(self, lists: list[ListNode | None]) -> ListNode | None:
        import heapq
        cur=dummy=ListNode()
        #创建堆
        h=[]
        #把头结点放入堆
        for i,head in enumerate(lists):
            if head:
                heapq.heappush(h,(head.val,i,head))
        
        while h:
            #取出堆的最小元素,heappop实现
            _,i,node=heapq.heappop(h)
            cur.next=node
            cur=cur.next

            if node.next:
                heapq.heappush(h,(node.next.val,i,node.next))
        return dummy.next

        
        
    
    
        





