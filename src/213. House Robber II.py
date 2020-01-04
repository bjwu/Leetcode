class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        elif len(nums) <=2:
            return max(nums)
        def helper(nums):
            memo = [(nums[0], True)]
            if nums[1] >= nums[0]:
                memo.append((nums[1], False))
            else:
                memo.append((nums[0], True))
            # True 和 False 为是否这个位置的结果用到了第一位置的元素值
            for i in range(2, len(nums)-1):
                if memo[i-2][0] + nums[i] > memo[i-1][0]:
                    memo.append((memo[i-2][0]+nums[i], memo[i-2][1]))
                else:
                    memo.append(memo[i-1])
            # 最后一个的时候
            if memo[-2][0] + nums[-1] > memo[-1][0]:
                if not memo[-2][-1]:
                    return memo[-2][0] + nums[-1]
                elif memo[-2][0] + nums[-1] - nums[0] > memo[-1][0]:
                    return memo[-2][0] + nums[-1] - nums[0]
            return memo[-1][0]
        return max(helper(nums), helper(nums[::-1]))

#  感觉我的方法好笨，因为从左往右遍历和从右往左遍历居然可以得到不一样的结果，如[2,2,4,3,2,5]
 
#  其实吧，可以简单一点的：
#  ```py
#  class Solution(object):
#     def rob(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         n = len(nums)
#         if n == 0: return 0
#         if n < 4: return max(nums)

#         first, second = 0, 0
#         for i in nums[:-1]: first, second = second, max(first + i, second)
#         result = second

#         first, second = 0, 0
#         for i in nums[1:]: first, second = second, max(first + i, second)
#         return max(result, second)
# ```
# 两次遍历，一起去首一次去尾



				
				
                
                