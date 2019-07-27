# medium
class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        if not str:
            return 0
        label = 1
        res = 0
        str = str.strip()
        if not str:
            return 0
        if str[0] == '-':
            label = -1
            str = str[1:]
        elif str[0] == '+':
            label = 1
            str = str[1:]
        for i in str:
            if (ord(i) >= ord('0') and ord(i) <= ord('9')):
                res = res*10 + (ord(i)-ord('0'))
            else:
                break
        if label > 0:
            res = res*label
            if res >= 2147483648:
                res = 2147483647
        elif label < 0:
            res = res*label
            if res < -2147483648:
                res =  -2147483648
        return res
