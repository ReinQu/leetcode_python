"""
1.两数之和

给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 target  的那 两个 整数，并返回它们的数组下标。
你可以假设每种输入只会对应一个答案，并且你不能使用两次相同的元素。
你可以按任意顺序返回答案。
"""
class Solution1:#暴力枚举，非重点解法，时间复杂度O(n^2)
    def twoSum(self, nums: list[int], target: int) -> list[int]:#self不用管，函数需要传入一个nums，target并输出一个list型的返回
        n=len(nums)#获取数组的长度
        for i in range(n):
            for j in range(i+1,n):
                if nums[i]+nums[j]==target:
                    return [i,j]


        return [] #最后返回空，保持结构完整


class Solution2:#哈希表，重点解法，
    def twoSum(self,nums:list[int],target:int)->list[int]:
        hashtable=dict()#建立一个空字典
        for i,num in enumerate(nums):#遍历数组的下标和元素，并在后续加入到字典
            if target-num in hashtable:
                return [hashtable[target-num],i]
            hashtable[nums[i]]=i#没有就加进去，形式为{元素：下标，...}

        return []

def main():
    nums=[2,3,5,6]
    target=8
    solution=Solution2()
    result=solution.twoSum(nums,target)
    print("答案：",result)

#如果这个 Python 文件是直接运行的，就执行 main()。这是 Python 中非常常见的主函数写法。
if __name__=="__main__":
    main()