# easy
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # self.m = dict()
        self.max = 0
        self.helper(root)
        return self.max
        
    def helper(self,root):
        if not root:
            return 0
        # if root in self.m:
        #     return self.m[root]
        left = self.helper(root.left)
        right = self.helper(root.right)
        self.max = max(self.max, left+right)
        # self.m[root] = max(left, right) + 1
        # return self.m[root]
        return max(left,right) + 1
