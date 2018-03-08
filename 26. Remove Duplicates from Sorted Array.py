class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cnt=0
        if len(nums)==0:
            return 0
        for i in range(1,len(nums)):
            if nums[cnt]!=nums[i]:
                cnt=cnt+1
                nums[cnt]=nums[i]
        return cnt+1