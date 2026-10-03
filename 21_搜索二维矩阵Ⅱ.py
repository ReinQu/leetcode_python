"""
编写一个高效的算法来搜索 m x n 矩阵 matrix 中的一个目标值 target 。该矩阵具有以下特性：
每行的元素从左到右升序排列。
每列的元素从上到下升序排列。
"""
class Solution:#搜索二叉树，贪心算法，将矩阵逆时针旋转45°，得到一颗类似向左边小、向右变大的二叉树
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        i,j=len(matrix)-1,0#从左下角开始
        while i>=0 and j<len(matrix[0]):
            if matrix[i][j]<target:j+=1
            elif matrix[i][j]>target:i-=1
            else:return True
        return False




