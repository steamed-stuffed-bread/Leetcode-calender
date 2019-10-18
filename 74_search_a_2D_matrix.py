# medium
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]:
            return False
        row = len(matrix)
        col = len(matrix[0])
        i = 0
        j = col - 1
        while i < row and j >= 0:
            if target == matrix[i][j]:
                return True
            elif target > matrix[i][j]:
                i = i + 1
            else:
                j = j - 1
        return False
