# easy
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        temp = x
        p = 0
        while temp:
            p = p*10 + temp%10
            temp = temp/10
        return p == x
