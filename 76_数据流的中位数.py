"""
中位数是有序整数列表中的中间值。如果列表的大小是偶数，则没有中间值，中位数是两个中间值的平均值。
例如 arr = [2,3,4] 的中位数是 3 。
例如 arr = [2,3] 的中位数是 (2 + 3) / 2 = 2.5 。
实现 MedianFinder 类:
MedianFinder() 初始化 MedianFinder 对象。
void addNum(int num) 将数据流中的整数 num 添加到数据结构中。
double findMedian() 返回到目前为止所有元素的中位数。与实际答案相差 10-5 以内的答案将被接受。
"""
class MedianFinder:#这个做法超市了，必须优化addNum的算法

    def __init__(self):
        self.st=[]

    def addNum(self, num: int) -> None:
        self.st.append(num)
        self.st.sort()

    def findMedian(self) -> float:
        n=len(self.st)
        if n%2==1:
            return float(self.st[n//2])
        else:
            return (self.st[n//2]+self.st[n//2-1])/2
from heapq import *
class MedianFinder2:#用正数存大的一半，用负数存小的一半
    def __init__(self):
        self.A=[]
        self.B=[]
    #我们约定A可以比B多一个元素
    def addNum(self,num:int)->None:
        if len(self.A)!=len(self.B):
            heappush(self.A,num)
            heappush(self.B,-heappop(self.A))
        else:
            heappush(self.B,-num)
            heappush(self.A,-heappop(self.B))
    def findMedian(self) -> float:
        return self.A[0] if len(self.A) != len(self.B) else (self.A[0] - self.B[0]) / 2.0
