class Solution:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        rangeJump = [0,0]
        for i in range(len(nums)):
            if i <= rangeJump[1]:
                rangeJump[1] = max(i + nums[i], rangeJump[1])
            else:
                return False
        return True