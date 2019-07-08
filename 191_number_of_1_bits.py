# easy
class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = 0
        for i in range(32):
            res = res + (1 & n)
            n = n >> 1
        return res
