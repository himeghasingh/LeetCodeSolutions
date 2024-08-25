class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:

        rows, cols = len(heights), len(heights[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def canReachDestination(maxEffort):
            visited = set()
            queue = deque([(0, 0)])
            visited.add((0, 0))
            
            while queue:
                i, j = queue.popleft()
                
                if i == rows - 1 and j == cols - 1:
                    return True
                
                for idir, jdir in directions:
                    newi, newj = i + idir, j + jdir
                    if 0 <= newi < rows and 0 <= newj < cols and (newi, newj) not in visited:
                        if abs(heights[i][j] - heights[newi][newj]) <= maxEffort:
                            visited.add((newi, newj))
                            queue.append((newi, newj))
                            
            return False

        left, right = 0, max(max(row) for row in heights) - min(min(row) for row in heights)
        result = right
        
        while left <= right:
            mid = (left + right) // 2
            
            if canReachDestination(mid):
                result = mid
                right = mid - 1
            else:
                left = mid + 1
        
        return result
        # rows = len(heights)
        # cols = len(heights[0])
        # directions = [[1,0], [-1,0], [0,1], [0,-1]]
        # consdiff = float("inf")
        # memo = {}

        # def routeEffort(i, j, diff):
        #     if i == rows - 1 and j == cols - 1:
        #         return diff
            
        #     if (i, j) in memo and memo[(i, j)] <= diff:
        #         return float('inf')  
            
        #     memo[(i, j)] = diff
        #     minEffort = float('inf')
            
        #     for idir, jdir in directions:
        #         newi, newj = i + idir, j + jdir
        #         if 0 <= newi < rows and 0 <= newj < cols:
        #             currDiff = max(diff, abs(heights[i][j] - heights[newi][newj]))
        #             minEffort = min(minEffort, routeEffort(newi, newj, currDiff))
                    
        #     return minEffort

        # return routeEffort(0, 0, 0)


        # def routeEffort(i, j, diff, visited, consdiff):
        #     if i == rows - 1 and j == cols - 1 and diff < consdiff[0] :
        #         consdiff[0] = diff
        #         return
        #     if diff >= consdiff[0]:
        #         return
        #     for idir, jdir in directions:
        #         newi = i + idir
        #         newj = j + jdir
        #         if 0 <= newi < rows and 0 <= newj < cols and (newi, newj) not in visited:
        #             visited.add((newi, newj))
        #             routeEffort(newi, newj, max(diff, abs(heights[i][j] - heights[newi][newj])), visited, consdiff)
        #             visited.remove((newi, newj))
        #     return consdiff[0]

        # vis = set()
        # vis.add((0,0))
        # effort = routeEffort(0, 0, 0, vis, [float("inf")])
        # if effort != float("inf") and effort != None:
        #     return effort
        # return 0
            

        