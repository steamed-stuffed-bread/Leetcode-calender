# easy
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        s = 0
        f = 0
        for i in range(len(nums)):
            if nums[s] != nums[f]:
                s = s+1
                nums[s] = nums[f]
            f = f+1
        return s+1
