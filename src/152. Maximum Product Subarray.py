# 这道题有负数的存在使得题目变得复杂
# 标签：动态规划
# 遍历数组时计算当前最大值，不断更新
# 令imax为当前最大值，则当前最大值为 imax = max(imax * nums[i], nums[i])
# 由于存在负数，那么会导致最大的变最小的，最小的变最大的。因此还需要维护当前最小值imin，imin = min(imin * nums[i], nums[i])
# 当负数出现时则imax与imin进行交换再进行下一步计算
# 时间复杂度：O(n)O(n)

# 作者：guanpengchn
# 链接：https://leetcode-cn.com/problems/maximum-product-subarray/solution/hua-jie-suan-fa-152-cheng-ji-zui-da-zi-xu-lie-by-g/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        imax = [nums[0]]
        imin = [nums[0]]
        for i, num in enumerate(nums):
            if num >=0:
                imax.append(max(imax[-1]*num, num))
                imin.append(min(imin[-1]*num, num))
            else:
                imax.append(max(imin[-1] * num, num))
                imin.append(min(imax[-1] * num, num))
        return max(imax)