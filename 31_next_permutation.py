# medium
class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        left = 0
        for i in range(len(nums)-2, -1, -1):
            if nums[i+1] > nums[i]:
                left = i+1
                for j in range(len(nums)-1, i, -1):
                    if nums[j] > nums[i]:
                        temp = nums[j]
                        nums[j] = nums[i]
                        nums[i] = temp
                        n = len(nums)
                        while left < n:
                            nums.insert(left, nums[n-1])
                            nums.pop()
                            left = left + 1
                        return nums
        nums.reverse()
        return nums
