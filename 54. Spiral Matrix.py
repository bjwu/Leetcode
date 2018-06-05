class Solution:
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if matrix == []:
            return []
        import numpy as np
        r, l, lenr, lenl = 0, 0, np.shape(matrix)[0]-1, np.shape(matrix)[1]-1
        output = []
        while r <= lenr and l <= lenl:
            output.extend(matrix[r][l:lenl+1])
            r = r+1
            for i in range(r, lenr+1):
                output.append(matrix[i][lenl])
            lenl = lenl-1
            if r > lenr or l > lenl:
                break
            output.extend(matrix[lenr][l:lenl+1][::-1])
            lenr = lenr-1
            for j in range(lenr,r-1,-1):
                output.append(matrix[j][l])
            l = l+1
        return output