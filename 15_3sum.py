# medium
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) == 0:
            return []
        nums = sorted(nums)
        res = []
        n = len(nums)
        for i in range(n):
            if nums[i] > 0:
                break
            if i > 0 and nums[i-1] == nums[i]:   # check the first repeated value, see repeat of the previous one
                continue
            newt = 0 - nums[i]
            left = i + 1
            right = n-1
            while left < right:
                if (nums[left] + nums[right]) == newt:
                    res.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]: # check the last repeat value, see repeat of the one behind
                        left = left + 1
                    while left < right and nums[right] == nums[right - 1]: # inverse, check the last repeat value, see repest of the previous one
                        right = right - 1
                    left = left + 1
                    right = right - 1
                elif nums[left] + nums[right] < newt:
                    left = left + 1
                else:
                    right = right - 1
        return res
