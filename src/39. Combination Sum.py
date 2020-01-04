class Solution:
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        sol = []
        def dfs(cands, rest, path, sol):
            if rest == 0:
                sol.append(path)
                return 
            elif rest < 0:
                return 
            else:
                for i, s in enumerate(cands):
                    dfs(cands[i:], rest-s, path+[s], sol)
        dfs(candidates, target, [], sol)
        return sol