"""
给定一个未排序的整数数组 nums ，找出数字连续的最长序列（不要求序列元素在原数组中连续）的长度。
请你设计并实现时间复杂度为 O(n) 的算法解决此问题。
"""
class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        numset=set(nums)#这里题目限定了时间复杂度，set的时间复杂度为O(1)
        longest_streak=0
        for num in numset:
            if num-1 not in numset:
                curr=num
                current_streak=1

                while curr+1 in numset:
                    curr+=1
                    current_streak+=1
                longest_streak=max(longest_streak,current_streak)

        return longest_streak


        



