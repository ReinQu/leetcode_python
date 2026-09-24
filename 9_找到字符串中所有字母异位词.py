"""
给定两个字符串s和p，找到s中所有p的异位词的子串，返回这些子串的起始索引。不考虑答案输出的顺序。
"""
class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        s_len,p_len=len(s),len(p)
        result=[]
        if s_len<p_len:
            return []
        s_count=[0]*26
        p_count=[0]*26
        for i in range(p_len):
            s_count[ord(s[i])-97]+=1
            p_count[ord(p[i])-97]+=1
        if s_count==p_count:
            result.append(0)
        for i in range(s_len-p_len):
            s_count[ord(s[i])-97]-=1
            s_count[ord(s[i+p_len])-97]+=1

            if s_count==p_count:
                result.append(i+1)

        return result

def main():
    s = "cbaebabacd"
    p = "abc"
    sol=Solution()
    print(sol.findAnagrams(s,p))

if __name__=="__main__":
    main()


        
