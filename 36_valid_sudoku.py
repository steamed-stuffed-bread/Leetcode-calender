# medium
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = [[x for x in y if x != '.'] for y in board]
        col = [[x for x in y if x != '.'] for y in zip(*board)]
        cell = [[board[i+m][j+n] for m in range(3) for n in range(3) if board[i+m][j+n] != '.'] for i in range(0,9,3) for j in range(0,9,3)]
        
        return all(len(set(x)) == len(x) for x in (*row, *col, *cell))
