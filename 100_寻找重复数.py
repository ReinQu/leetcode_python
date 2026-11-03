"""
给定一个包含 n + 1 个整数的数组 nums ，其数字都在 [1, n] 范围内（包括 1 和 n），可知至少存在一个重复的整数。
假设 nums 只有 一个重复的整数 ，返回 这个重复的数 。
你设计的解决方案必须 不修改 数组 nums 且只用常量级 O(1) 的额外空间。
"""
class Solution1:#暴力
    def findDuplicate(self, nums: list[int]) -> int:
        nums.sort()
        i=0
        while nums[i]<nums[i+1]:
            i+=1
        return nums[i]

class Solution:#有向图
    def findDuplicate(self, nums: list[int]) -> int:
        slow=fast=0
        while True:
            slow=nums[slow]#等价于slow=slow.next
            fast=nums[nums[fast]]#等价于fast.next.next
            if slow==fast:
                break

        head=0
        while slow!=head:
            slow=nums[slow]
            head=nums[head]
        return slow
