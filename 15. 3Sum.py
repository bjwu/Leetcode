class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) <3:
            return []
        from collections import Counter
        dict = Counter(nums)
        nums = list(set(nums))
        output = set()
        if dict[0] >2:
            output.add((0,0,0))
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if -(nums[i]+nums[j]) in dict:
                    if 2*nums[i] == -nums[j] and dict[nums[i]]>1:
                        output.add(tuple(sorted([nums[i], nums[i], nums[j]])))
                    elif 2*nums[j] == -nums[i] and dict[nums[j]]>1:
                        output.add(tuple(sorted([nums[j], nums[j], nums[i]])))
                    elif 2*nums[i] != -nums[j] and 2*nums[j] != -nums[i]:
                        output.add(tuple(sorted([nums[i], nums[j], -(nums[i]+nums[j])])))
        return list(output)

# ```
# class Solution(object):
#     def threeSum(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[List[int]]
#         """
#         if len(nums) < 3:
#             return []
#         nums.sort()
#         res = set()
#         for i, v in enumerate(nums[:-2]):
#             if i >= 1 and v == nums[i-1]:
#                 continue
#             d = {}
#             for x in nums[i+1:]:
#                 if x not in d:
#                     d[-v-x] = 1
#                 else:
#                     res.add((v, -v-x, x))
#         return map(list, res)
# 	```
# 在遍历每一个元素的时候，在字典里写出之后如果输出应该要出现的元素。这个方法实在是妙，比我好多了



	