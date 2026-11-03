"""
整数数组的一个 排列  就是将其所有成员以序列或线性顺序排列。
例如，arr = [1,2,3] ，以下这些都可以视作 arr 的排列：[1,2,3]、[1,3,2]、[3,1,2]、[2,3,1] 。
整数数组的 下一个排列 是指其整数的下一个字典序更大的排列。更正式地，如果数组的所有排列根据其字典顺序从小到大排列在一个容器中，那么数组的 下一个排列 就是在这个有序容器中排在它后面的那个排列。如果不存在下一个更大的排列，那么这个数组必须重排为字典序最小的排列（即，其元素按升序排列）。
例如，arr = [1,2,3] 的下一个排列是 [1,3,2] 。
类似地，arr = [2,3,1] 的下一个排列是 [3,1,2] 。
而 arr = [3,2,1] 的下一个排列是 [1,2,3] ，因为 [3,2,1] 不存在一个字典序更大的排列。
给你一个整数数组 nums ，找出 nums 的下一个排列。
必须 原地 修改，只允许使用额外常数空间
"""
class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
        n=len(nums)
        #第一步：从右到左找到第一个小于num[i+1]的nums[i]
        i=n-2
        while i>=0 and nums[i]>=nums[i+1]:#i>=0不能丢，否则会超出数组边界
            i-=1
        #如果找到了，进入第二步，否则直接进入第三步
        if i>=0:
            #第二步：从右到左找到nums[i]右边最小的大于nums[i]的数nums[j]
            j=n-1 
            while nums[j]<=nums[i]:
                j-=1
            nums[i],nums[j]=nums[j],nums[i]
        #第三步：翻转nums[i+1:]
        left,right=i+1,n-1
        while left<right:
            nums[left],nums[right]=nums[right],nums[left]
            left+=1
            right-=1