# medium
class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        dp = [sys.maxint for i in range(n)]
        dp[0] = 0
        for i in range(m):
            for j in range(n):
                if j==0:
                    dp[j] = dp[j] + grid[i][j]
                else:
                    dp[j] = min(dp[j-1],dp[j]) + grid[i][j]
        return dp[n-1]
