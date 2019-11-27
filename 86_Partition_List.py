# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        if not head:
            return None
        dummy = ListNode(-1)
        newdummy = ListNode(-1)
        dummy.next = head
        cur = dummy
        p = newdummy
        while cur.next:
            if cur.next.val < x:
                p.next = cur.next
                cur.next = cur.next.next
                p = p.next
            else:
                cur = cur.next
        p.next = dummy.next
        return newdummy.next
