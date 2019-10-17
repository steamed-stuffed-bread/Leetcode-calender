# hard
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if len(lists) == 0:
            return None
        n = len(lists)
        while n > 1:
            for i in range(n/2):
                lists[i] = self.helper(lists[i], lists[i+(n+1)/2])
            n = (n+1)/2 # make sure the previous step won't out of the list range, when n is even, +1 doesn't have impact, when it is odd, +1 will start with mid+1
        return lists[0]
    def helper(self, l1, l2):
        if not l1:
            return l2
        if not l2:
            return l1
        if l1.val < l2.val:
            head = l1
            head.next = self.helper(l1.next,l2)
        else:
            head = l2
            head.next = self.helper(l1,l2.next)
        return head
