class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:

        graph = defaultdict(defaultdict)
        for eq,val in zip(equations, values):
            graph = self.buildGraph(graph, eq, val)
        print(graph)
        qres = []
        
        for q in queries:
            a = q[0]
            b = q[1]
            print("\nquery:  ", q)
            if a not in graph or b not in graph:
                qres.append(-1.0)
            elif a == b:
                qres.append(1.0)
            else:
                visited = set()
                qres.append(self.calc(a, b, graph, 1, visited))
               
        print(qres)
        return qres


    def calc(self, a, b, graph, mul, visited):
        
        visited.add(a)
        print("\n")
        print("visisted after adding:", visited)
        res = -1.0
        if b in graph[a]:
            found = True
            visited.remove(a)
            return (mul*graph[a][b])
        else:
            for nei in graph[a]:
                if nei not in visited:
                    res = self.calc(nei, b, graph, graph[a][nei]*mul, visited)
                    if res != -1.0:
                        break
        visited.remove(a)
        print("visisted after removing:", visited)
        return res


    def buildGraph(self, graph, eq, val):
        a = eq[0]
        b = eq[1]
        graph[a][b] = val
        graph[b][a] = 1/val
        return graph

# class UnionFind:
#     def __init__(self, n, vertex):
#         self.rank = defaultdict()
#         self.root = defaultdict()
#         for v in vertex:
#             self.root[v] = v
#             self.rank[v] = 1





























#     def find(self, x):
#         while x != self.root[x]:
#             x = self.root[x]
#         return x

#     def union(self, x, y):
#         xroot = self.find(x)
#         yroot = self.find(y)

#         if xroot != yroot:
#             xrank = self.rank[xroot]
#             yrank = self.rank[yroot]
#             if xrank > yrank:
#                 self.root[yroot] = xroot  
#             elif yrank > xrank:
#                 self.root[xroot] = yroot   
#             elif xrank == yrank:
#                 self.root[yroot] = xroot 
#                 self.rank[xroot] += 1
#     def printstate(self):
#         print(self.root)



  