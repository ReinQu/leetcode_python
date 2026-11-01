"""
给你一个字符串 s，找到 s 中最长的 回文 子串。
"""
class Solution:#中心扩散法
    def longestPalindrome(self, s: str) -> str:
        n=len(s)
        ans_left=ans_right=0

        #奇回文串
        for i in range(n):
            l=r=i
            while l>=0 and r<n and s[l]==s[r]:
                l-=1
                r+=1

            if r-l-1>ans_right-ans_left+1:
                ans_left,ans_right=l+1,r-1#相当于回溯的功能

        #偶回文串
        for i in range(n-1):
            l,r=i,i+1
            while l>=0 and r<n and s[l]==s[r]:
                l-=1
                r-=1
            if r-l-1>ans_right-ans_left+1:
                ans_left,ans_right=l+1,r-1

        return s[ans_left:ans_right+1]