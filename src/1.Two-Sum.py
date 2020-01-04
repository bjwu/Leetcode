"""
使用哈希查找，且存入target-num的差值即可达到最优
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        memo = {}
        for i, num in enumerate(nums):
            res = target - num
            if res in memo:
                return [memo[res], i]
            else:
                memo[num] = i

        
