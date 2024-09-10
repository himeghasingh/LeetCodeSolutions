class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:

        def findIsland(i, j, islandList, grid):
                for idir, jdir in directions:
                    newi = i + idir
                    newj = j + jdir
                    if (0 <= newi < rows) and (0 <= newj < cols) and (grid[newi][newj] == 1) and (newi,newj) not in visited:
                        islandList.append([newi, newj])
                        visited.add((newi, newj))
                        findIsland(newi, newj, islandList, grid)
                return islandList, visited

        rows = len(grid1)
        cols = len(grid1[0])
        directions = [[1,0], [-1,0], [0,1], [0,-1]]
        visited = set()
        grid2islands = []
        for i in range(0, rows):
            for j in range(0, cols):
                if grid2[i][j] == 1 and (i,j) not in visited: 
                    visited.add((i,j))
                    island, visited = findIsland(i, j, [[i,j]], grid2)
                    grid2islands.append(island)

        c = 0
        
        for islands in grid2islands:
            flag = 0
            for i, j in islands:
                if grid1[i][j] != 1:
                    flag = 1
                    break
            if flag == 0:
                c += 1

        return c



                    


            

        