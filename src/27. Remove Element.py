class Solution:
    def removeElement(self, nums, val):
        cnt=-1
        for i in range(len(nums)):
            if nums[i]!=val:
                cnt=cnt+1
                nums[cnt]=nums[i]
        return cnt+1