"""
给定两个字符串 s 和 p，找到 s 中所有 p 的 异位词 的子串，返回这些子串的起始索引。不考虑答案输出的顺序。
"""
class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        result=list()
        left,n=0,len(p)
        dic_p={}
        dic_s={}
        for i,char in p:
            if char not in dic_p:
                dic_p[char]=1
            else:
                dic_p[char]+=1
        
        return result
        

        
