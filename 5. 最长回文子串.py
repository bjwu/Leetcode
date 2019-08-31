"""
给定一个字符串 s，找到 s 中最长的回文子串。
"""
##########################
# 子问题： P(i,j)= (P(i+1,j−1) and S(i)==S(j))
# 对于字符串问题，如用动态规划的话，最好采用二阶矩阵，横坐标和纵坐标分别表示字符串首尾位置


# 动态规划 
class Solution:
    def longestPalindrome(self, s: str) -> str:
        # 建立下三角矩阵，横坐标和纵坐标分别表示字符串首尾位置。
        memo = [[False] * i + [True]*2 for i in range(len(s))] 
        for j, row in enumerate(memo):
            for i, ele in enumerate(row):
                if not ele:
                    if memo[j-1][i+1] and s[i] == s[j]:
                        memo[j][i] = True
        # 从矩阵的True中得出最大长度
        maxlen = -1
        p1, p2 = 0, 0
        for j, row in enumerate(memo):
            for i in range(len(row)-1):
                if memo[j][i] and abs(i-j)>maxlen:
                    p1, p2 = i, j  
                    maxlen = abs(i-j)
        return s[p1:(p2+1)]

# 其实该题后半部分可以省略，只需要在开始的遍历过程中注意顺序就行
# 见下面2018年版



##################################### 
# 2018年版

class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) <= 1:
            return s
        ## Initialization
        import numpy as np
        memo = np.tri(len(s), len(s), 0)
        ## DP
        ri = rj = 0
        for k in range(1, len(s)):
            for i in range(len(s) - k):
                j = i + k
                if s[i] == s[j]:
                    if memo[i+1][j-1]:
                        memo[i][j] = 1
                        ri, rj = i, j
        return s[ri:rj+1]

#         这个题目居然困扰了我两天：
# 我的方法是一个DP方法，建立了一个len(s)✖️len(s)的矩阵memo。其index i和j分别表示取得的substring的[i...j]的值。若[i...j]为回文，则对应的矩阵元素为1，反之为0。
# 遍历的路线是根据substring的长度。

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