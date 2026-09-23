"""
给定一个字符串 s ，请你找出其中不含有重复字符的 最长 子串 的长度。
"""
class Solution:#滑动窗口，哈希表
    def lengthOfLongestSubstring(self, s: str) -> int:
        left,result=0,0
        dic={}
        for right,char in enumerate(s):
            if char in dic:
                left=max(left,dic[char]+1)

            dic[char]=right
            result=max(result,right-left+1)

        return result

def main():
    s = "abcabcbb"
    sol=Solution()
    print(sol.lengthOfLongestSubstring(s))

if __name__=="__main__":
    main()

