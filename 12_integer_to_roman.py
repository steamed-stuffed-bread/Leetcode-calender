# medium
class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        val = [1000, 500, 100, 50, 10, 5, 1]
        roma = ['M', 'D', 'C', 'L', 'X', 'V', 'I']
        res = ""
        for n in range(0,7,2):
            x = num/val[n]
            if x < 4:
                res = res + roma[n]*x
            elif x == 4:
                res = res + roma[n] + roma[n-1]
            elif x < 9:
                res = res + roma[n-1] + roma[n]*(x-5)
            else:
                res = res + roma[n] + roma[n-2] 
            num = num%val[n]
        return res
