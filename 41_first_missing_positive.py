# hard
class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        for i in range(n):
            # as long as all the val be allocated according to the law that nums[i] == i+1
            # and there is 1 in nums, the 1 should be at location 0 eventually
            while nums[i] <= n and nums[i] > 0 and nums[nums[i]-1] != nums[i]:
                temp = nums[i]
                nums[i] = nums[nums[i]-1]
                nums[temp-1] = temp
        for i in range(n):
            if nums[i] != i+1:
                return i+1
        return n+1
