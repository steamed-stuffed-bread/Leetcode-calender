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

    
    class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        m = len(num1)
        n = len(num2)
        val = [0 for i in range(m+n)]
        res = ""
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                mul = ord(num1[i])-ord('0')
                b_mul = ord(num2[j])-ord('0')
                tmp = mul*b_mul
                s = tmp+val[i+j+1]
                val[i+j] = val[i+j] + s/10
                val[i+j+1] = s%10
        for e in val:
            if not (len(res)==0 and e==0):
                res = res + chr(e+ord('0'))
        return res if len(res)!=0 else "0"
