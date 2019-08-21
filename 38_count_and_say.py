# easy
class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        res = '1'
        for i in range(n-1):
            tmp = ''
            pre = res[0]
            count = 0
            for j in range(len(res)):
                if res[j] == pre:
                    count = count + 1
                else:
                    tmp = tmp + str(count) + pre
                    count = 1
                    pre = res[j]
            res = tmp + str(count) + pre
        return res
