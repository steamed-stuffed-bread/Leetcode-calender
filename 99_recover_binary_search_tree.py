# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        self.pre = None
        self.m1 = None
        self.m2 = None
        self.helper(root)
        self.m1.val,self.m2.val = self.m2.val, self.m1.val
        
    def helper(self, root):
        if root:
            self.helper(root.left)
            if self.pre and (self.pre.val > root.val): # normally, pre's value is compared before it is given a larger value
                if not self.m1:
                    self.m1 = self.pre
                self.m2 = root
            self.pre = root
            self.helper(root.right)
