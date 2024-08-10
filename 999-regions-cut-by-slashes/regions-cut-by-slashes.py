class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        n = len(grid)
        new_n = 3 * n
        scaledGrid = [[0]* new_n for i in range (new_n)]
        for i in range(0, n):
            for j in range(0, n):
                ele = grid[i][j]
                if ele == '/':
                    scaledGrid[3*i][(3*j)+2] = 1
                    scaledGrid[(3*i)+1][(3*j)+1] = 1
                    scaledGrid[(3*i)+2][3*j] = 1
                if ele == '\\':
                    scaledGrid[(3*i)][(3*j)] = 1
                    scaledGrid[(3*i)+1][(3*j)+1] = 1
                    scaledGrid[(3*i)+2][(3*j)+2] = 1

        
        directions = [[1,0],[-1,0],[0,1],[0,-1]]       

        def regionCount(iindex, jindex, visited):
            visited.add((iindex, jindex))
            for idir, jdir in directions:
                new_i = iindex + idir
                new_j = jindex + jdir
                if (0 <= new_i < new_n) and (0 <= new_j < new_n) and (scaledGrid[new_i][new_j] == 0) and ((new_i, new_j) not in visited):
                    regionCount(new_i, new_j, visited)
                

        visited = set()     
        regions = 0
        for i in range (0, new_n):
            for j in range (0, new_n):
                if scaledGrid[i][j] == 0 and (i,j) not in visited:
                    regionCount(i, j, visited)
                    regions += 1
                

        return regions

                

      