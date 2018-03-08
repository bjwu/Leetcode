class Solution:
    def nextGreaterElement(self,nums1,nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        result=[]
        for a in range(len(nums1)):
            result.append(-1)
            for b in range(len(nums2))[::-1]:
                if nums2[b]>nums1[a]:
                    result[a]=nums2[b]
                elif nums2[b]==nums1[a]:
                    break
        return result


