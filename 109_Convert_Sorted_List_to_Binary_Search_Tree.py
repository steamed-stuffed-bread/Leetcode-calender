# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        if not head:
            return head
        if not head.next:
            return TreeNode(head.val)
        slow = head
        fast = head
        pre = slow
        while fast.next and fast.next.next:
            pre = slow
            slow = slow.next
            fast = fast.next.next
        newhead = TreeNode(slow.val)
        fast = slow.next
        pre.next = None
        if slow != head:
            newhead.left = self.sortedListToBST(head)
        newhead.right = self.sortedListToBST(fast)
        return newhead
