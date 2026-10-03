"""
给定一个 n × n 的二维矩阵 matrix 表示一个图像。请你将图像顺时针旋转 90 度。
你必须在 原地 旋转图像，这意味着你需要直接修改输入的二维矩阵。
请不要 使用另一个矩阵来旋转图像。
"""
class Solution:#四个值的轮换，用tmp存A，核心是搞清楚(i,j)对应的另外三个坐标
    def rotate(self, matrix: list[list[int]]) -> None:
        n=len(matrix)
        for i in range(n//2):
            for j in range((n+1)//2):#当n为奇数时，因为没法做到平分，所以j会比i多1个单位的边界
                tmp=matrix[i][j]
                matrix[i][j]=matrix[n-1-j][i]
                matrix[n-1-j][i]=matrix[n-1-i][n-1-j]
                matrix[n-1-i][n-1-j]=matrix[j][n-1-i]
                matrix[j][n-1-i]=tmp
