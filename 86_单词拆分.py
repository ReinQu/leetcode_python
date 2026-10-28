"""
给你一个字符串 s 和一个字符串列表 wordDict 作为字典。如果可以利用字典中出现的一个或多个单词拼接出 s 则返回 true。
注意：不要求字典中出现的单词全部都使用，并且字典中的单词可以重复使用。
"""
class Solution:#这个做法错的，如果是下面的案例就行不通
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        tmp=""
        for c in s:
            tmp+=c
            ans=-1
            if tmp in wordDict:
                tmp=""
                ans=1
        return True if ans==1 else False
from functools import cache
class Solution1:#记忆化搜索
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        max_len=max(map(len,wordDict))#map()输出每个单词的长度
        words=set(wordDict)#set()去除重复值
        @cache
        def dfs(i:int)->bool:#i是字符串的结束位置，左闭右开
            #拆分成功
            if i==0:return True
            #i-1是最后边的下标，i-max_len是单词的最小起始位置
            for j in range(i-1,max(i-max_len-1,-1),-1):#max中要保证结果最少是-1，否则会超出边界
                if s[j:i] in words and dfs(j):
                    return True
            return False
        return dfs(len(s))

def main():
    sol=Solution()
    s ="aaaaaaa"
    wordDict =["aaaa","aaa"]
    print(sol.wordBreak(s,wordDict))

if __name__=="__main__":
    main()