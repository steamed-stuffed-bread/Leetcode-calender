# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        return self.helper(preorder, 0, len(preorder)-1, inorder, 0, len(inorder)-1)
    
    def helper(self, preorder, pleft, pright, inorder, ileft, iright):
        if (pleft > pright) or (ileft > iright):
            return None
        mid = 0
        for i in range(ileft, iright + 1):
            if preorder[pleft] == inorder[i]:
                mid = i
                break
        root = TreeNode(preorder[pleft])
        root.left = self.helper(preorder, pleft+1, pleft+mid-ileft, inorder, ileft, mid-1)
        root.right = self.helper(preorder, pleft+mid-ileft+1, pright, inorder, mid+1, iright)
        return root
