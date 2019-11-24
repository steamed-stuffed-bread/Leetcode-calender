# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        if abs(self.get_length(root.left)-self.get_length(root.right))>1:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)
        
    def get_length(self, root):
        if not root:
            return 0
        left = self.get_length(root.left)
        right = self.get_length(root.right)
        return 1 + max(left, right)
        
        
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if self.check(root) == -1:
            return False
        else:
            return True
    
    def check(self, root):
        if not root:
            return 0
        left = self.check(root.left)
        if left == -1:
            return -1
        right = self.check(root.right)
        if right == -1:
            return -1
        diff = abs(right-left)
        if diff > 1:
            return -1
        else:
            return 1+max(left,right)
