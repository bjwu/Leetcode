class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        demo = {}
        demo[0] = nums[0]
        demo[1] = max(nums[0:2])
        for i, num in enumerate(nums[2:]):
            if demo[i]+num > demo[i+1]:
                value = demo[i]+num
            else:
                value = demo[i+1]
            demo[i+2] = value
        return demo[len(nums)-1]