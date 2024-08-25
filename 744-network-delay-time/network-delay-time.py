class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        timeMatrix = [[float("inf")] * n for i in range(n)]
        for i in range(0, n):
            timeMatrix[i][i] = 0                
        for src, dst, t in times:
            timeMatrix[src-1][dst-1] = t
        for j in range(0, n):
            for i in range(0, n):
                for m in range(0, n):
                    if timeMatrix[i][m] > timeMatrix[i][j] + timeMatrix[j][m]:
                        timeMatrix[i][m] = timeMatrix[i][j] + timeMatrix[j][m]
        timetaken = timeMatrix[k-1]
        restime = max(timetaken)
        if restime != float("inf"):
            return restime
        return -1



        #######TLE######
        # def findshortestpath(node, time, target, visited, timetaken):
        #     if node == target and time < timetaken[0]:
        #         timetaken[0] = time
        #         return
        #     if time > timetaken[0]:
        #         return
        #     neighbours = adjMatrix[node]
        #     for nei, neitime in neighbours:
        #         if nei not in visited:
        #             visited.add(nei)
        #             findshortestpath(nei, time+neitime, target, visited, timetaken)
        #             visited.remove(nei)
        #     return timetaken[0]
        
        
        # adjMatrix = defaultdict(list)
        # for src, dst, t in times:
        #     adjMatrix[src].append([dst, t])
        # totaltime = float("-inf")
       
                    
        # for i in range(1, n+1):
        #     if i != k:
        #         leasttime = findshortestpath(k, 0, i, set(), [float("inf")])
        #         totaltime = max(totaltime, leasttime)
        #         if leasttime == float('inf'):
        #             return -1
        # return totaltime
            
                

    