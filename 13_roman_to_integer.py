# easy
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        res = 0
        G = {'M':1000,
            'D':500,
            'C':100,
            'L':50,
            'X':10,
            'V':5,
            'I':1}
        for i in range(n-1):
            if G[s[i]] < G[s[i+1]]:
                res = res - G[s[i]]
            else:
                res = res + G[s[i]]
        res = res + G[s[n-1]]
        return res
            
