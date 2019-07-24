# easy
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        G = dict()
        for i in range(len(nums)):
            if target - nums[i] in G.keys():
                return [G[target-nums[i]],i]
            if nums[i] not in G.keys():
                G[nums[i]] = i
        return []
