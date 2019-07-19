# medium
'''
class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m = {0:-1}
        s = 0
        res = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                s = s+1
            else:
                s = s-1
                
            if s in m.keys():
                res = max(res, i-m[s])
            else:
                m[s] = i
                
        return res
'''
class Solution(object):
    def findMaxLength(self, nums):
        if not nums:
            return 0
        maxLength = 0
        disbalances = {}
        disbalance = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                disbalance += 1
            else:
                disbalance -= 1
            if disbalance == 0:
                maxLength = i + 1
            else:
                if disbalance in disbalances:
                    maxLength = max(maxLength, i - disbalances[disbalance])
                else:
                    disbalances[disbalance] = i
        return maxLength
