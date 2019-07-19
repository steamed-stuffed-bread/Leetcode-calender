# easy
class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        m = len(nums)
        n = len(nums[0])
        if m*n < r*c:
            return nums
        mu = [nums[i][j] for i in range(m) for j in range(n)]
        res = [[mu[c*j + i] for i in range(c)] for j in range(r)]
        return res
        
