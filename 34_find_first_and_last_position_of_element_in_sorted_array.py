# medium
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums) == 0:
            return [-1,-1]
        if len(nums) == 1 and nums[0] == target:
            return [0,0]
        res = [-1,-1]
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = left + (right-left)/2
            if nums[mid] > target:
                right = mid-1
            elif nums[mid] < target:
                left = mid+1
            else:
                start = mid
                while start >= 0 and nums[start] == target:
                    start = start - 1
                while mid <= len(nums)-1 and nums[mid] == target:
                    mid = mid + 1
                start = start + 1
                mid = mid - 1
                res = [start, mid]
                return res
        return res
