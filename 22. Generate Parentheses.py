# class Solution(object):
#     def generateParenthesis(self, N):
#         if N == 0: return ['']
#         ans = []
#         for c in range(N):
#             for left in self.generateParenthesis(c):
#                 for right in self.generateParenthesis(N-1-c):
#                     ans.append('({}){}'.format(left, right))
#         return ans
class Solution(object):
    def generateParenthesis(self, N):
        ans = []
        def backtrack(S = '', left = 0, right = 0):
            if len(S) == 2 * N:
                ans.append(S)
                return
            if left < N:
                backtrack(S+'(', left+1, right)
            if right < left:
                backtrack(S+')', left, right+1)

        backtrack()
        return ans

# 我个人是想用注释这一种，但是没有写出来。好好学习一下，这应该是DP算法，其实在代码中加一个memo的话我觉得时间消耗可能会更小一点。

# 另一种是提交的这种，这种方法没有重复的计算相同的子问题，我认为比上面这种方法效率要高。这应该是是一个典型树的生成。