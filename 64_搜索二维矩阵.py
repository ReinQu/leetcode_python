"""
给你一个满足下述两条属性的 m x n 整数矩阵：
每行中的整数从左到右按非严格递增顺序排列。
每行的第一个整数大于前一行的最后一个整数。
给你一个整数 target ，如果 target 在矩阵中，返回 true ；否则，返回 false 。
你必须编写一个时间复杂度为 O(log(m * n)) 的解决方案。
"""
class Solution:#mid是展开的一维数组的中间值，其对应的行下标为mid//n；对应的列下标是mid%n
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        m,n=len(matrix),len(matrix[0])
        left,right=0,m*n-1
        while left<=right:
            mid=(left+right)//2
            x=matrix[mid//n][mid%n]
            if x==target:
                return True
            if x<target:
                left=mid+1
            else:right=mid-1

        return False
