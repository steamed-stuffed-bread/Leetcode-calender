# hard
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head:
            return None
        cur = head
        for i in range(k):
            if not cur:
                return head
            cur = cur.next
        newhead = self.reverse(head, cur)
        head.next = self.reverseKGroup(cur, k)
        return newhead
    def reverse(self,head,tail):
        pre = tail
        while head!=tail:
            temp = head.next
            head.next = pre
            pre = head
            head = temp
        return pre
