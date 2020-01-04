import math
class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        (MaxSubArray,low,high)=self.findMaxSubArray(nums,0,len(nums)-1)
        return MaxSubArray
    def findCrossSubArray(self,nums,low,mid,high):
        left_sum,sum,left_low=-float('inf'),0,mid+1
        for i in range(mid,low-1,-1):
            sum=sum+nums[i]
            if sum>left_sum:
                left_sum=sum
                left_low=i
        right_sum,sum,right_high=-float('inf'),0,mid
        for i in range(mid+1,high+1):
            sum=sum+nums[i]
            if sum>right_sum:
                right_sum=sum
                right_high=i
        return left_sum+right_sum,left_low,right_high
    def findMaxSubArray(self,nums,low,high):
        if low==high:
            return nums[low],low,high
        else:
            mid=math.floor((low+high)/2)
            (left_sum,left_low,left_high)=self.findMaxSubArray(nums,low,mid)
            (right_sum,right_low,right_high)=self.findMaxSubArray(nums,mid+1,high)
            (cross_sum,cross_low,cross_high)=self.findCrossSubArray(nums,low,mid,high)
            if max(left_sum,right_sum,cross_sum)==left_sum:
                return left_sum,left_low,left_high
            elif max(left_sum,right_sum,cross_sum)==right_sum:
                return right_sum,right_low,right_high
            else:
                return cross_sum,cross_low,cross_high



