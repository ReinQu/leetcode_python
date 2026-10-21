"""
给定一个经过编码的字符串，返回它解码后的字符串。
编码规则为: k[encoded_string]，表示其中方括号内部的 encoded_string 正好重复 k 次。注意 k 保证为正整数。
你可以认为输入字符串总是有效的；输入字符串中没有额外的空格，且输入的方括号总是符合格式要求的。
此外，你可以认为原始数据不包含数字，所有的数字只表示重复的次数 k ，例如不会出现像 3a 或 2[4] 的输入。
测试用例保证输出的长度不会超过 105。
"""
class Solution:#单栈
    def decodeString(self, s: str) -> str:
        stk=[]
        for ch in s:
            if ch!=']':#只要不是]就进栈
                stk.append(ch)
                continue

            #对字母部分做处理，放在sub中
            sub=""
            while stk[-1]!='[':
                sub=stk.pop()+sub
            #处理[
            stk.pop()

            #处理数字部分，因为有可能是多位数
            k,base=0,1
            while stk and stk[-1].isdigit():
                k+=int(stk.pop())*base
                base*=10

            stk.append(sub*k)

        return ''.join(stk)
