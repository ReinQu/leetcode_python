"""
给定一个包含非负整数的 m x n 网格 grid ，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。
说明：每次只能向下或者向右移动一步。
"""
from functools import cache 
class Solution1:#记忆化搜索
    def minPathSum(self, grid: list[list[int]]) -> int:
        m,n=len(grid),len(grid[0])
        ans=0
        @cache
        def dfs(m:int,n:int)->int:
            if m==n==0:return grid[0][0]
            if m<0 or n<0:return float('inf')#超出边界，inf不参与min
            return min(dfs(m-1,n)+grid[m][n],dfs(m,n-1)+grid[m][n])
        return dfs(m-1,n-1)
from math import inf
class Solution2:#空间优化：二维数组转一维
    def minPathSum(self, grid: list[list[int]]) -> int:
        dp=[inf]*(len(grid[0])+1)
        dp[1]=0#为了让后面dp[1]=grid[0][0]
        #和上题一样：先按行处理，再按列
        for row in grid:
            for j,x in enumerate(row):
                dp[j+1]=min(dp[j],dp[j+1])+x#此时还没遍历到j+1所以dp[j+1]是当前位置的上边，dp[j]在左边
        return dp[-1]