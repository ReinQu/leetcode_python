"""
按照国际象棋的规则，皇后可以攻击与之处在同一行或同一列或同一斜线上的棋子。
n 皇后问题 研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。
给你一个整数 n ，返回所有不同的 n 皇后问题 的解决方案。
每一种解法包含一个不同的 n 皇后问题 的棋子放置方案，该方案中 'Q' 和 '.' 分别代表了皇后和空位
"""
class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        ans=[]
        queens=[0]*n
        col=[False]*n#用来记录哪些列已经被占用
        diag1=[False]*(n*2-1)#存放行加列
        diag2=[False]*(n*2-1)#存放行减列
        def dfs(r:int)->None:
            if r==n:
                ans.append(['.'*c+'Q'+'.'*(n-1-c) for c in queens])
                return

            for c,ok in enumerate(col):
                if not ok and not diag1[r+c] and not diag2[r-c]:
                    queens[r]=c
                    col[c]=diag1[r+c]=diag2[r-c]=True
                    dfs(r+1)
                    col[c]=diag1[r+c]=diag2[r-c]=False

        dfs(0)
        return ans
        