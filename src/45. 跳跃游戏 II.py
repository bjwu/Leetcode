"""
给定一个非负整数数组，你最初位于数组的第一个位置。

数组中的每个元素代表你在该位置可以跳跃的最大长度。

你的目标是使用最少的跳跃次数到达数组的最后一个位置。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/jump-game-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

# 贪心算法
# 在对问题求解时，总是做出在当前看来是最好的选择。贪心算法没有固定的算法框架，算法设计的关键是贪心策略的选择。
# 必须注意的是，贪心算法不是对所有问题都能得到整体最优解，选择的贪心策略必须具备无后效性，即某个状态以后的过程不会影响以前的状态，只与当前状态有关。

# 贪心策略：
# 每次找在end之前的范围内跳得最远的那一个作为新的start

class Solution:
    def jump(self, nums: List[int]) -> int:
        start, end = 0, 0
        cnt = 0
        while end < (len(nums) - 1):
            for i in range(start, end + 1):
                if nums[i] + i >= end:
                    end = nums[i] + i
                    start = i
            cnt += 1
        return cnt


