"""
给你一个按照非递减顺序排列的整数数组 nums，和一个目标值 target。请你找出给定目标值在数组中的开始位置和结束位置。
如果数组中不存在目标值 target，返回 [-1, -1]。
你必须设计并实现时间复杂度为 O(log n) 的算法解决此问题。
"""
class Solution:
    #lower_bound返回>=target的最小下标i
    def lower_bound(self,nums:list[int],target:int)->int:
        left,right=0,len(nums)-1
        while left<=right:
            mid=(left+right)//2
            #原left到mid走过的一定小于target，原right到mid走过的一定大于等于target，直到结束循环，left=right+1,此时right+1>=target
            if nums[mid]>=target:
                right=mid-1
            else:
                left=mid+1
        return left
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        start=self.lower_bound(nums,target)
        if start==len(nums) or nums[start]!=target:#因为数组空返回的是len，找不到也会返回一个值，而且这两个判断条件的顺序也不能换
            return [-1,-1]
        end=self.lower_bound(nums,target+1)-1
        return [start,end]
