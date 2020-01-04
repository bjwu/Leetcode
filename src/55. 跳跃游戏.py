"""
给定一个非负整数数组，你最初位于数组的第一个位置。

数组中的每个元素代表你在该位置可以跳跃的最大长度。

判断你是否能够到达最后一个位置。


"""
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        i, far = 0, 0
        while i <= far and i<len(nums):
            if i+nums[i] > far:
                far = (i+nums[i])
            i += 1
        return far >= (len(nums)-1)