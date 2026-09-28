"""
给你一个整数数组 nums，有一个大小为 k 的滑动窗口从数组的最左侧移动到数组的最右侧。
你只可以看到在滑动窗口内的 k 个数字。滑动窗口每次只向右移动一位。
返回 滑动窗口中的最大值 。
"""
import collections
import heapq#堆和队列

class Solution1:#单调队列，时间复杂度为O(n),空间复杂度为O(k)
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        dq=collections.deque()#dq是一个双端队列，用于存储下标，并且对应的nums值从队首到队尾单调递减，使队首dq[0]始终指向最大值

        result=[]
        for i,num in enumerate(nums):
            while dq and nums[dq[-1]]<=num:#从队尾开始，删除比当前数字小的元素
                dq.pop()#pop从右边删除
            dq.append(i)#先前已经删除了比当前数字小的元素，所以此时的i对应的num就是最小

            if dq[0]<=i-k:#用于判断当前队首是否还在窗口中
                dq.popleft()#从左边删除

            if i>=k-1:#从一个完整的窗口开始记录答案
                result.append(nums[dq[0]])

        return result

    
class Solution2:#时间复杂度为O(NLOGN),空间复杂度O（N）
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:

        n=len(nums)
        q=[(-nums[i],i) for i in range(k)]#q为二元数组，用于存下标和值
        heapq.heapify(q)#对其进行最小推排序：即得到最小值

        ans=[-q[0][0]]#第一个就是最大值
        for i in range(k,n):
            heapq.heappush(q,(-nums[i],i))#入队
            while q[0][1]<=i-k:#小于窗口左边界
                heapq.heappop(q)#出队

            ans.append(-q[0][0])
        return ans

    


def main():
    sol=Solution2()
    cases=[
        ([1,3,-1,-3,5,3,6,7],3,[3,3,5,5,6,7]),
        ([9,10,9,-7,-4,-8,2,-6],5,[10,10,9,2]),
        ([-7,-8,7,5,7,1,6,0],4,[7,7,7,7,7]),
        ([1],1,[1]),
        ([1,-1],1,[1,-1]),
        ([7,2,4],2,[7,4]),
        ([1,3,1,2,0,5],3,[3,3,2,5]),
        ([-4,-2,-7,-1,-9,-3],3,[-2,-1,-1,-1]),
        ([3,1,4,1,5],5,[5]),
    ]
    for nums,k,expected in cases:
        got=sol.maxSlidingWindow(nums,k)
        print("OK  " if got==expected else "FAIL",k,nums,"->",got,"expected",expected)

if __name__=="__main__":
    main()
