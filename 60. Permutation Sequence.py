class Solution:
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        ## 计算阶乘
        from functools import reduce
        jiecheng = reduce(lambda x,y:x*y,range(1,n+1))
        ## 元素list
        allletters = [str(i) for i in range(1,n+1)]
        # 从左到右确定每一位
        output = ''
        k -= 1
        for i in range(n, 0, -1):
            jiecheng = int(jiecheng / i)
            output += allletters.pop(k//jiecheng)
            k = k % jiecheng
        return output
        