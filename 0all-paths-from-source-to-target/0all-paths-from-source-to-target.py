class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph)
        source = 0 
        dest = n - 1
        self.results = []
        self.dfs(source, dest, graph, [source])
        return (self.results)



    def dfs(self, source, dest, graph, path):
        if source == dest:
            self.results.append(list(path))
            return
        for nei in graph[source]:
            path.append(nei)
            self.dfs(nei, dest, graph, path)
            path.pop()
        return


        