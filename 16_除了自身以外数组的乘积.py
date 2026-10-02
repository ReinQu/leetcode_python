"""
给你一个整数数组 nums，返回 数组 answer ，其中 answer[i] 等于 nums 中除了 nums[i] 之外其余各元素的乘积 。
题目数据 保证 数组 nums之中任意元素的全部前缀元素和后缀的乘积都在  32 位 整数范围内。
请 不要使用除法，且在 O(n) 时间复杂度内完成此题。
"""
class Solution1:#左右乘积列表，用l和r来记录nums[i]左右两边的乘积
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        l,r,answer=[0]*n,[0]*n,[0]*n
        l[0]=1
        for i in range(1,n):
            l[i]=l[i-1]*nums[i-1]
        r[n-1]=1
        for i in range(n-2,-1,-1):
            r[i]=r[i+1]*nums[i+1]
        for i in range(n):
            answer[i]=l[i]*r[i]
        return answer

class Solution2:#空间复杂度为O(1)
    def productExceptSelf(self, nums: List[int]) -> List[int]: 
        n=len(nums)
        answer=[0]*n
        answer[0]=1
        for i in range(1,n):
            answer[i]=answer[i-1]*nums[i-1]
        r=1
        for i in reversed(range(n)):
            answer[i]=answer[i]*r
            r=r*nums[i]
        return answer




#class Solution3:这里有一种自动微分反向传播的做法：y=a*b*c*d，对abcd分别偏导，得到的就是对应的乘积