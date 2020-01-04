"""
在一条环路上有 N 个加油站，其中第 i 个加油站有汽油 gas[i] 升。

你有一辆油箱容量无限的的汽车，从第 i 个加油站开往第 i+1 个加油站需要消耗汽油 cost[i] 升。你从其中的一个加油站出发，开始时油箱为空。

如果你可以绕环路行驶一周，则返回出发时加油站的编号，否则返回 -1。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/gas-station
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
# 贪心策略

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # 从头开始遍历，加上gas[i]，减掉cost[i]，并更新两个tank的值，如果curr_tank<0，将curr_tank置0，并以
        # i+1为头重新开始遍历。最后如果total_tank<0，则返回-1，否则返回i
        total_tank = 0
        curr_tank = 0
        start = 0
        for i in range(len(gas)):
            curr_tank = curr_tank + gas[i] -cost[i]
            total_tank = total_tank + gas[i] -cost[i]
            if curr_tank < 0:
                start = i+1
                curr_tank = 0
        if total_tank < 0:
            return -1
        else:
            return start