"""
给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？找出所有满足条件且不重复的三元组。
"""


# 这个解最后没有去重复，算法是利用固定first num且利用sum of 2 numbers的算法进行
class Solution1:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        for i, firstNum in enumerate(nums):
            remainNums = nums[i+1:]
            remain = 0 - firstNum
            memo = set()
            for secNum in remainNums:
                if secNum in memo:
                    ans.append([firstNum, secNum, remain-secNum])
                else:
                    memo.add(remain-secNum)
        return ans
    
# 最好的办法还是利用双指针，在双指针之前先进行排序
class Solution2:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums = sorted(nums)
        for i, firstNum in enumerate(nums):
            # 防止重复
            if i > 0 and nums[i] == nums[i-1]:
                continue
            remainNums = nums[i+1:]
            remain = 0 - firstNum
            # 采用双指针策略
            p1, p2 = i+1, len(nums)-1
            while p1 < p2:
                if nums[p1]+nums[p2] == remain:
                    ans.append([firstNum, nums[p1], nums[p2]])
                    p1 += 1
                    # 防止重复
                    while p1 < p2 and nums[p1] == nums[p1-1]:
                        p1 += 1
                elif nums[p1]+nums[p2] < remain:
                    p1 += 1
                else:
                    p2 -= 1
        return ans