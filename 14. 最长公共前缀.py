"""
编写一个函数来查找字符串数组中的最长公共前缀。

如果不存在公共前缀，返回空字符串 ""。
"""

# 水平扫描法
# LCP(S1,S2,...Sn) = LCP(LCP(LCP(S1, S2),S3)...Sn)

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        length = len(strs)
        if length==0:
            return ""
        currstr = strs[0]
        for i in range(1, length):
            nextstr = strs[i]
            comstr = ''
            for j in range(min(len(currstr), len(nextstr))):
                if currstr[j] == nextstr[j]:
                    comstr += currstr[j]
                else:
                    break
            if not comstr:
                return ""
            currstr = comstr
        return currstr
