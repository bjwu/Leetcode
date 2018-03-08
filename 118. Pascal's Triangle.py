class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows==0:
            return []
        elif numRows==1:
            return [[1]]
        else:
            result=[[1],[1,1]]
            for i in range(2,numRows):
                result.append(list(result[i-1]))
                result[i].append(1)
                for j in range(1,i):
                    result[i][j]=result[i-1][j-1]+result[i-1][j]
            return result


Solu=Solution()
s=Solu.generate(5)


