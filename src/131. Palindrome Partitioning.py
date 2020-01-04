class Solution:
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        s = [i for i in s]
        sol = []
        def helper(ss):
            if ss not in sol:
                sol.append(ss)
            for i in range(1, len(ss)-1):
                if ss[i-1] == ss[i+1]:
                    helper(ss[:i-1]+[ss[i-1]+ss[i]+ss[i+1]]+ss[i+2:])
            for i in range(1, len(ss)):
                if ss[i-1] == ss[i]:
                    helper(ss[:i-1]+[ss[i-1]+ss[i]]+ss[i+1:])
        helper(s)
        return sol
# 基本上时间很大了，用回溯法可能更好，直接使用 if s==s[::-1]判断回文可能更好