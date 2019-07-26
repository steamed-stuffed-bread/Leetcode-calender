# medium
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[0 for i in range(n)] for j in range(n)]
        l = 1
        left = 0
        for j in range(n):
            dp[j][j] = 1
            for i in range(j):
                dp[i][j] = (s[j]==s[i]) and (dp[i+1][j-1] or (j-i<2))
                if dp[i][j] and (l < j-i+1):
                    l = j-i+1
                    left = i
        return s[left:(left+l)]
