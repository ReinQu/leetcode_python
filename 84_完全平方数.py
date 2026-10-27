"""
给你一个整数 n ，返回 和为 n 的完全平方数的最少数量 。
完全平方数 是一个整数，其值等于另一个整数的平方；换句话说，其值等于一个整数自乘的积。例如，1、4、9 和 16 都是完全平方数，而 3 和 11 不是。
"""
from functools import cache
from math import inf,isqrt
class Solution1:#记忆化搜索，该方法实际可行，但是内存炸了
    def numSquares(self, n: int) -> int:
        @cache#cache会记住函数计算过的结果。当函数收到相同参数时，直接返回旧结果
        def dfs(i:int,j:int)->int:
            #i=0，全部搜索完毕，对应两种情况：j=0，则此方案行得通，返回0；j!=0，则不行，j=inf，不参与最小值竞争
            if i==0:return inf if j else 0
            #i的平方大于目标数，i-1
            if j<i*i:
                return dfs(i-1,j)
            #两种情况：一种不选i，那么范围就在i-1内；一种选i，则范围在i内，但目标变成j-i*i
            return min(dfs(i-1,j),dfs(i,j-i*i)+1)
        return dfs(isqrt(n),n)

class Solution2:#一维动态规划
    def numSquares(self, n: int) -> int:
        #dp[i]表示凑出数字i最少需要几个数字
        dp=[0]+[inf]*n
        for i in range(1,isqrt(n)+1):
            square=i*i
            for j in range(square,n+1):
                dp[j]=min(dp[j],dp[j-square]+1)#比较不使用当前平方数和使用一个当前平方数的结果
        return dp[n]