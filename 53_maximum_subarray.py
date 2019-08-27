# easy
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = -sys.maxint-1
        tmp = 0
        for e in nums:
            tmp = max(e, tmp+e)
            res = max(res,tmp)
        return res

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        res = self.helper(nums, 0, len(nums)-1)
        return res
    
    def helper(self, nums, left, right):
        if left >= right:
            return nums[left]
        mid = left + (right-left)/2
        lmax = self.helper(nums, left, mid-1)
        rmax = self.helper(nums, mid+1, right)
        mmax = nums[mid]
        tmp = mmax
        for i in range(mid-1, left-1, -1):
            tmp = nums[i]+tmp
            mmax = max(mmax, tmp)
        tmp = mmax
        for i in range(mid+1, right+1):
            tmp = nums[i]+tmp
            mmax = max(mmax, tmp)
        return max(mmax, max(lmax, rmax))
