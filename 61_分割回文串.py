"""
给你一个字符串 s，请你将 s 分割成一些 子串，使每个子串都是 回文串 。返回 s 所有可能的分割方案。
"""
class Solution:#如何判断回文：t==t[::-1]
    def partition(self, s: str) -> list[list[str]]:
        n=len(s)
        ans=[]
        path=[]


        def dfs(i:int)->None:
            if i==n:
                ans.append(list(path))
                return

            for j in range(i,n):
                t=s[i:j+1]
                if t==t[::-1]:
                    path.append(t)
                    dfs(j+1)
                    path.pop()

        dfs(0)
        return ans
