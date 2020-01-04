class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        import string
        table = str.maketrans('','',string.punctuation+' ')
        s = s.translate(table).lower()
        for i in range(len(s)//2):
            if s[i]!=s[-(i+1)]:
                return False
        return True
            