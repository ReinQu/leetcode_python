"""
设计一个支持 push ，pop ，top 操作，并能在常数时间内检索到最小元素的栈。
实现 MinStack 类:
MinStack() 初始化堆栈对象。
void push(int value) 将元素 value 推入堆栈。
void pop() 删除堆栈顶部的元素。
int top() 获取堆栈顶部的元素。
int getMin() 获取堆栈中的最小元素。
"""
from math import inf
class MinStack:

    def __init__(self):
       self.st=[(0,inf)]#栈底哨兵

    def push(self, value: int) -> None:
        self.st.append((value,min(self.st[-1][1],value)))#st[-1][1]对应原栈顶元素存放的最小值

    def pop(self) -> None:
        self.st.pop()

    def top(self) -> int:
        return self.st[-1][0]

    def getMin(self) -> int:
        return self.st[-1][1]