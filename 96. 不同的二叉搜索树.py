"""
给定一个整数 n，求以 1 ... n 为节点组成的二叉搜索树有多少种？
"""
# 转移函数也可以是求和的类型，如下：
# 这个可能需要预先分析
# G(n)= ∑G(i-1)G(n-i)

class Solution:
    def numTrees(self, n: int) -> int:
        G = [1, 1] + [0] * (n - 1)
        for i in range(2, n+1):
            for j in range(1, i+1):
                G[i] += G[j-1] * G[i-j]
        return G[-1]