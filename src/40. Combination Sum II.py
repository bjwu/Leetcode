class Solution:
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        sol = []
        def dfs(cands, rest, path, sol):
            if rest == 0:
                sol.append(path)
                return 
            elif rest < 0:
                return 
            else:
                for i,s in enumerate(cands):
                    if i>0 and cands[i] == cands[i-1]:
                        continue
                    dfs(cands[i+1:], rest-s, path+[s], sol)
        dfs(candidates, target, [], sol)
        return sol
                    