"""
给定一个链表的头节点  head ，返回链表开始入环的第一个节点。 如果链表无环，则返回 null。
如果链表中有某个节点，可以通过连续跟踪 next 指针再次到达，则链表中存在环。 为了表示给定链表中的环，评测系统内部使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。如果 pos 是 -1，则在该链表中没有环。注意：pos 不作为参数进行传递，仅仅是为了标识链表的实际情况。
不允许修改 链表。
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:#fast比slow快，最后会套一圈，所以fast比slow多走的路就是环的长度
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return None
        
        fast=slow=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            if fast is slow:#为什么用is而不是==：因为这里要判断的是结点是否相同，而不是值是否一致
                break
        #判断是因为没有环结束循环还是找到环的长度结束的循环
        if fast is None or fast.next is None:
            return None
        #slow从当前结点，fast从头结点开始
        fast=head
        while fast is not slow:
            fast=fast.next
            slow=slow.next
            
        return fast


        

        