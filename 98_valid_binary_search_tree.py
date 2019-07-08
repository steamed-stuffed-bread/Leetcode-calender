# medium
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return True
        if root.left == None and root.right == None:
            return True
        
        self.res = []
        self.helper(root)
        
        for i in range(1,len(self.res)):
            if self.res[i] <= self.res[i-1]:
                return False
        return True

    def helper(self,root):
        if root == None:
            return
        self.helper(root.left)
        self.res.append(root.val)
        self.helper(root.right)
