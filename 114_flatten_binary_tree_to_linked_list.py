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
        self.res = []
        self.helper(root)
        for i in range(1,len(self.res)):
            self.res[i-1].left = None
            self.res[i-1].right = self.res[i]
        
    def helper(self,root):
        if not root:
            return
        self.res.append(root)
        if root.left:
            self.helper(root.left)
        if root.right:
            self.helper(root.right)
            
            
            
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
        if root.left:
            self.flatten(root.left)
        if root.right:
            self.flatten(root.right)
        tmp = root.right
        root.right = root.left
        root.left = None
        while root.right:
            root = root.right
        root.right = tmp
