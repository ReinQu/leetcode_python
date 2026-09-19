"""
给你一个字符串数组，请你将 字母异位词 组合在一起。可以按任意顺序返回结果列表。
"""

import collections
class Solution1:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        mp=collections.defaultdict(list)#工具箱到特殊字典到类型，如果mp中没有k，可以建立一个空值[]
        for st in strs:
            key="".join(sorted(st))
            mp[key].append(st)

        return list(mp.values())#mp.values()返回所有的键值，list转换为list类型
class Solution2:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        d={}
        for st in strs:
            key="".join(sorted(st))
            if key not in d:
                d[key]=[]
            d[key].append(st)
        return list(d.values())

def main():
    strs= ["eat", "tea", "tan", "ate", "nat", "bat"]
    sol1=Solution1()
    sol2=Solution2()
    result1=sol1.groupAnagrams(strs)
    result2=sol2.groupAnagrams(strs)
    print(result1)
    print(result2)


if __name__=="__main__":
    main()

