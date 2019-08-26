# meidum
class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if num1 == "0" or num2 == "0":
            return "0"
        m = len(num1)
        n = len(num2)
        res = []
        k = m+n-2
        tmp = [0 for i in range(m+n)]
        for i in range(m):
            for j in range(n):
                tmp[k-i-j] = tmp[k-i-j] + (ord(num1[i])-ord("0"))*(ord(num2[j])-ord("0"))
        carry = 0
        for p in range(m+n):
            tmp[p] = tmp[p] + carry
            carry = tmp[p]/10
            tmp[p] = tmp[p]%10
        i = m+n-1
        while tmp[i] == 0:
            i = i-1
        if i < 0:
            return "0"
        while i>=0:
            res.append(chr(tmp[i] + ord("0")))
            i = i-1
        return ''.join(res)
