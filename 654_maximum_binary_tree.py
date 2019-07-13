# medium
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if len(nums) == 0:
            return None
        val = max(nums)
        i = nums.index(val)
        l = nums[:i]
        r = nums[i+1:]
        root = TreeNode(val)
        root.left = self.constructMaximumBinaryTree(l)
        root.right = self.constructMaximumBinaryTree(r)
        return root
