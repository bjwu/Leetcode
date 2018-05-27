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