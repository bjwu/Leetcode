class Solution:
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 这是一个DP问题
        # 每次新增一个数字，如果这个数字可以跟之前的最后一位组合<26，那么子问题只跟间隔的问题相关，否则，只跟相邻的子问题题相关
        if s == '':
            return 0
        dp = [0] * (len(s)+1)   
        dp[0] = 1
        for i in range(1, len(s)+1):
            if s[i-1] != "0":
                dp[i] += dp[i-1]
            if i != 1 and s[i-2:i] < "27" and s[i-2:i] > "09":  #这一句就已经剔除了string里有0且前面一个数>2的情况
                dp[i] += dp[i-2]
        return dp[len(s)]
        