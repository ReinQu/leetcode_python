"""
给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。
请注意 ，必须在不复制数组的情况下原地对数组进行操作。
"""
class Solution1:#如果不是0，则数字未来的下标是当前下标减去前面0的个数
    def moveZeroes(self, nums: list[int]) -> None:
        n=len(nums)
        count=0
        for i in range(n):

            if nums[i]!=0:
                nums[i],nums[i-count]=nums[i-count],nums[i]

            else:
                count+=1
class Solution2:#快慢指针：先用一个left一直指向0，right一直向后走，如果right不为0，就交换left和right
    def moveZeroes(self, nums: list[int])->None:
        n=len(nums)
        left=right=0
        while right<n:
            if nums[right]!=0:
                nums[right],nums[left]=nums[left],nums[right]
                left+=1
            right+=1

def main():
    sol1=Solution1()
    sol2=Solution2()
    nums=[0,1,0,3,12]
    print(nums)
    sol2.moveZeroes(nums)
    print(nums)

if __name__=="__main__":
    main()

       

                    