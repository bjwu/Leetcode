class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l=len(nums)
        if not l:
            return 0
        for i in range(l):
            if nums[i]>=target:
                return i
        return l