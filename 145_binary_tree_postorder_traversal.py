# hard
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        res = []
        stack = [root]
        while len(stack) != 0:
            temp = stack[len(stack)-1]
            stack.pop()
            res.append(temp.val)
            if temp.left:
                stack.append(temp.left)
            if temp.right:
                stack.append(temp.right)
        res.reverse()
        return res
        
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        res = []
        stack = [root]
        head = root
        while len(stack)!=0:
            temp = stack[len(stack)-1]
            if (not temp.left and not temp.right) or temp.left == head or temp.right == head:
                res.append(temp.val)
                stack.pop()
                head = temp
            else:
                if temp.right:
                    stack.append(temp.right)
                if temp.left:
                    stack.append(temp.left)
        return res
