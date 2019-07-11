# easy
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.s = 0
        return self.helper(root)
    
    def helper(self,root):
        if root == None:
            return
        self.helper(root.right)
        root.val = root.val + self.s
        self.s = root.val
        self.helper(root.left)
        return root
