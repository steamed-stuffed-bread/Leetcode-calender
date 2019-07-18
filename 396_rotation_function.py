# medium
class Solution(object):
    def maxRotateFunction(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        n = len(A)
        res = 0
        s = 0
        for i in range(n):
            s = A[i] + s
            res = res + i * A[i]
        tmp = res
        for i in range(1, n):
            tmp = tmp + s - n*A[n-i]
            res = max(res, tmp)
        return res
