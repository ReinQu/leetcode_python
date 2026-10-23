"""
给定整数数组 nums 和整数 k，请返回数组中第 k 个最大的元素。
请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。
你必须设计并实现时间复杂度为 O(n) 的算法解决此问题。
"""
class Solution1:#排序
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort()
        return nums[len(nums)-k]

    
import random
class Solution2:#快速选择：哨兵划分＋递归，最难的还是怎么排序
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def quick_select(nums,k):

            pivot=random.choice(nums)
            big,equal,small=[],[],[]
            #将大于、小于、等于pivot的元素划分至big，small，equal
            for num in nums:
                if num>pivot:
                    big.append(num)
                elif num<pivot:
                    small.append(num)
                else:
                    equal.append(num)
            #第k大的元素在big中
            if k<=len(big):
                return quick_select(big,k)#因为是从大到小排序，所以还是第k个
            #第k大的元素在small中
            if len(nums)-len(small)<k:
                return quick_select(small,k-len(nums)+len(small))#等效k-len(big)-len(equal)
            
            return pivot
        return quick_select(nums,k)

#如果k<=len(big)，就会进入big；如果k>len(big)+len(equal)就会进入small；最后就是equal