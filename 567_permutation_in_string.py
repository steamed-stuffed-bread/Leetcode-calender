# meidum
class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        m = len(s1)
        n = len(s2)
        if m > n:
            return False
        res1 = [0 for i in range(128)]
        res2 = [0 for i in range(128)]
        for i in range(m):
            res1[ord(s1[i])] = res1[ord(s1[i])] + 1
            res2[ord(s2[i])] = res2[ord(s2[i])] + 1
        if res1==res2:
            return True
        for j in range(m,n):
            res2[ord(s2[j])] = res2[ord(s2[j])] + 1
            res2[ord(s2[j-m])] = res2[ord(s2[j-m])] - 1
            if res1 == res2:
                return True
        return False
