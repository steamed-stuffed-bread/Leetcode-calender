# medium
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        self.res = []
        self.helper(root)
        root = self.res.pop()
        node = root
        while len(self.res) != 0:
            node.left = None
            node.right = self.res.pop()
            node = node.right
        
    def helper(self,root):
        if not root:
            return
        self.res.insert(0, root)
        self.helper(root.left)
        self.helper(root.right)
