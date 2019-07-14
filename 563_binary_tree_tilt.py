# easy
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = 0
        self.helper(root)
        return self.res
    
    def helper(self,root):
        if not root:
            return 0
        left = self.helper(root.left)
        right = self.helper(root.right)
        self.res = self.res + abs(left - right)
        return left + right + root.val
