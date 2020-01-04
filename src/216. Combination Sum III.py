class Solution:
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        sol = []
        def helper(restn, lastnum, index, path, sol):
            if restn == 0 and index == k:
                sol.append(path)
            elif index == k or restn == 0:
                return 
            elif restn > 0:
                for i in range(lastnum, min(10, restn+1)):
                    if i not in path:
                        helper(restn-i, i, index+1, path+[i], sol)
        helper(n, 1, 0, [], sol)
        return sol