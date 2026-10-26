"""
给你一个字符串 s 。我们要把这个字符串划分为尽可能多的片段，同一字母最多出现在一个片段中。例如，字符串 "ababcc" 能够被分为 ["abab", "cc"]，但类似 ["aba", "bcc"] 或 ["ab", "ab", "cc"] 的划分是非法的。
注意，划分结果需要满足：将所有划分结果按顺序连接，得到的字符串仍然是 s 。
返回一个表示每个字符串片段的长度的列表。
"""
class Solution:
    def partitionLabels(self, s: str) -> list[int]:
        last={c:i for i,c in enumerate(s)}#每个字母最后出现的下标
        ans=[]
        start=end=0
        for i,c in enumerate(s):
            end=max(end,last[c])
            if end==i:
                ans.append(end-start+1)
                start=end+1
        return ans