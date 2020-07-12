# medium
# set or check the duplication of m and n
class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        n = len(nums)
        res = []
        for i in range(n-3):
            if i>0 and nums[i] == nums[i-1]: # skip the first element of the duplicated number
                continue
            for j in range(i+1, n-2):
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                left = j+1
                right = n-1
                while left < right:
                    if nums[left] + nums[right] + nums[i] + nums[j] == target:
                        res.append([nums[i],nums[j],nums[left],nums[right]])
                        while left < right and nums[left] == nums[left + 1]:
                            left = left + 1
                        while left < right and nums[right] == nums[right - 1]:
                            right = right - 1 
                        left = left + 1
                        right = right - 1
                    elif nums[left] + nums[right] + nums[i] + nums[j] > target:
                        right = right - 1
                    else:
                        left = left + 1
        return res
