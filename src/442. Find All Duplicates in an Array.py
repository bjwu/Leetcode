class Solution:
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        output = []
        for i in range(len(nums)):
            while(nums[i]!= (i+1)):
                if nums[nums[i]-1] == nums[i]:
                    output.append(nums[i])
                    break
                tmp = nums[nums[i]-1]
                nums[nums[i]-1] = nums[i]
                nums[i] = tmp     #这里不能直接使用两数交换的操作
        return list(set(output))
        