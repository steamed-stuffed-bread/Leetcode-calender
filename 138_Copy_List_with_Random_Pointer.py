"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""
class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        return self.copy(head, {})
    
    def copy(self, node, G):
        if not node:
            return None
        if node in G:
            return G[node]
        newnode = Node(node.val, None, None)
        G[node] = newnode
        newnode.next = self.copy(node.next, G)
        newnode.random = self.copy(node.random, G)
        return newnode
