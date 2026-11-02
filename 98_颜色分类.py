"""
给定一个包含红色、白色和蓝色、共 n 个元素的数组 nums ，原地 对它们进行排序，使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。
我们使用整数 0、 1 和 2 分别表示红色、白色和蓝色。
必须在不使用库内置的 sort 函数的情况下解决这个问题。
"""
class Solution:#插入排序，两个指针p0、p1
    def sortColors(self, nums: list[int]) -> None:
        #p0,p1分别维护1和0的边界
        p0=p1=0
        for i,x in enumerate(nums):
            nums[i]=2
            if x<=1:
                nums[p1]=1
                p1+=1
            if x==0:
                nums[p0]=0
                p0+=1
