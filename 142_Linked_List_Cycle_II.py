#     a
# ---------*----
#          |c    \ b
#          |     /
#           ----*

# length of loop r
# length of list l
# s = (a+b)
# vfast = 2vslow
# 2s = s + nr
# a+b = nr
# a+b = (n-1)r + l-a
# a = (n-1)r + l-a-b
# a = c + (n-1)r
# next time fast start from meeting point, slow start from start point
# before they meet at the start point of loop, fast may have round the loop several times.
# but they are meant to meet at the start point of the loop.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        if not fast or not fast.next:
            return None
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        return fast
