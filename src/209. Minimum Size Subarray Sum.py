class Solution:
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        ## two pointers
        if nums == []:
            return 0
        left, right = 0, 0 
        mini_size = float('inf')
        curr_sum = nums[0]
        nums.append(0)
        while right < len(nums)-1:
            if curr_sum >= s:
                mini_size = min(right-left+1, mini_size)
                curr_sum -= nums[left]
                left += 1
            else:
                right += 1
                curr_sum += nums[right]
        return mini_size if mini_size != float('inf') else 0
        