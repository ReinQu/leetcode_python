"""
给你一个整数数组 nums ，判断是否存在三元组 [nums[i], nums[j], nums[k]] 满足 i != j、i != k 且 j != k ，同时还满足 nums[i] + nums[j] + nums[k] == 0 。请你返回所有和为 0 且不重复的三元组。
注意：答案中不可以包含重复的三元组。
"""
class Solution:#思路：排序+固定+双指针+去重
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        n=len(nums)
        nums.sort()
        result=list()


        for first in range(n):
            if first>0 and nums[first]==nums[first-1]:#防止重复
                continue
            third=n-1
            target=-nums[first]
            for second in range(first+1,n):
                if second>first+1 and nums[second]==nums[second-1]:#防止重复
                    continue
                while second<third and nums[second]+nums[third]>target:
                    third-=1

                if second==third:
                    break
                if nums[third]+nums[second]==target:
                    result.append([nums[first],nums[second],nums[third]])

        return result

def main():
    nums = [-1,0,1,2,-1,-4]
    sol=Solution()
    print(sol.threeSum(nums))

if __name__=="__main__":
    main()

