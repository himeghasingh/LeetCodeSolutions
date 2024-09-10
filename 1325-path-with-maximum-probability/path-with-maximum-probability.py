class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        adjMatrix = defaultdict(list)
        for edge, prob in zip(edges, succProb):
            src, dest = edge
            adjMatrix[src].append([dest, prob])
            adjMatrix[dest].append([src, prob])


        queue = deque()
        queue.append([start_node, 1])
        visited = [0] * n
        visited[start_node] = 1  

        while queue:
            node, prob = queue.popleft()
            neighbours = adjMatrix[node]
            for neinode, neiprob in neighbours:
                newprob = prob * neiprob
                if newprob > visited[neinode]:
                    visited[neinode] = newprob
                    queue.append((neinode, newprob))

        return visited[end_node] if visited[end_node] > 0 else 0





        
            



         # def findPath(nodeid, nodeprob, visited, maxprob):
        #     if nodeid == end_node and nodeprob > maxprob[0]:
        #         maxprob[0] = nodeprob
        #         return
        #     neighbours = adjMatrix[nodeid]
        #     for neinode, neiprob in neighbours:
        #         if neinode not in visited:
        #             visited.add(neinode)
        #             findPath(neinode, neiprob * nodeprob, visited, maxprob)
        #             visited.remove(neinode)

        
        
        # findPath(start_node, 1, visited, maxprob)

        # if maxprob[0] == float("-inf"):
        #     return 0
        # return maxprob[0]

        












