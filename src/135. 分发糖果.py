"""
老师想给孩子们分发糖果，有 N 个孩子站成了一条直线，老师会根据每个孩子的表现，预先给他们评分。

你需要按照以下要求，帮助老师给这些孩子分发糖果：

每个孩子至少分配到 1 个糖果。
相邻的孩子中，评分高的孩子必须获得更多的糖果。
那么这样下来，老师至少需要准备多少颗糖果呢？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/candy
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

## 这道题有一个隐形条件，如果相邻两个学生分数一样，则不考虑，我也是醉了
class Solution:
    def candy(self, ratings: List[int]) -> int:
        ans1 = [1] * len(ratings)
        ans2 = [1] * len(ratings)
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i - 1]:
                ans1[i] = ans1[i - 1] + 1
        for i in range(len(ratings) - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                ans2[i] = ans2[i + 1] + 1
        ans = [max(ans1[i], ans2[i]) for i in range(len(ratings))]
        return sum(ans)
