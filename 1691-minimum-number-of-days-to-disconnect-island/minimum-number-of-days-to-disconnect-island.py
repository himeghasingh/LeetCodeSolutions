class Solution:
    def minDays(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        def countIslands():
            visited = set()
            c = 0
            for i in range(0, rows):
                for j in range(0, cols):
                    if grid[i][j] == 1 and (i,j) not in visited:
                        findIsland(i, j, visited)
                        c +=1
            return c

        def findIsland(i, j, visited):
            visited.add((i,j))
            direction = [[1,0],[-1,0],[0,1],[0,-1]]
            for idir, jdir in direction:
                new_i = i + idir
                new_j = j + jdir
                if 0 <= new_i < rows and 0 <= new_j <cols and (new_i, new_j) not in visited and grid[new_i][new_j] == 1:
                    findIsland(new_i, new_j, visited)
        
        if countIslands() != 1:
            return 0
        
        for i in range(0, rows):
            for j in range(0, cols):
                if grid[i][j] == 1:
                    grid[i][j] = 0
                    if countIslands() != 1:
                        return 1
                    grid[i][j] = 1
        return 2