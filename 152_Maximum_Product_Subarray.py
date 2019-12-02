class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        res = nums[0]
        ma = nums[0]
        mi = nums[0]
        for e in nums[1:]:
            if e < 0:
                tmp = mi
                mi = ma
                ma = tmp
            ma = max(ma*e, e)
            mi = min(mi*e, e)
            res = max(ma, res)
        return res
