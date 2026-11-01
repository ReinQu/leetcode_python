"""
给你两个单词 word1 和 word2， 请返回将 word1 转换成 word2 所使用的最少操作数  。
你可以对一个单词进行如下三种操作：
插入一个字符
删除一个字符
替换一个字符
"""
from functools import cache
class Solution:#对word1操作和对word2操作其实是一样的，所以我们以其中一个为基准就行了
    def minDistance(self, word1: str, word2: str) -> int:
        m,n=len(word1),len(word2)
        @cache
        def dfs(i:int,j:int)->int:
            if i<0:#此时word1到底例如(-1,2)那就需要插入三个字符
                return j+1
            if j<0:#同上
                return i+1
            if word1[i]==word2[j]:
                return dfs(i-1,j-1)
            #操作1：删除word1[i]；操作2：插入使word1[i]等于word2[j]；操作三：word1[i]替换为word2[j]
            return min(dfs(i-1,j),dfs(i,j-1),dfs(i-1,j-1))+1
        return dfs(m-1,n-1)