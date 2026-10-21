"""
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s ，判断字符串是否有效。
有效字符串需满足：
左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
每个右括号都有一个对应的相同类型的左括号。
"""
class Solution:#栈＋哈希表
    def isValid(self, s: str) -> bool:
        if len(s)%2==1:
            return False
        tmp=[]
        mp={')':'(',']':'[','}':'{'}
        for c in s:
            if c not in mp:#c是左
                tmp.append(c)
            elif not tmp or mp[c]!=tmp.pop():
                return False
        return not tmp#为什么不直接返回true？答：假如是(()的情况，也不会返回False，这时tmp当中有一个(
