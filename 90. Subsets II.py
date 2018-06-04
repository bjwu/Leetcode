class Solution:
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        sol = []
        nums.sort()
        def dfs(dnums, path, sol):
            sol.append(path)
            for i,s in enumerate(dnums):
                if i > 0 and dnums[i] == dnums[i-1]:
                    continue
                dfs(dnums[i+1:], path+[s], sol)
        dfs(nums, [], sol)
        return sol