"""
请你设计并实现一个满足  LRU (最近最少使用) 缓存 约束的数据结构。
实现 LRUCache 类：
LRUCache(int capacity) 以 正整数 作为容量 capacity 初始化 LRU 缓存
int get(int key) 如果关键字 key 存在于缓存中，则返回关键字的值，否则返回 -1 。
void put(int key, int value) 如果关键字 key 已经存在，则变更其数据值 value ；如果不存在，则向缓存中插入该组 key-value 。如果插入操作导致关键字数量超过 capacity ，则应该 逐出 最久未使用的关键字。
函数 get 和 put 必须以 O(1) 的平均时间复杂度运行。
"""
class Node:
    def __init__(self,key=0,value=0):
        self.key=key
        self.value=value

class LRUCache:

    def __init__(self, capacity: int):
        #构建双链表
        self.capacity=capacity
        self.dummy=Node()
        self.dummy.prev=self.dummy
        self.dummy.next=self.dummy
        self.key_to_node={}

    #获取key对应的结点，同时把该节点移到链表头部
    def get_node(self, key: int) -> Optional[Node]:
        if key not in self.key_to_node:
            return None
        node=self.key_to_node[key]
        self.remove(node)#先删掉
        self.push_front(node)#再加到最上面，表示最近使用
        return node

    def get(self,key:int) -> int:
        node=self.get_node(key)
        return node.value if node else -1


    def put(self, key: int, value: int) -> None:
        node=self.get_node(key)#直接将其移动到头部了
        if node:
            node.value=value
            return
        self.key_to_node[key]=node=Node(key,value)
        self.push_front(node)
        if len(self.key_to_node)>self.capacity:
            back_node=self.dummy.prev#指向链表尾部

            del self.key_to_node[back_node.key]#删除哈希表中结点对应的key   
            self.remove(back_node)#删除结点

    #删除功能
    def remove(self,x:Node) ->None:
        x.prev.next=x.next
        x.next.prev=x.prev

    #将结点插入到头结点后模块
    def push_front(self,x:Node) ->None:
        x.prev=self.dummy
        x.next=self.dummy.next
        x.prev.next=x
        x.next.prev=x

