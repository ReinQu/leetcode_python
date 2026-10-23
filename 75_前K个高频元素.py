"""
给你一个整数数组 nums 和一个整数 k ，请你返回其中出现频率前 k 高的元素。你可以按 任意顺序 返回答案。
"""
class Solution1:#普通做法：排序加遍历
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        nums.sort()
        count=1
        p=[]
        for i in range(len(nums)):
            if i==len(nums)-1 or nums[i+1]!=nums[i] :
                p.append((nums[i],count))
                count=1
            else:
                count+=1
        p.sort(key=lambda x:x[1])
        return [x[0] for x in p[-k:]]
from collections import Counter
class Solution2:#桶排序
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        cnt=Counter(nums)#Counter会统计每一个元素出现的次数
        max_cnt=max(cnt.values())

        buckets=[[] for _ in range(max_cnt+1)]
         
        for x,c in cnt.items():#x对应具体数字，c对应频次，cnt.items()会遍历每一组键值对
            buckets[c].append(x)

        ans=[]

        for bucket in reversed(buckets):
            ans+=bucket#这里不能用append，因为会出现[[]]的情况

            if len(ans)==k:
                return ans