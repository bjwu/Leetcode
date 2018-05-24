class Solution:
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        revlist=[]
        for i in range(len(s)):
            revlist.append(s[-(i+1)])
        return ''.join(revlist)


############## More simple #############
# return s[::-1]