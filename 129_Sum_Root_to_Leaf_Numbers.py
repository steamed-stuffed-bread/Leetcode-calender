# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.helper(root,0)
    
    def helper(self, root, out):
        if not root:
            return 0
        out = out*10 + root.val
        if not root.left and not root.right:
            return out
        return self.helper(root.left, out) + self.helper(root.right,out)
        
