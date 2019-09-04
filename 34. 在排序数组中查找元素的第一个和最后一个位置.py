"""
给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。

你的算法时间复杂度必须是 O(log n) 级别。

如果数组中不存在目标值，返回 [-1, -1]。
"""

# 找到比他大的和比他小0.5的两个数的位置
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        target_1, target_2 = target - 0.5, target + 0.5
        # 前半部分
        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] < target_1:
                left = mid + 1
            else:
                right = mid
        pos_l = left
        # 后半部分
        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + (right - left + 1) // 2
            if nums[mid] < target_2:
                left = mid
            else:
                right = mid - 1
        pos_r = right
        if pos_l > pos_r or (pos_l == pos_r and nums[pos_l] != target):
            return [-1, -1]

        return [pos_l, pos_r]
