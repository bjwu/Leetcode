class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        sortedstrs = [''.join(sorted(s)) for s in strs]
        dict = {}
        for i, s in enumerate(sortedstrs):
            if s not in dict:
                dict[s] = [strs[i]]
            else:
                dict[s].append(strs[i])                
        return list(dict.values())