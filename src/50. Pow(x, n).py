"""
实现 pow(x, n) ，即计算 x 的 n 次幂函数。
"""
#  分情况讨论
#  一个递归二分法，复杂度O(logn)
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            return self.myPow(1/x, -n)
        if n == 0:
            return 1
        if n % 2:
            return self.myPow(x*x, n // 2) * x
        else:
            return self.myPow(x*x, n // 2)