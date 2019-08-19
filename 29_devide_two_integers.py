# medium
class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if divisor == 0 or (dividend == -2147483648 and divisor == -1):
            return 2147483647
        sign = -1 if ((dividend<0)^(divisor<0)) else 1
        m = abs(dividend)
        n = abs(divisor)
        if n == 1:
            return m if sign == 1 else -m
        res = 0
        while m>=n:
            t = n
            p = 1
            while (t<<1) <= m:
                p = p<<1
                t = t<<1
            res = res + p
            m = m-t
        return res if sign==1 else -res
