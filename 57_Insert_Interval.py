class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        res = []
        cur = 0
        n = len(intervals)
        while cur < n and intervals[cur][1] < newInterval[0]:
            res.append(intervals[cur])
            cur = cur+1
        while cur < n and newInterval[1] >= intervals[cur][0]: # as long as there is overlapping, keep merging
            newInterval[0] = min(intervals[cur][0], newInterval[0])
            newInterval[1] = max(intervals[cur][1], newInterval[1])
            cur = cur+1
        res.append(newInterval)
        while cur < n:
            res.append(intervals[cur])
            cur = cur+1
        return res
