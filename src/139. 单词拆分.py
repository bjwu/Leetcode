"""
给定一个非空字符串 s 和一个包含非空单词列表的字典 wordDict，判定 s 是否可以被空格拆分为一个或多个在字典中出现的单词。
"""


# 暴力求解，递归
# 由于子问题大量重复，这个会造成时间limit
class Solution:
    def wordBreak(self, s, wordDict) -> bool:
        def helper(ss):
            if not ss:
                return True
            memo = []
            for i in range(len(ss)):
                if ss[:i+1] in wordDict:
                    memo.append(helper(ss[i+1:]))
            return any(memo)
        return helper(s)

# 动态规划
# 要储存一个数组border，数组保存所有的边界位置（正好可以满足要求的位置）
class Solution:
    def wordBreak(self, s, wordDict) -> bool:
        border =[0]
        for i in range(len(s)):
            if any([s[b:i+1] in wordDict for b in border]):
                border.append(i+1)
        return len(s) in border
