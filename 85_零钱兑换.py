"""
给你一个整数数组 coins ，表示不同面额的硬币；以及一个整数 amount，表示总金额。
计算并返回可以凑成总金额所需的 最少 的硬币个数。如果没有任何一种硬币组合能组成总金额，返回 -1 。
你可以认为每种硬币的数量是无限的。
"""
from math import inf
from functools import cache
class Solution1:#记忆化搜索，依旧超时
    def coinChange(self, coins: list[int], amount: int) -> int:
        coins.sort()
        @cache#时间依旧过长
        def dfs(i:int,j:int)->int:
            #符合条件，终止
            if j==0:return 0
            #i遍历到-1或j超出限度，inf不计入min的比较
            if i<0 or j<0:
                return inf
            if coins[i]>j:
                dfs(i-1,j)
            return min(dfs(i-1,j),dfs(i,j-coins[i])+1)
        ans=dfs(len(coins)-1,amount)
        return -1 if ans==inf else ans

class Solution2:#一维动态规划：实现空间、时间上的优化
    def coinChange(self, coins: list[int], amount: int) -> int:
        #dp[i]表示凑成数字i最少需要几个数字
        dp=[0]+[inf]*amount
        for i in coins:
            for j in range(i,amount+1):
                dp[j]=min(dp[j],dp[j-i]+1) 
        ans=dp[amount]
        return -1 if ans==inf else ans