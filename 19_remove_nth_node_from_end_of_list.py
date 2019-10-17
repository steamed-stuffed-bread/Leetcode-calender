# meidum
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if not head or not head.next: # when linked list only has one node or no node
            return None
        cur = head
        pre = head
        i = 0
        while i < n:
            i = i+1
            cur = cur.next
            if not cur: # take care of case when n is larger than the length of the linked list
                return head.next
        while cur.next:
            pre = pre.next
            cur = cur.next
        pre.next = pre.next.next # cannot use cur.next, because that only works when n = 2
        return head
