# easy
class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m = dict()
        n = dict()
        degree = 0
        for i in range(len(nums)):
            if not (nums[i] in m.keys()):
                m[nums[i]] = [i, i]
                n[nums[i]] = 1
            else:
                m[nums[i]][1] = i
                n[nums[i]] = n[nums[i]] + 1
            degree = max(degree, n[nums[i]])
        res = sys.maxint
        for k in n.keys():
            if degree == n[k]:
                res = min(res,(m[k][1]-m[k][0]+1))
        return res
