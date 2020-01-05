"""
给定一个字符串，请你找出其中不含有重复字符的最长子串的长度。
"""

###
# 动态规划问题，主要是选好子问题，该子问题选取的是以第i个字符为结尾的不包含重复字符的子字符串的最长长度，
# 而不是全局的最长长度，这一点很重要。
#
# 更新：不应该说是个动态规划问题，而是个滑动窗口问题，
# 每次关注的是上一个元素结尾的最大长度的字符串与当前元素合并后的情况
###


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = [0] * (len(s) + 1)  # 每一个元素储存以该元素结尾的最大子串
        sset= set()  # 储存当前滑动窗口的字符
        # 双指针滑动窗口 [i, j)
        i = 0
        for j in range(len(s)):  
            if s[j] not in sset:
                res[j] = res[j-1] + 1
                sset.add(s[j])
            else:
                while s[i] != s[j]:
                    sset.remove(s[i])     
                    i += 1
                res[j] = j - i
                i += 1
        return max(res)