class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        res = []
        
        def helper(h, out):
            if len(out) >= k:
                res.append(out[:])
                return
            for i in range(h, n):
                out.append(i+1)
                helper(i+1, out)
                out.pop()

        helper(0, [])
        return res
