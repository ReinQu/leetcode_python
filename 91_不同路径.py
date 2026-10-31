"""
一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为 “Start” ）。
机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为 “Finish” ）。
问总共有多少条不同的路径？
"""
class Solution:#本质数学：C27等于A7/(A2*A5)
    def uniquePaths(self, m: int, n: int) -> int:
        #阶乘
        def dfs(i:int)->int:
            if i==0:return 1
            return dfs(i-1)*i
        return dfs(m+n-2)//(dfs(m-1)*dfs(n-1))


from functools import cache
class Solution1:#记忆化搜索：选或不选
    def uniquePaths(self, m: int, n: int) -> int:
        @cache
        def dfs(i:int,j:int)->int:
            if i<0 or j<0:return 0
            if i==0 and j==0:return 1
            return dfs(i-1,j)+dfs(i,j-1)
        return dfs(m-1,n-1)

class Solution2:#二维动态规划转化为一维:我们只关注第一行d[0][j]只与d[0][j+1]有关
    def uniquePaths(self,m:int,n:int)->int:
        dp=[0]*(n+1)
        dp[1]=1
        #从第一行开始，先处理行再处理列
        for _ in range(m):
            for j in range(n):
                dp[j+1]+=dp[j]
        return dp[n]
