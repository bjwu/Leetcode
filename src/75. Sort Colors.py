class Solution:
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i, left, right =0, 0, len(nums)-1
        
        while i <= right:
            if nums[i] == 2 and i <= right:
                nums[i], nums[right] = nums[right], nums[i]
                right -= 1
                continue
            elif nums[i] == 0 and i >= left:
                nums[i], nums[left] = nums[left], nums[i]
                left += 1
                continue
            i += 1