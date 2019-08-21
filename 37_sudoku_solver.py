# hard
class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        self.sheet = ['1','2','3','4','5','6','7','8','9']
        self.board = board
        self.helper(0, 0)
    
    def helper(self,x,y):
        if x == 9:
            return True
        if y >= 9:
            return self.helper(x+1,0)
        if self.board[x][y] != '.':
            return self.helper(x,y+1)
        for c in self.sheet:
            if not self.isValid(x, y, ord(c)):
                continue
            self.board[x][y] = c
            if self.helper(x, y+1):
                return True
            self.board[x][y] = '.'
        return False
        
    def isValid(self,i,j,val):
        for m in range(9):
            if ord(self.board[i][m]) == val:
                return False
        for n in range(9):
            if ord(self.board[n][j]) == val:
                return False
        pos_x = i-i%3
        pos_y = j-j%3
        for m in range(3):
            for n in range(3):
                if ord(self.board[m+pos_x][n+pos_y]) == val:
                    return False
        return True
