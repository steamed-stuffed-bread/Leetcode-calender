# easy
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x <= 1:
            return x
        left = 0
        right = x
        while left < right:
            mid = left + (right-left)/2
            if x/mid >= mid:
                left = mid + 1
            else:
                right = mid
        return right-1
