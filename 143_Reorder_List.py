# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        if not head or not head.next or not head.next.next:
            return
        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        aft = slow.next
        slow.next = None
        pre = None
        while aft:
            tmp = aft.next
            aft.next = pre
            pre = aft
            aft = tmp
        while head and pre:
            tmp = head.next
            head.next = pre
            pre = pre.next # must be here, because the head.next.next = tmp will lost what is behind the pre pointer
            head.next.next = tmp
            head = tmp
            
