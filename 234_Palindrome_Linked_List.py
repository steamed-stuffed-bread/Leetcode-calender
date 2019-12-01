# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next:
            return True
        slow = head
        fast = head
        stack = [head.val]
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            stack.append(slow.val)
        if not fast:
            stack.pop()
        while slow:
            if slow.val != stack[len(stack)-1]:
                return False
            stack.pop()
            slow = slow.next
        return True
