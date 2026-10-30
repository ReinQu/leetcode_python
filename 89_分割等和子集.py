"""
给你一个 只包含正整数 的 非空 数组 nums 。请你判断是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。
"""
from functools import cache
class Solution1:#记忆化搜索
    def canPartition(self, nums: List[int]) -> bool:
        s=sum(nums)
        if s%2==1:return False
        @cache
        def dfs(i:int,j:int)->bool:
            if i<0:
                return j==0
            if j<nums[i]:
                return dfs(i-1,j)
            return dfs(i-1,j-nums[i]) or dfs(i-1,j)

        return dfs(len(nums)-1,s//2)
    

class Solution2:#一维数组空间优化
    def canPartition(self, nums: List[int]) -> bool:
        s=sum(nums)
        if s%2==1:return False
        target=s//2
        #dp[0]=0:什么数字都不选就能凑出数字0
        dp=[True]+[False]*s

        for x in nums:
            for j in range(target,x-1,-1):#target>=j>=x
                #两者只要有其一是true那就是true
                dp[j]=dp[j] or dp[j-x]
        return dp[target]