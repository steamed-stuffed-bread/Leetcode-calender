# medium
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def printTree(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[str]]
        """
        self.h = self.getheight(root)
        w = 2**self.h-1
        self.res = [["" for i in range(w)] for j in range(self.h)]
        self.helper(root, 0, w-1, 0)
        return self.res
        
    def helper(self, root, left, right, height):
        if not root or height == self.h:
            return
        mid = left + (right - left)/2
        self.res[height][mid] = str(root.val)
        self.helper(root.left, left, mid, height + 1)
        self.helper(root.right, mid+1, right, height + 1)
        
    def getheight(self,root):
        if not root:
            return 0
        return 1 + max(self.getheight(root.left), self.getheight(root.right))
