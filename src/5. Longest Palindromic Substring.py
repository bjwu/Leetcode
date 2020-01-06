"""
给定一个字符串 s，找到 s 中最长的回文子串。
"""
##########################
# 子问题： P(i,j)= (P(i+1,j−1) and S(i)==S(j))
# 对于字符串问题，如用动态规划的话，最好采用二阶矩阵，横坐标和纵坐标分别表示字符串首尾位置


# 动态规划 
# 该类问题具体可见 ideas/shortcuts.md
class Solution:
    def longestPalindrome(self, s: str) -> str:
        leng = len(s)
        dp = [[0] * i + [1] * (leng - i + 1) for i in range(leng)]
        res = ""
        nres = len(res) # 目前最长的字符串长度
        for j in range(leng):  # j为字符串尾
            for i in range(j+1): # i为字符串头
                if s[i] == s[j] and dp[j-1][i+1] != 0:
                    dp[j][i] = j - i + 1
                if dp[j][i] > nres:
                    res = s[i: j+1]
                    nres = dp[j][i]
        return res



# 可是，这个方法消耗O(n^2)的时间，另一个方法令我倾佩。
# 这个方法根据这道题的特征来求解，对于string来说，每在后面增加一个char，回文的长度只有可能增加1或者2或者没有。
# ```
# class Solution:
#     # @return a string
#     def longestPalindrome(self, s):
#         if len(s)==0:
#         	return 0
#         maxLen=1
#         start=0
#         for i in range(len(s)):
#         	if i-maxLen >=1 and s[i-maxLen-1:i+1]==s[i-maxLen-1:i+1][::-1]:
#         		start=i-maxLen-1
#         		maxLen+=2
#         		continue

#         	if i-maxLen >=0 and s[i-maxLen:i+1]==s[i-maxLen:i+1][::-1]:
#         		start=i-maxLen
#         		maxLen+=1
#         return s[start:start+maxLen]
# 	```