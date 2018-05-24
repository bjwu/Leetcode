class Solution:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if k !=0 and k!=len(nums):
            k = k % len(nums)
            count = len(nums)
            start = 0
            while count>1:
                current = (start + k) % len(nums)
                while current != start: 
                    temp = nums[current]
                    nums[current] = nums[start]
                    nums[start] = temp
                    current = (current + k)  % len(nums)
                    count -= 1
                start += 1
                count -= 1

# 其实这道题很多种解法，用python的话最容易的解法应该属于slice直接替换，但是每一次slice都会产生一个额外的copy，从而消耗了空间
# 由于题目要求空间复杂度为 O(1)，所以其实对于每个元素进行逐次索引替换就可以了。