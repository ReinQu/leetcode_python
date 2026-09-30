"""
给你一个整数数组 nums ，请你找出一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
子数组是数组中的一个连续部分。
"""

class Solution1:#动态规划，这是自己写对的，时间复杂度O(n)
    def maxSubArray(self, nums: list[int]) -> int:
        result=[nums[0]]
        pre_max=nums[0]
        for i in range(1,len(nums)):
            curr=max(pre_max+nums[i],nums[i])
            result.append(curr)
            pre_max=curr
        return max(result)


class Solution2:#分治法，折中，这里不好用
    def maxSubArray(self, nums: list[int]) -> int: