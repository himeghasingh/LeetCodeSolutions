class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        count = 0

        def checkSubmatrix(r, c):
            distinct = set()
            firstRowSum = sum(grid[r][c:c+3]) 
            leftDiag = grid[r][c]+ grid[r+1][c+1] + grid[r+2][c+2]
            rightDiag = grid[r][c+2]+ grid[r+1][c+1] + grid[r+2][c]
            if leftDiag != firstRowSum or rightDiag != firstRowSum:
                return False
            for j in range(c, c+3):
                colsum = 0
                for i in range(r, r+3):
                    if grid[i][j] < 1 or grid[i][j] > 9 or grid[i][j] in distinct:
                        return False
                    distinct.add(grid[i][j])
                    if sum(grid[i][c:c+3]) != firstRowSum:
                        return False
                    colsum += grid[i][j]
                if colsum != firstRowSum:
                    return False
            return True



        for row in range(0, rows-2):
            for col in range(0, cols-2):
                if checkSubmatrix(row,col):
                    count += 1
        return count

