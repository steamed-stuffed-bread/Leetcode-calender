# easy
class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        rep = 0
        for e in nums:
            if nums[abs(e) - 1] > 0:
                nums[abs(e) - 1] = -nums[abs(e) - 1]
            else:
                rep = abs(e)
                
        lost = 0
        for i in range(len(nums)):
            if nums[i] > 0:
                lost = i + 1
        res = [rep, lost]
        return res
