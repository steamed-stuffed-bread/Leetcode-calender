# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        return self.helper(inorder, 0, len(inorder)-1, postorder, 0, len(postorder)-1)
    
    def helper(self, inorder, ileft, iright, postorder, pleft, pright):
        if (ileft > iright) or (pleft > pright):
            return None
        mid = 0
        for i in range(ileft, iright+1):
            if postorder[pright] == inorder[i]:
                mid = i
                break
        root = TreeNode(postorder[pright])
        root.left = self.helper(inorder, ileft, mid-1, postorder, pleft, pleft+mid-ileft-1)
        root.right = self.helper(inorder, mid+1, iright, postorder, pleft+mid-ileft, pright-1)
        return root
