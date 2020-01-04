class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        nbin = bin(n)
        nbinlist = nbin[:2] + nbin[2:][::-1] + '0'*(32+2-len(nbin))
        return int(nbinlist, 2)
        

# 几个函数：
# python3 `zfill( )` 方法：str.zfill(width) 方法返回指定长度的字符串，原字符串右对齐，前面填充0。

class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        oribin='{0:032b}'.format(n)
        reversebin=oribin[::-1]
        return int(reversebin,2)

# 另：python3 中的format格式化函数可以了解一下