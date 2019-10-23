class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        n = len(nums)
        for i in range(32):
            one = 0
            zero = 0
            for num in nums:
                if one > n/2 or zero > n/2:
                    break
                if num & (1<<i):
                    one = one + 1
                else:
                    zero = zero + 1
            if zero < one:
                res = res | (1<<i)
        return res if res >> 31 == 0 else res-(1<<32)

    
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return self.helper(nums, 0, len(nums)-1)
    def helper(self,orgnum, left, right):
        if left == right:
            return orgnum[left]
        mid = left + (right-left)/2
        major_l = self.helper(orgnum, left, mid)
        major_r = self.helper(orgnum, mid+1, right)
        if major_l == major_r:
            return major_l
        else:
            return major_l if orgnum[left:right+1].count(major_l) > orgnum[left:right+1].count(major_r) else major_r
