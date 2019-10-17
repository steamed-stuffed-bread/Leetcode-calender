# medium
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return None
        dummy = ListNode(-1)
        pre = dummy
        dummy.next = head
        while pre.next:
            cur = pre.next
            while cur.next and cur.next.val == cur.val:
                cur = cur.next
            if cur != pre.next:
                pre.next = cur.next
            else:
                pre = pre.next
        return dummy.next
