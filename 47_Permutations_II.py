class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return []
        nums.sort()
        visit = [0 for i in range(len(nums))]
        self.res = []
        self.helper(0, nums, visit, [])
        return self.res
    
    def helper(self, h, nums, visit, out):
        if h >= len(nums):
            self.res.append(out[:])
            return
        for i in range(len(nums)):
            if not visit[i]:
                if i > 0 and visit[i-1] == 0 and nums[i] == nums[i-1]:
                    continue
                visit[i] = 1
                out.append(nums[i])
                self.helper(h+1, nums, visit, out[:])
                out.pop()
                visit[i] = 0
