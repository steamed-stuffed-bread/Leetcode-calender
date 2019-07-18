# easy
class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        res = []
        cnt = 0
        i = len(num1)-1
        j = len(num2)-1
        while i >= 0 or j >= 0:
            a = ord(num1[i])-ord('0') if i >= 0 else 0
            b = ord(num2[j])-ord('0') if j >= 0 else 0
            temp = a+b+cnt
            res.insert(0, chr(temp%10+ord('0')))
            cnt = temp/10
            i = i - 1
            j = j - 1
            
        if cnt >= 1:
            res.insert(0, chr(cnt + ord('0')))
            
        return ''.join(res)
