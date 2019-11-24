# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        self.res = -sys.maxint-1
        self.helper(root)
        return self.res
    
    def helper(self, root):
        if not root:
            return 0
        left = max(self.helper(root.left), 0)
        right = max(self.helper(root.right) , 0)
        # if it is not the root, it will return the max value of left and right
        # the result will be calculated by the root node
        self.res = max(self.res, left+right+root.val) 
        return max(left, right) + root.val
