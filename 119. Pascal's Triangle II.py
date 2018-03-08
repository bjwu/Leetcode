import math
class Solution:
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        result=[1 for _ in range(rowIndex+1)]
        for iter in range(2,rowIndex+1):
            temp=result[1]
            result[1]=iter
            for index in range(2,iter):
                result[index],temp=result[index]+temp,result[index]
        return result

Solu=Solution()
s=Solu.getRow(8)
