# medium
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):

    def __init__(self, head):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        :type head: ListNode
        """
        self.head = head
        node = head
        self.l = 0
        while node:
            self.l = self.l + 1
            node = node.next

    def getRandom(self):
        """
        Returns a random node's value.
        :rtype: int
        """
        t = random.randint(0, self.l-1) % self.l
        node = self.head
        while t:
            node = node.next
            t = t-1
        return node.val


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

'''
class Solution(object):

    def __init__(self, head):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        :type head: ListNode
        """
        self.head = head

    def getRandom(self):
        """
        Returns a random node's value.
        :rtype: int
        """
        res = self.head
        cur = res.next
        i = 2
        while cur:
            t = random.randint(0,i-1) % i
            if t == 0:
                res = cur
            cur = cur.next
            i = i+1
        return res.val

# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()
'''
