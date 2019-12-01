class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return []
        self.res = []
        self.helper(nums, 0, [])
        return self.res
    
    def helper(self, nums, h, out):
        self.res.append(out[:])
        for i in range(h, len(nums)):
            out.append(nums[i])
            self.helper(nums, i+1, out[:])
            out.pop()
