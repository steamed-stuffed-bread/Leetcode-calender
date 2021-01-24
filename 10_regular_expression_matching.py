# hard
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        m = len(s)
        n = len(p)
        dp = [[False for i in range(n+1)] for j in range(m+1)]
        dp[0][0] = True
        for i in range(m+1):
            for j in range(1, n+1):
                if j > 1 and p[j-1] == '*':
                    dp[i][j] = dp[i][j-2] or (i>0 and (s[i-1] == p[j-2] or p[j-2] == '.') and dp[i-1][j]) // i-1 j is not about matching s i and p j-1, * only means that the previous repeating
                else:
                    dp[i][j] = i>0 and dp[i-1][j-1] and (s[i - 1] == p[j - 1] or p[j - 1] == '.')
        return dp[m][n]
