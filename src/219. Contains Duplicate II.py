class Solution:
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        # 在这个字典中，key是nums中元素，value为时间戳
        dict = {}
        for i,num in enumerate(nums):
            if num not in dict:
                dict[num] = i
            else:
                if i-dict[num] <= k:
                    return True
                else:
                    dict[num] = i
        return False


########### 明明代码可以更简洁

		# 	 for i, v in enumerate(nums):
        #      if v in dic and i - dic[v] <= k:
        #          return True
        #      dic[v] = i
        #  return False