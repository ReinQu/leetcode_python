"""
给你一个整数数组 nums ，请你找出数组中乘积最大的非空连续 子数组（该子数组中至少包含一个数字），并返回该子数组所对应的乘积。
测试用例的答案是一个 32-位 整数。
请注意，一个只包含一个元素的数组的乘积是这个元素的值。
"""
from math import inf
class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        ans=-inf
        f_max=f_min=1
        for x in nums:
            #这一定是连续子数组，因为f_max，f_min维护了连续性
            f_max,f_min=max(f_max*x,f_min*x,x),min(f_max*x,f_min*x,x)
            ans=max(ans,f_max)
        return ans