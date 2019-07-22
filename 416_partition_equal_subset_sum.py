# medium
class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        s = sum(nums)
        target = s >> 1
        if (s & 1):
            return False
        dp = [False for i in range(target+1)]
        dp[0] = True
        for num in nums:
            for i in range(target, num-1, -1):
                dp[i] = (dp[i] | dp[i-num])
        return dp[target]
