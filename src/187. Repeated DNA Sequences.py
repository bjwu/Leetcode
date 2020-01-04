class Solution:
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        path = set()
        sol = set()
        for i in range(len(s)-9):
            if s[i:i+10] not in path:
                path.add(s[i:i+10])
            else:
                sol.add(s[i:i+10])
        return list(sol)