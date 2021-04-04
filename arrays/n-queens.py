class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        allCombs = []

        def recur(curCol, queenPos):
            if curCol >= n:
                return   
            
            for curRow in range(n):
                possible = True
                for pos in queenPos:
                    if pos[0] == curCol or pos[1] == curRow or abs(pos[0] - curCol) == abs(pos[1] - curRow):
                        possible = False
                        break
    
                if possible:
                    newPos = queenPos[:]
                    newPos.append([curCol, curRow])
                    
                    if curCol == n - 1:
                        allCombs.append(newPos)
                        return
                    else:
                        recur(curCol + 1, newPos)

        recur(0, [])

        result = []        
        for sol in allCombs:
            board = [['.'] * n for _ in range(n)]
            for pos in sol:
                board[pos[0]][pos[1]] = 'Q'
            
            result.append([''.join(x) for x in board])
    
        return result