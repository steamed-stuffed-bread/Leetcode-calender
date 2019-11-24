"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
            return None
        q = [root]
        while q:
            n = len(q)
            for i in range(n):
                tmp = q[len(q)-1]
                q.pop()
                if i < n-1:
                    tmp.next = q[len(q)-1]
                if tmp.left:
                    q.insert(0, tmp.left)
                if tmp.right:
                    q.insert(0, tmp.right)
        return root
        
        
        
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
            return None
        q = root.next
        while q:
            if q.left:
                q = q.left
                break
            if q.right:
                q = q.right
                break
            q = q.next
        if root.right:
            root.right.next = q
        if root.left:
            root.left.next = root.right if root.right else q
        self.connect(root.left)
        self.connect(root.right)
        return root
        
        
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
            return None
        dummy = Node(0)
        head = root
        cur = dummy
        # cur = Node(0)
        # dummy = cur     # dummy point to cur, when cur.next be given a value, dummy.next had a same value.
        while root:
            if root.left:
                cur.next = root.left
                cur = cur.next
            if root.right:
                cur.next = root.right
                cur = cur.next
            root = root.next
            if not root:
                cur = dummy
                root = dummy.next
                dummy.next = None
        return head
