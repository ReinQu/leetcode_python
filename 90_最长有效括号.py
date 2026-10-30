"""
给你一个只包含 '(' 和 ')' 的字符串，找出最长有效（格式正确且连续）括号 子串 的长度。
左右括号匹配，即每个左括号都有对应的右括号将其闭合的字符串是格式正确的，比如 "(()())"。
"""
class Solution:#栈
    def longestValidParentheses(self, s: str) -> int:
        st=[-1]#栈底存无法匹配的右括号的下标,-1兼容第一个就是左括号的s
        ans=0
        for i,c in enumerate(s):
            if c=='(':
                st.append(i)
            elif len(st)>1:#右括号且栈里有左括号
                st.pop()
                ans=max(ans,i-st[-1])#从st[-1]+1到i都是有效的
            else:#s[i]是永远无法匹配的右括号
                st[0]=i

        return ans