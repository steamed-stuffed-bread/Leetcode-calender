# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.res = []
        self.helper(root)
        return self.res
    
    def helper(self,root):
        if not root:
            return
        if root.left:
            self.helper(root.left)
        self.res.append(root.val)
        if root.right:
            self.helper(root.right)
