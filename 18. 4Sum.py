class Solution:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        output = set()
        for i, v in enumerate(nums[:-3]):
            if i >= 1 and v == nums[i-1]:
                continue
            for j, w in enumerate(nums[i+1:-2]):
                dict = {}
                for m in nums[i+j+2:]:
                    if m in dict:
                        output.add(tuple(sorted([v,w,m,target-(v+w+m)])))
                    else:
                        dict[target-(v+w+m)]=1
        return list(output)