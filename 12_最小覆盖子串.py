"""
给定两个字符串 s 和 t，长度分别是 m 和 n，返回 s 中的 最短窗口 子串，使得该子串包含 t 中的每一个字符（包括重复字符）。如果没有这样的子串，返回空字符串 ""。
测试用例保证答案唯一。
"""
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        #统计t中各字母出现次数
        need={}
        for char in t:
            need[char]=need.get(char,0)+1#如果原来的char有值就不变，没值就变为0
        window={}
        left=0
        have=0
        need_count=len(need)

        min_len=float('inf')#把其初始化为正无穷大
        result=""
        for right,char in enumerate(s):
            if char in need:
                window[char]=window.get(char,0)+1

                if window[char]==need[char]:
                    have+=1
            while have==need_count:
                if right-left+1<min_len:
                    min_len=right-left+1
                    result=s[left:right+1]

                left_char=s[left]

                if left_char in need:
                    window[left_char]-=1

                    if window[left_char]<need[left_char]:
                        have-=1
                left+=1
        return result




        

