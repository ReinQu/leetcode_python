"""
整数数组 nums 按升序排列，数组中的值 互不相同 。
在传递给函数之前，nums 在预先未知的某个下标 k（0 <= k < nums.length）上进行了 向左旋转，使数组变为 [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]（下标 从 0 开始 计数）。例如， [0,1,2,4,5,6,7] 下标 3 上向左旋转后可能变为 [4,5,6,7,0,1,2] 。
给你 旋转后 的数组 nums 和一个整数 target ，如果 nums 中存在这个目标值 target ，则返回它的下标，否则返回 -1 。
你必须设计一个时间复杂度为 O(log n) 的算法解决此问题。
"""
class Solution:#把旋转后的数组分成两段
    def search(self, nums: list[int], target: int) -> int:
        left,right=0,len(nums)-1
        while left<=right:
            mid=(left+right)//2
            x=nums[mid]

            if target>nums[-1]>=x:#target在第一段，mid在第二段
                right=mid-1
            elif x>nums[-1]>=target:#mid在第一段，target在第二段
                left=mid+1
            elif x>=target:#在同一段
                right=mid-1
            else:
                left=mid+1
        #和前一道一样left是>=target的最小下标
        return left if left<len(nums) and nums[left]==target else -1
