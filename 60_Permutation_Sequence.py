class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        res = ""
        nums = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        f = [1 for i in range(n)]
        for i in range(1, n):
            f[i] = i*f[i-1]
        k = k-1
        for i in range(n, 0, -1):
            j = k//f[i-1]
            k = k%f[i-1]
            res = res + nums[j]
            nums.pop(j)
        return res
