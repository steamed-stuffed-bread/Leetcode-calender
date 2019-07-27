# easy
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        label = 1 if x >= 0 else -1
        temp = abs(x)
        res = 0
        while temp:
            res = res*10 + temp%10
            temp = temp/10
            
        return res*label if res < 2147483648 and res >= -2147483648 else 0
