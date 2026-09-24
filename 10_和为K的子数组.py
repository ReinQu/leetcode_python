"""
给你一个整数数组 nums 和一个整数 k ，请你统计并返回 该数组中和为 k 的子数组的个数 。
子数组是数组中元素的连续非空序列。
"""
class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        count=0
        prefix_count=0
        mp={0:1}
        for num in nums:
            prefix_count+=num

            if prefix_count-k in mp:
                count+=mp[prefix_count-k]

            if prefix_count in mp:
                mp[prefix_count]+=1
            else:
                mp[prefix_count]=1

        return count
def main():
    nums=[1,1,1]
    k=2
    sol=Solution()
    print(sol.subarraySum(nums,k))

if __name__=="__main__":
    main()
            
