# medium
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        res = []
        q = [root]
        while len(q) != 0:
            res.append(q[0].val)
            for i in range(len(q)):
                temp = q.pop()
                if temp.left:
                    q.insert(0, temp.left)
                if temp.right:
                    q.insert(0, temp.right)
                
        return res
