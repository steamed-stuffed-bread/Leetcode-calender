# medium
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height)-1
        res = 0
        while left < right:
            h = min(height[left], height[right])
            res = max(res, h*(right-left))
            while left < right and h == height[left]:
                left = left + 1
            while left < right and h == height[right]:
                right = right - 1
        return res
