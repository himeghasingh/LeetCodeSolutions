class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        rottingQueue = deque()
        total = rows * cols
        empty = 0
        rotten = 0
        mins = 0
        directions =[[1,0], [-1,0], [0,1], [0,-1]]
        
        for i in range(0, rows):
            for j in range(0, cols):
                if grid[i][j] == 0:
                    empty += 1
                if grid[i][j] == 2:
                    rottingQueue.append([i,j,0])
                    rotten += 1

        while rottingQueue:
            i, j, mins = rottingQueue.popleft()
            for idir, jdir in directions:
                newi = i + idir
                newj = j + jdir
                if 0 <= newi < rows and 0 <= newj < cols and grid[newi][newj] == 1:
                    grid[newi][newj] = 2
                    if [newi, newj] not in rottingQueue:
                        rottingQueue.append([newi, newj, mins+1])
                        rotten += 1

        if empty + rotten != total:
            return -1

        return mins
# The logic to calculate the mins is, each time we add a set of new rotten oranges, we increase the minutes to that set by 1.
# as the rotten oranges keep getting added to the queue, the orange that is appended last will have the max number of mins because we are doing bfs
# so we return mins, as that was the last minutes field that was popped from the queue.



















        #     temp = set()
        #     tempremove = set()
        #     for rot in rottingQueue:
        #         flag = False
        #         iindex = rot[0]
        #         jindex = rot[1]
        #         visitedRotten.add((iindex,jindex))
        #         tempremove.add(rot)
        #         if iindex + 1 < rows and (iindex+1, jindex) not in rottingQueue and grid[iindex+1][jindex] == 1:
        #             temp.add((iindex+1, jindex))
        #             grid[iindex+1][jindex] = 2
        #             flag = True
        #         if iindex - 1 >= 0 and (iindex-1, jindex) not in rottingQueue and grid[iindex-1][jindex] == 1:
        #             temp.add((iindex-1, jindex))
        #             grid[iindex-1][jindex] = 2
        #             flag = True
        #         if jindex + 1 <  cols and (iindex, jindex+1) not in rottingQueue and grid[iindex][jindex+1] == 1:
        #             temp.add((iindex, jindex+1))
        #             grid[iindex][jindex+1] = 2
        #             flag = True
        #         if jindex - 1 >=0 and (iindex, jindex-1) not in rottingQueue and grid[iindex][jindex-1] == 1:
        #             temp.add((iindex, jindex-1))
        #             grid[iindex][jindex-1] = 2
        #             flag = True

        #     for t in tempremove:
        #         rottingQueue.remove(t)
        #     for t in temp:
        #         rottingQueue.add(t)
        #     if rottingQueue:
        #         minutes += 1
            
        # stillfresh = total - len(visitedRotten) - empty
        # if stillfresh > 0:
        #     return -1
        # else:
        #     return minutes
        

            



        