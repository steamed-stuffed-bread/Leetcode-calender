# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head:
            return None
        n = 1
        cur = head
        while cur.next:
            cur = cur.next
            n = n+1
        cur.next = head
        m = n-k%n
        for i in range(m):
            cur = cur.next
        newhead = cur.next
        cur.next = None
        return newhead
