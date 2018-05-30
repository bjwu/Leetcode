class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        maxwater = 0
        left, right = 0, len(height)-1
        while left < right:
            temp = (right-left) * min(height[left], height[right])
            if temp > maxwater:
                maxwater = temp
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return maxwater
                