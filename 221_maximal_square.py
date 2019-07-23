# medium
class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if matrix == []:
            return 0
        m = len(matrix)
        n = len(matrix[0])
        res = 0
        dp = [[0 for i in range(n)] for j in range(m)]
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    dp[i][j] = ord(matrix[i][j]) - ord('0')
                elif matrix[i][j] == '1':
                    dp[i][j] = min(dp[i-1][j-1], min(dp[i][j-1], dp[i-1][j])) + 1
                res = max(res, dp[i][j])
        return res*res
