"""
给定一个字符串，请你找出其中不含有重复字符的最长子串的长度。
"""

###
# 动态规划问题，主要是选好子问题，该子问题选取的是以第i个字符为结尾的不包含重复字符的子字符串的最长长度，
# 而不是全局的最长长度，这一点很重要。
###

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 储存字符遍历为止最近的位置
        pos = {}
        # ans的每个元素为以第i个字符为结尾的不包含重复字符的子字符串的最长长度
        # +1为了ans[-1]有效
        ans = [0] * (len(s) + 1)
        for i, ch in enumerate(s):
            # 如果第i个字符不包含在前面
            if ch not in pos:
                pos[ch] = i
                ans[i] = ans[i-1] + 1
            # 如果第i个字符包含在前面
            else:
                # 计算第i个字符和它上次出现在字符串中的位置的距离
                d = i - pos[ch]
                pos[ch] = i
                # 分两种情况讨论，
                if d <= ans[i-1]:
                    ans[i] = d
                else:
                    ans[i] = ans[i-1] + 1
        return max(ans)