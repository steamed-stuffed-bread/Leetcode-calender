# medium
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        n = len(s)
        if numRows <= 1:
            return s
        res = ""
        step = 2*numRows - 2
        for i in range(numRows):
            for j in range(i, n, step):
                res = res+s[j]
                temp = j + step - 2*i
                if i != 0  and i != numRows-1 and temp < n:
                    res = res + s[temp]
        return res
