"""
给你一个非负整数数组 nums ，你最初位于数组的 第一个下标 。数组中的每个元素代表你在该位置可以跳跃的最大长度。
判断你是否能够到达最后一个下标，如果可以，返回 true ；否则，返回 false 。
"""
class Solution:#用mx维护最长下标，如果i>mx，中断
    def canJump(self, nums: list[int]) -> bool:
        mx=0
        for i,num in enumerate(nums):
            if i>max:return False
            mx=max(mx,i+num)
        return True
                    

