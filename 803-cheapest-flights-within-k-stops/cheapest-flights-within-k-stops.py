class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:

        adj = defaultdict(list)
        for s, d, w in flights:
            adj[s].append((d, w))

        min_heap = [(0, src, 0)]
        stops = [float('inf')] * n
        
        while min_heap:
            dist, node, steps = heapq.heappop(min_heap)
            if steps > stops[node] or steps > k + 1:
                continue
            
            stops[node] = steps
            if node == dst:
                return dist
            
            for neighbor, weight in adj[node]:
                heapq.heappush(min_heap, (dist + weight, neighbor, steps + 1))
        
        return -1




























#         adjList = defaultdict(list)
#         mincosts  = [float("inf")] * n
#         for start, stop, price in flights:
#             adjList[start].append([stop, price])
#         visited = set()
#         visited.add(src)
#         finalcosts = self.cheapestFlight(src, dst, k, adjList, visited, 0 , mincosts)
#         print (finalcosts)
#         return finalcosts[-1] if finalcosts[-1]!=float("inf") and finalcosts[-1]!=0 else -1
    
#     def cheapestFlight(self, src, dst, k, adjList, visited, cost, mincosts):
#         mincosts[src] = min(mincosts[src], cost)
#         print("mincosts = ", mincosts)
#         if src == dst:
#             return
#         if k < 0:
#             return 
        
#         neighbours = adjList[src]
#         print("neighbours", neighbours)
#         for n in neighbours:
#             if n[0] not in visited:
#                 visited.add(n[0])
#                 if mincosts[n[0]] == float("inf"):
#                     self.cheapestFlight(n[0], dst, k-1, adjList, visited, cost+ n[1], mincosts)
#                 visited.remove(n[0])
#         return mincosts
#         adjList = defaultdict(list)
#         for start, stop, price in flights:
#             adjList[start].append((stop, price))
        
#         # Initialize mincosts to store the minimum cost to reach each city with a certain number of stops
#         mincosts = [[float("inf")] * (k + 2) for _ in range(n)]
#         mincosts[src][0] = 0
        
#         dfs(src, 0, k, adjList, mincosts)
        
#         # Get the minimum cost to reach dst with at most k stops
#         result = min(mincosts[dst][:k + 2])
#         return result if result != float("inf") else -1

# def dfs(node, stops, k, adjList, mincosts):
#     if stops > k:  # No need to explore more than k stops
#         return
#     for nei, price in adjList[node]:
#         if mincosts[nei][stops + 1] > mincosts[node][stops] + price:
#             mincosts[nei][stops + 1] = mincosts[node][stops] + price
#             dfs(nei, stops + 1, k, adjList, mincosts)