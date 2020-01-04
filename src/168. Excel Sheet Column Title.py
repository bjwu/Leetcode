class Solution:
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        import string
        if n==0:return ''
        dict = string.ascii_uppercase
        out = []
        while n >= 26:
            out.append(dict[(n-1)%26])
            n = (n-1) // 26
        if n!=0:
            out.append(dict[n-1])
        return ''.join(out)[::-1]
            
        