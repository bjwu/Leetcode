class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        # cnt=0
        # if m==len(nums1):
        #     nums1.append(float('inf'))
        # else:
        #     nums1[m]=float('inf')
        # for key in nums2:
        #     for i in range(cnt,m):      #For nums1
        #         if nums1[i]<=key<=nums1[i+1]:
        #             nums1.insert(i+1,key)
        #             cnt=i+1
        #             m=m+1
        #             break
        #         elif key<nums1[i]:
        #             nums1.insert(i,key)
        #             cnt=i+1
        #             m=m+1
        #             break
        #         else:
        #             continue  
        for i in range(len(nums1)-m):
            nums1.pop()
        nums1.extend(nums2)
        nums1.sort()
