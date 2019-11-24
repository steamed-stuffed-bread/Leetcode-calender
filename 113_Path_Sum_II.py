# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        self.res = []
        self.helper(root, sum, [])
        return self.res
    
    def helper(self, root, sum, out):
        if not root:
            return
        out.append(root.val)
        if not root.left and not root.right and sum == root.val:
            self.res.append(out[:])
        self.helper(root.left, sum-root.val, out)
        self.helper(root.right, sum-root.val, out)
        out.pop()
