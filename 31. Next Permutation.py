class Solution:
    def nextPermutation(nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)-1,0,-1):
            if nums[i-1] < nums[i]:
                left = i-1
                break
            if i == 0:
                nums.sort()
                return
        for j in range(left+1, len(nums)):
            if nums[j] <= nums[left]:
                right = j-1
                break
            if j == len(nums)-1:
                right = j
        nums[left], nums[right] = nums[right], nums[left]
        nums[left+1:] = sorted(nums[left+1:])

