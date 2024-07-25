class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        visited = set()
        if source == destination:
            return True
        adj = self.adjList(edges, n)
        exists = self.dfs(source, destination, adj, visited)
        return exists
    
    def adjList(self, edges, n):
        adj = defaultdict(list)
        for i in range(0, len(edges)):
            e1, e2 = edges[i]
            adj[e1].append(e2)
            adj[e2].append(e1)
        return adj

    def dfs(self, source, destination, adj, visited):
        result = False
        visited.add(source)
        if destination in adj[source]:
            return True
        else:
            neighbours = adj[source]
            for n in neighbours:
                if n not in visited:
                    result = self.dfs(n, destination, adj, visited)
                    if result:
                        break
        return result



        