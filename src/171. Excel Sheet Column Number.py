class Solution:
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        out = 0
        for i, a in enumerate(s[::-1]):
            out += (ord(a)-64) * 26**i
        return out
            