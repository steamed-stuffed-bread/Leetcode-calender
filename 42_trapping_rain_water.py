# hard
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        res = 0
        dp = [0 for i in range(n)]
        mx = 0
        # get the max possible height from left to right for every height
        for i in range(n):
            dp[i] = mx
            mx = max(mx, height[i])
        mx = 0
        # get the max possible height from right to left for every height
        for i in range(n-1, -1, -1):
            dp[i] = min(mx, dp[i])
            mx = max(mx, height[i])
            # the height is smaller than the possible max rain height, so the rain can be cumulated
            if dp[i] > height[i]:
                res = res + (dp[i] - height[i])
        return res
