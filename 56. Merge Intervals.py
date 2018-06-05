# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if intervals == []:
            return []
        intervals.sort(key = lambda x: x.start)
        output = []
        temp = intervals[0]
        for i, r in enumerate(intervals):
            if  temp.end >= r.start:
                temp = Interval(temp.start, max(r.end, temp.end))
            else:
                output.append(temp)
                temp = r
        
        output.append(temp)
        return output