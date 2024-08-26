class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        # a node cant be in the same set as its neighbours
        n = len(graph)
        nodecolors = [0] * n 

        def bfs(start):

            queue = deque()
            queue.append([start,1])
            nodecolors[start] = 1
            c = 1
            while queue:
                node, color = queue.popleft()
                neighbours = graph[node]
                for nei in neighbours:
                    if nodecolors[nei] == 0:
                        nodecolors[nei] = color * -1
                        queue.append([nei, color*-1])
                        c += 1
                    else:
                        if nodecolors[nei] != color * -1:
                            return False
            return True
        
        for i in range(n):
            if nodecolors[i] == 0: 
                if not bfs(i):
                    return False
        
        return True




        