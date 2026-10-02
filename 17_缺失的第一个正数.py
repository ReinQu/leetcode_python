"""
给你一个未排序的整数数组 nums ，请你找出其中没有出现的最小的正整数。
请你实现时间复杂度为 O(n) 并且只使用常数级别额外空间的解决方案。
"""
#核心：只关心1到n

class Solution1:#哈希表，按照1到n的顺序开始检查，若没有，就是答案，空间复杂度o(n)
    def firstMissingPositive(self, nums: list[int]) -> int:
        num_set=set(nums)#变为字典
        n=len(nums)
        for i in range(1,n+1):
            if i not in num_set:
                return i
        return n+1
class Solution2:#置换：数字x应该在下标x-1的位置，空间复杂度o(1)
    def firstMissingPositive(self, nums: list[int]) -> int:
        n=len(nums)

        for i in range(n):
            while 1<=nums[i]<=n and nums[nums[i]-1]!=nums[i]:
                nums[nums[i]-1],nums[i]=nums[i],nums[nums[i]-1]
        for i in range(n):
            if nums[i]!=i+1:
                return i+1
        return n+1
        