"""
给定两个大小分别为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。请你找出并返回这两个正序数组的 中位数 。
算法的时间复杂度应该为 O(log (m+n)) 。
"""
from math import inf
class Solution:#二分查找+划分数组：把原数组划分成两个数组，使左边数组的数字都不大于右边数组的数字
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        if len(nums1)>len(nums2):
            nums1,nums2=nums2,nums1#保证nums1是最短数组，我们只对nums1进行二分，这样最小化时间复杂度
        m,n=len(nums1),len(nums2)
        left,right=0,m#闭区间：但为什么right是m？答：我们找的是切分位置
        while left<=right:
            #i+j=(m+n+1)//2:如果是m+n是奇数，左侧分到的多
            i=(left+right)//2#确定nums1分到左侧数组的个数i
            j=(m+n+1)//2-i#确定nums2分到左侧数组的个数j
            ai=nums1[i-1] if i>0 else -inf#ai是num1切分位置的左侧最大值
            ai1=nums1[i] if i<m else inf#ai1是num1切分位置的右侧最小值
            bj=nums2[j-1] if j>0 else -inf#inf是防止数组越界的情况
            bj1=nums2[j] if j<n else inf

            #我们希望切分后，左侧数组的所有值小于右侧数组的所有值
            if ai<=bj1 and bj<=ai1:
                max1=max(ai,bj)
                min2=min(ai1,bj1)
                if (m+n)%2==1:return max1
                else:return (max1+min2)/2
            
            elif ai>bj1:#num1左侧的最大值大于num2右边的最小值，需要把a的切分位置向左移动，二分查找
                right=i-1
            else:
                left=i+1