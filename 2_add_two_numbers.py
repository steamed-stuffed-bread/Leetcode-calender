# medium
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        cnt = 0
        res = ListNode(-1)
        node = res
        while l1 or l2:
            n1 = l1.val if l1 else 0
            n2 = l2.val if l2 else 0
            val = (n1 + n2 + cnt) % 10
            cnt = (n1 + n2 + cnt) / 10
            node.next = ListNode(val)
            node = node.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        if cnt:
            node.next = ListNode(cnt)
        return res.next
