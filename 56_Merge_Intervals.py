class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        if not intervals:
            return []
        intervals.sort()
        res = [intervals[0]]
        for i in range(1, len(intervals)):
            if res[len(res)-1][1] < intervals[i][0]:
                res.append(intervals[i])
            else:
                tmp_m = max(res[len(res)-1][1], intervals[i][1])
                res[len(res)-1][1] = tmp_m
        return res
