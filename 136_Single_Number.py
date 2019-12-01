class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        G = dict()
        for e in nums:
            if e not in G:
                G[e] = 1
            else:
                G[e] = G[e]-1
        for e in G:
            if G[e]:
                return e
