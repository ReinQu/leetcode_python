"""
给你一个整数数组 nums，有一个大小为 k 的滑动窗口从数组的最左侧移动到数组的最右侧。
你只可以看到在滑动窗口内的 k 个数字。滑动窗口每次只向右移动一位。
返回 滑动窗口中的最大值 。
"""
import collections
import heapq

class Solution1:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        dq=collections.deque()
        result=[]
        for i,num in enumerate(nums):
            while dq and nums[dq[-1]]<=num:
                dq.pop()
            dq.append(i)

            if dq[0]<=i-k:
                dq.popleft()

            if i>=k-1:
                result.append(nums[dq[0]])

        return result
class Solution2:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:

        n=len(nums)
        q=[(-nums[i],i) for i in range(k)]
        heapq.heapify(q)#heap和q，对其进行最小推牌序：即得到最小值

        ans=[-q[0][0]]#第一个就是最大值
        for i in range(k,n):
            heapq.heappush(q,(-nums[i],i))#入队
            while q[0][1]<=i-k:
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
