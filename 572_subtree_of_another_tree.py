# easy
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        if not s:
            return False
        if self.issame(s,t):
            return True
        else:
            return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)
        
    def issame(self, s, t):
        if not s and not t:
            return True
        elif (not s and t) or (s and not t):
            return False
        if s.val == t.val:
            return self.issame(s.left, t.left) and self.issame(s.right, t.right)
        else:
            return False
