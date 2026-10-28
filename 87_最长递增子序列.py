"""
给你一个整数数组 nums ，找到其中最长严格递增子序列的长度。
子序列 是由数组派生而来的序列，删除（或不删除）数组中的元素而不改变其余元素的顺序。例如，[3,6,2,7] 是数组 [0,3,1,6,2,2,7] 的子序列。
"""
class Solution1:#记忆化搜索，依旧贼慢
    def lengthOfLIS(self, nums: list[int]) -> int:
        @cahce
        def dfs(i:int)->int:#i表示i前能够得到的最长子序列
            ans=1
            for j in range(i):
                if nums[j]<nums[i]:
                    ans=max(ans,dfs(j)+1)
            return ans
        #最长递增子序列未必以数组最后一个元素结尾
        return max(dfs(i) for i in range(len(nums)))

class Solution2:#一维数组：空间优化
    def lengthOfLIS(self, nums: list[int]) -> int:
        n=len(nums)
        dp=[1]*n

        for i in range(n):
            for j in range(i):
                if nums[j]<nums[i]:
                    dp[i]=max(dp[i],dp[j]+1)
        return max[dp]