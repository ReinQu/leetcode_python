"""
给你一个 m 行 n 列的矩阵 matrix ，请按照 顺时针螺旋顺序 ，返回矩阵中的所有元素。
"""
class Solution:#从左到右，从上到下，从右到左，从下到上的循环，界定l、r、t、b四个边界
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        if not matrix:
            return []
        l,r,t,b,result=0,len(matrix[0])-1,0,len(matrix)-1,[]
        while True:
            for i in range(l,r+1):
                result.append(matrix[t][i])
            t+=1
            if t>b:break
            for i in range(t,b+1):
                result.append(matrix[i][r])
            r-=1
            if l>r:break
            for i in range(r,l-1,-1):
                result.append(matrix[b][i])
            b-=1
            if t>b:break
            for i in range(b,t-1,-1):
                result.append(matrix[i][l])
            l+=1
            if l>r:break
        return result


        