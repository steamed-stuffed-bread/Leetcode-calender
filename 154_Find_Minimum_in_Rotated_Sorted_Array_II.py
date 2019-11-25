class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        right = len(nums)-1
        while left < right:
            mid = left + (right-left)/2
            if nums[right] < nums[mid]:
                left = mid+1
            elif nums[right] > nums[mid]:
                right = mid
            else:
                right = right - 1
        return nums[right]
