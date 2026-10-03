"""
给定一个 m x n 的矩阵，如果一个元素为 0 ，则将其所在行和列的所有元素都设为 0 。请使用 原地 算法。
"""
class Solution1:#遍历，非常简单，自己做出了，空间复杂度O(mn)
    def setZeroes(self, matrix: list[list[int]]) -> None:
        m=len(matrix)
        n=len(matrix[0])
        s=list()
        for i in range(m):
            for j in range(n):
                if matrix[i][j]==0:
                    s.append((i,j))
        for p in s:
            for j in range(n):
                matrix[p[0]][j]=0
            for i in range(m):
                matrix[i][p[1]]=0

class Solution2:#直接将是否需要清零存储在第一行和第一列中，同时需要判断第一行和第一列中原本是否有0
    def setZeroes(self, matrix: list[list[int]]) -> None:
        m=len(matrix)
        n=len(matrix[0])

        first_row_zero=0
        first_col_zero=0

        #判断第一行和第一列是否有0
        for i in range(m):
            if matrix[i][0]==0:
                first_col_zero=True
        for j in range(n):
            if matrix[0][j]==0:
                first_row_zero=True

        #用第一行和第一列记录其他位置的0
        for i in range(1,m):
            for j in range(1,n):
                if matrix[i][j]==0:
                    matrix[i][0]=0
                    matrix[0][j]=0

        #置零
        for i in range(1,m):
            for j in range(1,n):
                if matrix[i][0]==0 or matrix[0][j]==0:
                    matrix[i][j]=0

        if first_col_zero:
            for i in range(m):
                matrix[i][0]=0

        if first_row_zero:
            for j in range(n):
                matrix[0][j]=0


