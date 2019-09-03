class Solution(object):
    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if len(s1) != len(s2):
            return False
        if s1 == s2:
            return True
        l = len(s1)
        dp = [[[False for i in range(l+1)] for j in range(l)] for k in range(l)]
        for i in range(l):
            for j in range(l):
                dp[i][j][1] = (s1[i] == s2[j]) # length 1
        for lo in range(2, l+1):
            for i in range(l-lo+1):
                for j in range(l-lo+1):
                    for k in range(1, lo):
                        if (dp[i][j][k] and dp[i+k][j+k][lo-k]) or (dp[i][j+lo-k][k] and dp[i+k][j][lo-k]):
                            dp[i][j][lo] = True;
        return dp[0][0][l]
