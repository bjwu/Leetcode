class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        def binSearch(nums, target):            
            if len(nums) == 1 and nums[0] == target:
                    return [0,0]
            elif len(nums) > 1:
                mid = (len(nums)-1) // 2
                if nums[mid] == target and nums[mid+1] == target:
                    return [binSearch(nums[:mid+1], target)[0], binSearch(nums[mid+1:], target)[1]+mid+1]
                elif nums[mid] >= target and nums[0] <= target:
                    return binSearch(nums[:mid+1], target)
                elif nums[mid+1] <= target and nums[-1] >= target:
                    if binSearch(nums[mid+1:], target) == [-1,-1]:
                        return [-1,-1]
                    else:
                        return [binSearch(nums[mid+1:], target)[0]+mid+1, binSearch(nums[mid+1:], target)[1]+mid+1]
                else:
                    return [-1,-1]
            else:
                return [-1,-1]
                
        return binSearch(nums, target)

# 怎么说呢，我是采用二分搜索，然后beat了2%的人，下面这个也是二分搜索，然后击败了所有人。不过下面的方法用了一个很巧妙的方法，那就是一次找头，一次找尾，这样大大节省了时间。
# ```py
# class Solution:
#     def searchRange(self, nums, target):
#         start = self.firstGreaterEqaul(nums, target)
#         if start==len(nums) or nums[start]!=target:
#             return [-1, -1]
#         return [start, self.firstGreaterEqaul(nums, target+1)-1]
#     def firstGreaterEqaul(self, nums, target):
#         lo, hi = 0, len(nums)
#         while lo<hi:
#             mid = (hi+lo)//2
#             if nums[mid]<target:
#                 lo = mid + 1
#             else:
#                 hi = mid
#         return lo
# 	```