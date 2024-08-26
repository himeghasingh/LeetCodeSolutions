# class Solution:
#     def minimumCost(self, n: int, highways: List[List[int]], discounts: int) -> int:

#         self.results = []

#         # Building the Graph
#         graph = defaultdict(defaultdict)
#         for h in highways:
#             v1, v2, toll = h
#             graph[v1][v2] = toll
#             graph[v2][v1] = toll

#         self.findPaths(0, n-1, graph, [0], [])

#         cost = float("inf")
#         if not self.results:
#             return -1
#         for res in self.results:
#             cost = min(cost, self.applyDiscount(res, discounts))
#         return cost

#     def applyDiscount(self, tollList, discounts):
#         finalcost = 0
#         tollList.sort(reverse=True)
#         i = 0
#         for i in range(0, len(tollList)):
#             if discounts>0:
#                 finalcost += (tollList[i]//2)
#                 discounts -= 1
#             else:
#                 finalcost += tollList[i]
#         return finalcost

#     def findPaths(self, source, dest, graph, path, toll):
#         if source == dest:
#             self.results.append(toll.copy())
#             return 
#         neighbors = graph[source]
#         for n in neighbors:
#             if n not in path:
#                 path.append(n)
#                 toll.append(graph[source][n])

#                 self.findPaths(n, dest, graph, path, toll )
#                 path.pop()  
#                 toll.pop()


import heapq
from collections import defaultdict, deque
from typing import List

class Solution:
    def minimumCost(self, n: int, highways: List[List[int]], discounts: int) -> int:
        graph = defaultdict(list)
        for src, dst, toll in highways:
            graph[src].append((dst, toll))
            graph[dst].append((src, toll))

        minHeap = [(0, 0, discounts)]  
        visited = {}  

        while minHeap:

            currcost, node, remdisc = heapq.heappop(minHeap)
            if node == n - 1:
                return currcost
            if (node, remdisc) in visited and visited[(node, remdisc)] <= currcost:
                continue

            visited[(node, remdisc)] = currcost

            for neighbor, toll in graph[node]:
                newcost = currcost + toll
                if (neighbor, remdisc) not in visited :
                    heapq.heappush(minHeap, (newcost, neighbor, remdisc))

                if remdisc > 0:
                    newcost_with_discount = currcost + toll // 2
                    if (neighbor, remdisc - 1) not in visited or visited[(neighbor, remdisc - 1)] > newcost_with_discount:
                        heapq.heappush(minHeap, (newcost_with_discount, neighbor, remdisc - 1))

        return -1 

