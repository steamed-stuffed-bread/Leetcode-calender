# easy
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA or not headB:
            return None
        lenA = self.getlenth(headA)
        lenB = self.getlenth(headB)
        if lenA > lenB:
            for i in range(lenA-lenB):
                headA = headA.next
        else:
            for i in range(lenB-lenA):
                headB = headB.next
        while headA and headB and headA!=headB:
            headA = headA.next
            headB = headB.next
        return headA if (headA and headB) else None
        
    def getlenth(self, head):
        if not head:
            return 0
        cur = head
        n = 0
        while cur:
            cur = cur.next
            n = n+1
        return n
