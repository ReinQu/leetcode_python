"""
给你一个 无重复元素 的整数数组 candidates 和一个目标整数 target ，找出 candidates 中可以使数字和为目标数 target 的 所有 不同组合 ，并以列表形式返回。你可以按 任意顺序 返回这些组合。
candidates 中的 同一个 数字可以 无限制重复被选取 。如果至少一个数字的被选数量不同，则两种组合是不同的。 
对于给定的输入，保证和为 target 的不同组合数少于 150 个。
"""
class Solution:#使用全排列同样的思想，剪枝回溯
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        def backtrack(state:list[int],target:int,choices:list[int],start:int,res:list[list[int]])->None:
            if target==0:
                res.append(list(state))
                return


            #剪枝二：从start开始遍历
            for i in range(start,len(choices)):
                #剪枝一：若子集和已经超过target就结束
                if target-choices[i]<0:
                    break
                #尝试：做出选择，更新target，start
                state.append(choices[i])
                #进行下一轮选择
                backtrack(state,target-choices[i],choices,i,res)
                #恢复：撤销选择
                state.pop()

        state=[]
        candidates.sort()
        start=0
        res=[]
        backtrack(state,target,candidates,start,res)
        return res




