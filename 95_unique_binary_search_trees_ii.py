# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n == 0:
            return None
        return self.helper(1,n)

    def helper(self, start, end):
        if start>end:
            return [None]
        res = []
        for i in range(start, end+1):
            left = self.helper(start, i-1)
            right = self.helper(i+1, end)
            for el in left:
                for er in right:
                    tmp = TreeNode(i)
                    tmp.left = el
                    tmp.right = er
                    res.append(tmp)
        return res
