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
