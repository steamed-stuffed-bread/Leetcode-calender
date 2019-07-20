# medium
"""
# Definition for a QuadTree node.
class Node(object):
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""
class Solution(object):
    def construct(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: Node
        """
        self.grid = grid
        return self.helper(0, 0, len(grid))
        
    def helper(self, x, y, n):
        if n <= 0:
            return None
        for i in range(x,x+n):
            for j in range(y,y+n):
                if self.grid[i][j] != self.grid[x][y]:
                    return Node('*', False,
                        self.helper(x,y,n/2),
                        self.helper(x,y+n/2,n/2),
                        self.helper(x+n/2,y,n/2),
                        self.helper(x+n/2,y+n/2,n/2))
        return Node(self.grid[x][y] == 1, True, None, None, None, None)
