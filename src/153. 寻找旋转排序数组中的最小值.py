"""
假设按照升序排序的数组在预先未知的某个点上进行了旋转。

( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。

请找出其中最小的元素。

你可以假设数组中不存在重复元素。

"""
# 二分搜索，其判断左边界还是右边界需要分析，找到规律
# class Solution:
#     def findMin(self, nums: List[int]) -> int:
#         left, right = 0, len(nums)-1
#         while (left < right):
#             mid = left + (right-left) // 2
#             if nums[mid] <= nums[right] and nums[mid] <= nums[left]:
#                 right = mid 
#             elif nums[mid] >= nums[right] and nums[mid] >= nums[left]:
#                 left = mid + 1
#             elif nums[mid] <= nums[right] and nums[mid] >= nums[left]:
#                 right = mid
#         return nums[left]

##下面是对上面的改进，综合了if条件

class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums)-1
        while (left < right):
            mid = left + (right-left) // 2
            if nums[mid] <= nums[right]:
                right = mid 
            elif nums[mid] >= nums[right] and nums[mid] >= nums[left]:
                left = mid + 1
        return nums[left]