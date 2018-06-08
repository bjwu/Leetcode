class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        sol = []
        def dfs(nums, path, sol):
            if len(nums) == 0:
                sol.append(path)
            else:
                dfs(nums[1:], path+[nums[0]], sol)
                dfs(nums[1:], path, sol)
        dfs(nums, [], sol)
        return sol