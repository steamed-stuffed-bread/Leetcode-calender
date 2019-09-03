class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix:
            return 0
        m = len(matrix)
        n = len(matrix[0])
        res = 0
        cur = 0
        height = [0 for i in range(n+1)]
        for i in range(m):
            s = []
            for j in range(n+1):
                if j < n:
                    if matrix[i][j] == '1':
                        height[j] = height[j]+1
                    else:
                        height[j] = 0
                while len(s)!=0 and height[j] <= height[s[len(s)-1]]:
                    cur = height[s[len(s)-1]]
                    s.pop()
                    if len(s) == 0:
                        temp = cur * j
                    else:
                        temp = cur * (j-s[len(s)-1]-1)
                    res = max(res,temp)
                s.append(j)
        return res
