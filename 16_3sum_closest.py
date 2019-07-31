# medium
class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) == 0:
            return []
        n = len(nums)
        nums = sorted(nums)
        res = nums[0] + nums[1] + nums[2]
        diff = abs(res - target)
        for i in range(n):
            left = i+1
            right = n-1
            while left < right:
                temp = nums[i] + nums[left] + nums[right]
                ndiff = abs(temp - target)
                if ndiff < diff:
                    res = temp
                    diff = ndiff
                elif temp > target:
                    right = right - 1
                else:
                    left = left + 1
        return res
