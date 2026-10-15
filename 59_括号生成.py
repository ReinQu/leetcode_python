"""
数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。
"""
#本质上来说，我们需要在 0,1,2,…,2n−1 中选 n 个数（位置），填入左括号。其余 n 位置填入右括号。
#对于括号字符串的任意前缀，右括号的个数不能超过左括号的个数。
class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        ans=[]
        path=['']*(n*2)

        def dfs(left:int,right:int)->None:
            if right==n:
                ans.append(''.join(path))
                return
            if left<n:#可以填左括号
                path[left+right]='('#直接覆盖
                dfs(left+1,right)
            if right<left:
                path[left+right]=')'
                dfs(left,right+1)
        dfs(0,0)
        return ans


