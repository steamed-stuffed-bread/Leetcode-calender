# easy
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        left = 0
        right = len(nums)-1
        res = 0
        while left <= right:
            mid = left + (right-left)/2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                res = mid
                return res
            if left > right and nums[right] < target:
                res = left
        return res
