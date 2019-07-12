# medium
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def widthOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.start = []
        self.res = 0
        self.helper(root, 0, 1)
        return self.res
    
    def helper(self, node, h, idex):
        if not node:
            return
        if h >= len(self.start):
            self.start.append(idex)
        self.res = max(self.res, idex - self.start[h] + 1)
        self.helper(node.left, h+1, idex*2)
        self.helper(node.right, h+1, idex*2 + 1)
