# easy
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if val not in nums:
            return len(nums)
        s = 0
        f = 0
        while f < len(nums):
            if nums[f] != val:
                nums[s] = nums[f]
                s = s+1
                f = f+1
            else:
                f = f+1
        return s
