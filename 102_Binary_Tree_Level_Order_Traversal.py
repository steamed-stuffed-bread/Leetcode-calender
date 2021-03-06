# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return
        q1 = [root]
        q2 = []
        res = []
        out = []
        while q1:
            out.append(q1[len(q1)-1].val)
            if q1[len(q1)-1].left:
                q2.insert(0, q1[len(q1)-1].left)
            if q1[len(q1)-1].right:
                q2.insert(0, q1[len(q1)-1].right)
            q1.pop()
            if not q1:
                res.append(out)
                out = []
                tmp = q2
                q2 = q1
                q1 = tmp
        return res
