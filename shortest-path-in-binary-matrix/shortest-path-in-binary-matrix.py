class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:

        n = len(grid)
        if grid[0][0] != 0 or grid[n-1][n-1] != 0:
            return -1

        queue = deque()
        visited = set()
        visited.add((0,0))
        queue.append([0,0,1])
        direction = [[1,0], [-1,0], [0,1], [0,-1], [1,1], [1,-1], [-1,1], [-1,-1]]
        shortest = float("inf")

        while queue:
            i, j, dist = queue.popleft()
            if i == n-1 and j == n-1:
                shortest = min(shortest, dist)
            for idir, jdir in direction:
                newi = i + idir
                newj = j + jdir
                if 0 <= newi < n and 0 <= newj < n and (newi, newj) not in visited and grid[newi][newj] == 0:
                    visited.add((newi, newj))
                    queue.append([newi, newj, dist+1])
        return shortest if shortest!=float("inf") else -1

        